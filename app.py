import streamlit as st

# Function for the homepage
def homepage():
    st.title("Welcome to the Home Page")
    st.write("This is the home page of the app.")
    
# Function for the chatbot page
def chatbot_page():
    st.title("Chatbot Interface")
    st.write("Chatbot page goes here!")
    input_text = st.text_input("Type your message:")
    if input_text:
        st.write(f"Chatbot says: {input_text}")  # Simple echo response (replace with real chatbot logic)
        
# Function for the about page
def about_page():
    st.title("About")
    st.write("This is a simple app to demonstrate page navigation in Streamlit.")

# Navigation sidebar
page = st.sidebar.selectbox("Choose a page", ["Home", "Chatbot", "About"])

# Conditionally display the selected page
if page == "Home":
    homepage()
elif page == "Chatbot":
    chatbot_page()
elif page == "About":
    about_page()
