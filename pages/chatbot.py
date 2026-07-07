import streamlit as st
import base64
from PIL import Image

st.set_page_config(
    page_title="EduChat",
    page_icon="assets/eve.png",
    layout="wide"
)

# Load and encode image
with open("assets/eve.png", "rb") as img_file:
    img_data = base64.b64encode(img_file.read()).decode()

# Display title with inline image using HTML
st.markdown(
    f"""
    <h1 style='display: flex; align-items: center;'>
        <img src='data:image/png;base64,{img_data}' style='width: 120px; height: 120px; margin-right: 10px;'>
        EduChat
    </h1>
    """,
    unsafe_allow_html=True
)

st.caption("Your educational AI assistant")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hello! 👋 I'm EduChat. How can I help you today?"
        }
    ]

# Display messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Type your message..."):

    # Show user message
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.markdown(prompt)

    # Temporary response
    response = "This is a placeholder response."

    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })

    with st.chat_message("assistant"):
        st.markdown(response)