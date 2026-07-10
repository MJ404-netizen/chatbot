import sqlite3
import hashlib

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

def authenticate_user(username, password):
    conn = sqlite3.connect('educhat.db')
    cursor = conn.cursor()
    
    hashed_pw = hash_password(password)
    
    cursor.execute(
        "SELECT * FROM users WHERE username = ? AND password = ?",
        (username, hashed_pw)
    )
    user = cursor.fetchone()
    conn.close()
    
    return user is not None