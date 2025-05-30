import streamlit as st

# Set page title and layout
st.set_page_config(page_title="Simple Rule-Based Chatbot", layout="centered")

st.title("💬 Simple Rule-Based Chatbot")
st.write("Type something and I will respond!")

# Initialize chat history if not already done
if "messages" not in st.session_state:
    st.session_state.messages = []

# Function to generate chatbot response based on user input
def get_bot_response(user_msg):
    user_msg = user_msg.lower()
    if "hello" in user_msg or "hi" in user_msg:
        return "Hello! How can I help you today?"
    elif "how are you" in user_msg:
        return "I'm just a bot, but I'm doing great! Thanks for asking."
    elif "bye" in user_msg or "exit" in user_msg:
        return "Goodbye! Have a nice day!"
    else:
        return "Sorry, I don't understand that yet."

# User input
user_input = st.text_input("You:", key="input")

# When user submits input
if user_input:
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Get bot response
    response = get_bot_response(user_input)
    
    # Add bot response to chat history
    st.session_state.messages.append({"role": "bot", "content": response})

# Display chat messages
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"**You:** {msg['content']}")
    else:
        st.markdown(f"**Bot:** {msg['content']}")
