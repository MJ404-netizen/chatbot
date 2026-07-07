import streamlit as st

st.set_page_config(
    page_title="Login",
    page_icon="🔐",
    layout="centered"
)

st.title("🤖 EduChat")
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