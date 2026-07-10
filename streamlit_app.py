# import streamlit as st
# from openai import OpenAI

# # Show title and description.
# st.title("💬 Chatbot")
# st.write(
#     "This is a simple chatbot that uses OpenAI's GPT-3.5 model to generate responses. "
#     "To use this app, you need to provide an OpenAI API key, which you can get [here](https://platform.openai.com/account/api-keys). "
#     "You can also learn how to build this app step by step by [following our tutorial](https://docs.streamlit.io/develop/tutorials/llms/build-conversational-apps)."
# )

# # Ask user for their OpenAI API key via `st.text_input`.
# # Alternatively, you can store the API key in `./.streamlit/secrets.toml` and access it
# # via `st.secrets`, see https://docs.streamlit.io/develop/concepts/connections/secrets-management
# openai_api_key = st.text_input("OpenAI API Key", type="password")
# if not openai_api_key:
#     st.info("Please add your OpenAI API key to continue.", icon="🗝️")
# else:

#     # Create an OpenAI client.
#     client = OpenAI(api_key=openai_api_key)

#     # Create a session state variable to store the chat messages. This ensures that the
#     # messages persist across reruns.
#     if "messages" not in st.session_state:
#         st.session_state.messages = []

#     # Display the existing chat messages via `st.chat_message`.
#     for message in st.session_state.messages:
#         with st.chat_message(message["role"]):
#             st.markdown(message["content"])

#     # Create a chat input field to allow the user to enter a message. This will display
#     # automatically at the bottom of the page.
#     if prompt := st.chat_input("What is up?"):

#         # Store and display the current prompt.
#         st.session_state.messages.append({"role": "user", "content": prompt})
#         with st.chat_message("user"):
#             st.markdown(prompt)

#         # Generate a response using the OpenAI API.
#         stream = client.chat.completions.create(
#             model="gpt-3.5-turbo",
#             messages=[
#                 {"role": m["role"], "content": m["content"]}
#                 for m in st.session_state.messages
#             ],
#             stream=True,
#         )

#         # Stream the response to the chat using `st.write_stream`, then store it in 
#         # session state.
#         with st.chat_message("assistant"):
#             response = st.write_stream(stream)
#         st.session_state.messages.append({"role": "assistant", "content": response})



# import streamlit as st
# import base64
# from PIL import Image

# st.set_page_config(
#     page_title="EduChat",
#     page_icon="assets/eve.png",
#     layout="wide"
# )

# # Load and encode image
# with open("assets/eve.png", "rb") as img_file:
#     img_data = base64.b64encode(img_file.read()).decode()

# # Display title with inline image using HTML
# st.markdown(
#     f"""
#     <h1 style='display: flex; align-items: center;'>
#         <img src='data:image/png;base64,{img_data}' style='width: 120px; height: 120px; margin-right: 10px;'>
#         EduChat
#     </h1>
#     """,
#     unsafe_allow_html=True
# )

# st.subheader("Your Educational AI Assistant")

# st.write("""
# Learn smarter with AI.

# • Ask educational questions
# • Get instant explanations
# • Improve your learning experience
# """)

# col1, col2 = st.columns(2)

# with col1:
#     if st.button("🔐 Login", use_container_width=True):
#         st.switch_page("pages/login.py")

# with col2:
#     if st.button("📝 Register", use_container_width=True):
#         st.switch_page("pages/register.py")


import streamlit as st
import base64
from PIL import Image

st.set_page_config(
    page_title="EduChat",
    page_icon="assets/eve.png",
    layout="wide",
    initial_sidebar_state="collapsed"  # Hide sidebar
)

# Check if user is logged in
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if st.session_state.logged_in:
    # Show main app with sidebar navigation
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
    st.write(f"Welcome back, {st.session_state.username}!")
    
    with st.sidebar:
        st.image("assets/eve.png", width=100)
        st.write(f"👋 {st.session_state.username}")
        if st.button("🚪 Sign Out", use_container_width=True):
            st.session_state.logged_in = False
            st.session_state.username = None
            st.rerun()
    
    # Your main content here
    st.subheader("Your Educational AI Assistant")
    st.write("""
    Learn smarter with AI.
    • Ask educational questions
    • Get instant explanations
    • Improve your learning experience
    """)
    
else:
    # Show login/register page
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
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
        st.subheader("Welcome! Please sign in")
        
        # Login Form
        with st.form("login_form"):
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            submitted = st.form_submit_button("🔐 Sign In", use_container_width=True)
            
            if submitted:
                # Add your authentication logic here
                # Example:
                if username and password:  # Replace with actual DB check
                    st.session_state.logged_in = True
                    st.session_state.username = username
                    st.rerun()
                else:
                    st.error("Invalid credentials")
        
        # Register link
        st.write("Don't have an account?")
        if st.button("📝 Create Account", use_container_width=True):
            st.switch_page("pages/register.py")