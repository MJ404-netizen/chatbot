import streamlit as st
import base64
from PIL import Image

st.set_page_config(
    page_title="Login",
    page_icon="🔐",
    layout="centered"
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

st.subheader("Welcome Back")

with st.form("login_form"):

    email = st.text_input(
        "Email",
        placeholder="Enter your email"
    )

    password = st.text_input(
        "Password",
        type="password",
        placeholder="Enter your password"
    )

    remember = st.checkbox("Remember me")

    login = st.form_submit_button("Login")

if login:
    st.success("Login button clicked (authentication coming later).")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.button("Forgot Password")

with col2:
    st.button("Create Account")