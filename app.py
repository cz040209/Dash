import streamlit as st

# Define a function to process the chatbot response
def chatbot(input_text, history):
    response = f"Chatbot says: {input_text}"
    history.append(("You", input_text))
    history.append(("Chatbot", response))
    return history, response

# Streamlit UI components
st.title("Chatbot Interface")
st.subheader("This is a simple chatbot interface powered by Streamlit")

history = []

# Create the input field
input_text = st.text_input("Type your message:")

if input_text:
    history, response = chatbot(input_text, history)

# Display the chat history
if history:
    for message in history:
        st.text(f"{message[0]}: {message[1]}")
