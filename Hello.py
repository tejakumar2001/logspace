import streamlit as st
import json

# Load responses from JSON file
with open("responses.json", "r") as file:
    responses = json.load(file)

st.title("Echo Bot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    st.markdown(f"**{message['role']}:** {message['content']}")

# React to user input
prompt = st.chat_input("You:")

if prompt:
        # Display user message in chat message container
        st.markdown(f"**You:** {prompt}")
        # Add user message to chat history
        st.session_state.messages.append({"role": "You", "content": prompt})

        # Get response from JSON file based on user input
        response = responses.get(prompt.lower(), "Sorry, I didn't understand that.")
        
        # Display assistant response in chat message container
        st.markdown(f"**Echo Bot:** {response}")
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "Echo Bot", "content": response})
