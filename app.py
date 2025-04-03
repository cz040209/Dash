import streamlit as st

# Function for processing the chatbot response
def chatbot(input_text, history):
    # Generate a simple response (this can be replaced with more advanced logic)
    response = f"Chatbot says: {input_text}"
    
    # Add user message and chatbot response to history
    history.append({"role": "user", "message": input_text})
    history.append({"role": "chatbot", "message": response})
    
    return history

# Streamlit UI components
st.title("Chatbot Interface")
st.subheader("Chat with the bot! 👇")

# Initialize history list to keep track of conversation
if 'history' not in st.session_state:
    st.session_state.history = []

# Create the input field for user message
input_text = st.text_input("You: ", "")

# If user submits a message, process it and update the history
if input_text:
    st.session_state.history = chatbot(input_text, st.session_state.history)

# Display the conversation as chat blocks (user and chatbot messages)
if st.session_state.history:
    for msg in st.session_state.history:
        if msg["role"] == "user":
            st.markdown(f'<div style="text-align: left; padding: 10px; background-color: #DCF8C6; border-radius: 5px;">{msg["message"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div style="text-align: right; padding: 10px; background-color: #ECECEC; border-radius: 5px;">{msg["message"]}</div>', unsafe_allow_html=True)

