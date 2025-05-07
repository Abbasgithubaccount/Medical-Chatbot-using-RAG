import streamlit as st
from medibot import generate_answer  # Ensure this function is defined in medibot.py

st.set_page_config(page_title="Medical Chatbot", layout="wide")
st.title("🩺 Medical Chatbot (RAG-powered)")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_query = st.text_input("Ask a medical question:")

if user_query:
    with st.spinner("Generating answer..."):
        response = generate_answer(user_query)
        st.session_state.chat_history.append(("You", user_query))
        st.session_state.chat_history.append(("Bot", response))

for speaker, message in st.session_state.chat_history:
    st.markdown(f"**{speaker}:** {message}")
