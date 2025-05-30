
# Simple Rule-Based Chatbot using Streamlit

This is a basic chatbot built with Streamlit in Python. It does **not** use any external API — instead, it replies using simple conditional logic (if-else statements).

---

## How it works

- The app uses Streamlit to create a web interface.
- User inputs a message.
- The chatbot checks the message for certain keywords and replies accordingly.
- The conversation history is maintained using Streamlit's session state.

---

## Code

```python
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
```

---

## How to run locally

1. Make sure you have Python installed (preferably 3.8+).
2. Install Streamlit:  
   ```bash
   pip install streamlit
   ```
3. Save the code in a file, for example, `chatbot.py`.
4. Run the Streamlit app:  
   ```bash
   streamlit run chatbot.py
   ```
5. Your browser will open at `http://localhost:8501`, where you can chat with the bot.

---

## Next steps (optional)

- Add more rules to the bot for better responses.
- Improve UI with custom CSS or Streamlit components.
- Add logging of conversations.

---

Feel free to use and share!

---

**Author:** Rohit singh Bisht
**Date:** 2025-05-30
