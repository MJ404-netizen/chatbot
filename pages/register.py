import sqlite3
import streamlit as st

# Connect to database
conn = sqlite3.connect("database/educhat.db")
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    email TEXT UNIQUE,
    password TEXT
)
""")
conn.commit()

st.title("Register")

with st.form("register"):
    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    confirm = st.text_input("Confirm Password", type="password")

    submit = st.form_submit_button("Create Account")

if submit:

    if password != confirm:
        st.error("Passwords do not match.")

    else:
        try:
            cursor.execute(
                """
                INSERT INTO users(username, email, password)
                VALUES (?, ?, ?)
                """,
                (username, email, password)
            )

            conn.commit()
            st.success("Account created successfully!")

        except sqlite3.IntegrityError:
            st.error("Username or email already exists.")

st.subheader("Registered Users")

cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

st.write(rows)