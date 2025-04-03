import streamlit as st

# Define a function to process the chatbot response
def chatbot(input_text, history):
    response = f"Chatbot says: {input_text}"  # You can customize this to make the chatbot smarter
    history.append(("You", input_text))
    history.append(("Chatbot", response))
    return history, response

# Streamlit UI components
st.title("Chatbot Interface")
st.subheader("This is a simple chatbot interface powered by Streamlit")

# Initialize chat history
if 'history' not in st.session_state:
    st.session_state.history = []

# Create the input field
input_text = st.text_input("Type your message:")

# Handle input and chat response
if input_text:
    st.session_state.history, response = chatbot(input_text, st.session_state.history)

# Display the chat history in a conversation-like format
for message in st.session_state.history:
    if message[0] == "You":
        st.markdown(f"**{message[0]}:** {message[1]}")  # User message
    else:
        st.markdown(f"<p style='color:blue;'><strong>{message[0]}:</strong> {message[1]}</p>", unsafe_allow_html=True)  # Chatbot message
