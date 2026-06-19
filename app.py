"""
Xeria Bank Assistant
Streamlit Frontend powered by Rasa Open Source NLU

This application contains NO rule-based chatbot logic and NO if/else
response mapping. Every reply shown to the user is obtained from the
running Rasa server via its REST and NLU parse endpoints.

Run the Rasa server first:
    rasa run --enable-api --cors "*" --port 5005

Then run this app:
    streamlit run app.py
"""

import streamlit as st
import requests
from datetime import datetime

# ============================================================
# CONFIGURATION
# ============================================================

RASA_SERVER_URL = "http://localhost:5005"
RASA_REST_ENDPOINT = f"{RASA_SERVER_URL}/webhooks/rest/webhook"
RASA_PARSE_ENDPOINT = f"{RASA_SERVER_URL}/model/parse"
RASA_STATUS_ENDPOINT = f"{RASA_SERVER_URL}/"
REQUEST_TIMEOUT = 10

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Xeria Bank Assistant",
    page_icon="🏦",
    layout="centered",
    initial_sidebar_state="expanded",
)

# ============================================================
# BANKING THEME — CUSTOM CSS
# ============================================================

CUSTOM_CSS = """
<style>
    .stApp {
        background-color: #0b1f3a;
    }

    #MainMenu, footer, header {visibility: hidden;}

    .xeria-header {
        background: linear-gradient(135deg, #0b1f3a 0%, #143869 100%);
        padding: 22px 18px;
        border-radius: 12px;
        border: 1px solid #d4af37;
        margin-bottom: 18px;
        text-align: center;
    }

    .xeria-header h1 {
        color: #d4af37;
        font-size: 28px;
        margin: 0;
        letter-spacing: 1px;
    }

    .xeria-header p {
        color: #e6e6e6;
        margin: 4px 0 0 0;
        font-size: 14px;
    }

    .chat-container {
        background-color: #11284a;
        border-radius: 12px;
        padding: 16px;
        border: 1px solid #1f3d66;
    }

    .meta-badge {
        display: inline-block;
        background-color: #1f3d66;
        color: #d4af37;
        border: 1px solid #d4af37;
        border-radius: 6px;
        padding: 2px 8px;
        font-size: 11px;
        margin-right: 6px;
        margin-top: 4px;
    }

    .confidence-high {
        color: #4caf50;
        font-weight: 600;
    }

    .confidence-medium {
        color: #ffb300;
        font-weight: 600;
    }

    .confidence-low {
        color: #ef5350;
        font-weight: 600;
    }

    .status-online {
        color: #4caf50;
        font-weight: 600;
    }

    .status-offline {
        color: #ef5350;
        font-weight: 600;
    }

    section[data-testid="stSidebar"] {
        background-color: #0b1f3a;
        border-right: 1px solid #d4af37;
    }

    section[data-testid="stSidebar"] * {
        color: #e6e6e6;
    }
</style>
"""

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# ============================================================
# SESSION STATE INITIALIZATION
# ============================================================

if "messages" not in st.session_state:
    st.session_state.messages = []

if "rasa_sender_id" not in st.session_state:
    st.session_state.rasa_sender_id = (
        f"streamlit_user_{datetime.now().strftime('%Y%m%d%H%M%S')}"
    )


# ============================================================
# RASA COMMUNICATION FUNCTIONS
# ============================================================

def check_rasa_server_status() -> bool:
    """Returns True if the Rasa server is reachable."""
    try:
        response = requests.get(RASA_STATUS_ENDPOINT, timeout=5)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False


def get_nlu_parse(user_message: str):
    """
    Calls Rasa's /model/parse endpoint to obtain the predicted
    intent and confidence score for the given message.
    """
    payload = {"text": user_message}
    try:
        response = requests.post(
            RASA_PARSE_ENDPOINT, json=payload, timeout=REQUEST_TIMEOUT
        )
        if response.status_code == 200:
            data = response.json()
            intent_data = data.get("intent", {}) or {}
            intent_name = intent_data.get("name", "unknown")
            confidence = intent_data.get("confidence", 0.0)
            return intent_name, float(confidence)
        return "unknown", 0.0
    except requests.exceptions.RequestException:
        return "server_unavailable", 0.0


def get_rasa_bot_response(user_message: str, sender_id: str):
    """
    Calls Rasa's REST webhook endpoint to obtain the bot's
    conversational response(s) for the given message.
    """
    payload = {"sender": sender_id, "message": user_message}
    try:
        response = requests.post(
            RASA_REST_ENDPOINT, json=payload, timeout=REQUEST_TIMEOUT
        )
        if response.status_code == 200:
            bot_messages = response.json()
            texts = [m.get("text", "") for m in bot_messages if m.get("text")]
            if texts:
                return texts
            return ["I did not receive a recognizable response from the assistant."]
        return [f"Rasa server returned status code {response.status_code}."]
    except requests.exceptions.ConnectionError:
        return [
            "Unable to connect to the Rasa server. "
            "Please ensure it is running on http://localhost:5005."
        ]
    except requests.exceptions.Timeout:
        return ["The Rasa server took too long to respond. Please try again."]
    except requests.exceptions.RequestException as exc:
        return [f"An error occurred while contacting the Rasa server: {exc}"]


def confidence_css_class(confidence: float) -> str:
    if confidence >= 0.75:
        return "confidence-high"
    if confidence >= 0.45:
        return "confidence-medium"
    return "confidence-low"


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:
    st.markdown("### 🏦 Xeria Bank Assistant")
    st.markdown("---")

    server_online = check_rasa_server_status()
    if server_online:
        st.markdown(
            "**Rasa Server Status:** <span class='status-online'>● Online</span>",
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            "**Rasa Server Status:** <span class='status-offline'>● Offline</span>",
            unsafe_allow_html=True,
        )
        st.caption("Start it with: rasa run --enable-api --cors \"*\"")

    st.markdown("---")
    st.markdown("**Server Endpoint**")
    st.code(RASA_SERVER_URL, language=None)

    st.markdown("**Session ID**")
    st.code(st.session_state.rasa_sender_id, language=None)

    st.markdown("---")
    st.markdown("**Powered By**")
    st.markdown("- Rasa Open Source NLU\n- Streamlit\n- Local Intent Classification")

    st.markdown("---")
    if st.button("🗑️ Clear Chat History", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

# ============================================================
# HEADER
# ============================================================

st.markdown(
    """
    <div class="xeria-header">
        <h1>🏦 Xeria Bank Assistant</h1>
        <p>NLU-Powered Banking Support — Intent Classification In Real Time</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# CHAT HISTORY DISPLAY
# ============================================================

for msg in st.session_state.messages:
    if msg["role"] == "user":
        with st.chat_message("user", avatar="🧑"):
            st.write(msg["content"])
            conf = msg.get("confidence", 0.0)
            intent = msg.get("intent", "unknown")
            css_class = confidence_css_class(conf)
            st.markdown(
                f"<span class='meta-badge'>Intent: {intent}</span>"
                f"<span class='meta-badge {css_class}'>Confidence: {conf:.2f}</span>",
                unsafe_allow_html=True,
            )
    else:
        with st.chat_message("assistant", avatar="🏦"):
            st.write(msg["content"])

# ============================================================
# CHAT INPUT
# ============================================================
st.markdown("### Quick Services")

col1, col2 = st.columns(2)

with col1:
    if st.button("💰 Account Services"):
        st.session_state.quick_message = "account"

    if st.button("🏠 Loans"):
        st.session_state.quick_message = "loan"

    if st.button("📍 Branch Locator"):
        st.session_state.quick_message = "branch"

with col2:
    if st.button("💳 Card Services"):
        st.session_state.quick_message = "card"

    if st.button("📈 Fixed Deposit"):
        st.session_state.quick_message = "fixed deposit"

    if st.button("📝 Complaint"):
        st.session_state.quick_message = "complaint"
user_input = st.chat_input("Ask about your account, cards, loans, or branches...")

if "quick_message" in st.session_state:
    user_input = st.session_state.quick_message
    del st.session_state.quick_message

if user_input:
    intent_name, confidence = get_nlu_parse(user_input)

    st.session_state.messages.append(
        {
            "role": "user",
            "content": user_input,
            "intent": intent_name,
            "confidence": confidence,
        }
    )

    bot_replies = get_rasa_bot_response(user_input, st.session_state.rasa_sender_id)

    for reply in bot_replies:
        st.session_state.messages.append({"role": "assistant", "content": reply})

    st.rerun()