# import sqlite3
# import streamlit as st

# # Connect to database
# conn = sqlite3.connect("database/educhat.db")
# cursor = conn.cursor()

# # Create table if it doesn't exist
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS users (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     username TEXT UNIQUE,
#     email TEXT UNIQUE,
#     password TEXT
# )
# """)
# conn.commit()

# st.title("Register")

# with st.form("register"):
#     username = st.text_input("Username")
#     email = st.text_input("Email")
#     password = st.text_input("Password", type="password")
#     confirm = st.text_input("Confirm Password", type="password")

#     submit = st.form_submit_button("Create Account")

# if submit:

#     if password != confirm:
#         st.error("Passwords do not match.")

#     else:
#         try:
#             cursor.execute(
#                 """
#                 INSERT INTO users(username, email, password)
#                 VALUES (?, ?, ?)
#                 """,
#                 (username, email, password)
#             )

#             conn.commit()
#             st.success("Account created successfully!")

#         except sqlite3.IntegrityError:
#             st.error("Username or email already exists.")

# st.subheader("Registered Users")

# cursor.execute("SELECT * FROM users")
# rows = cursor.fetchall()

# st.write(rows)

import streamlit as st
import sqlite3
import hashlib

st.set_page_config(
    page_title="Register - EduChat",
    page_icon="assets/eve.png",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.title("📝 Create Account")

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def create_user(username, email, password):
    conn = sqlite3.connect('educhat.db')
    cursor = conn.cursor()
    
    hashed_pw = hash_password(password)
    
    try:
        cursor.execute(
            "INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
            (username, email, hashed_pw)
        )
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

# Registration Form
with st.form("register_form"):
    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")
    
    submitted = st.form_submit_button("Create Account", use_container_width=True)
    
    if submitted:
        if password != confirm_password:
            st.error("Passwords don't match!")
        elif not username or not email or not password:
            st.error("Please fill all fields!")
        else:
            if create_user(username, email, password):
                st.success("Account created successfully! 🎉")
                st.info("Please go back to login page")
            else:
                st.error("Username or email already exists!")

# BUTTON OUTSIDE THE FORM - This won't cause an error
st.write("Already have an account?")
if st.button("🔐 Sign In", use_container_width=True):
    st.switch_page("streamlit_app.py")