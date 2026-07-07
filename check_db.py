import sqlite3

conn = sqlite3.connect("educhat.db")
cursor = conn.cursor()

# Show all tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print("Tables:", cursor.fetchall())

# Show all users
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

print("\nUsers:")
for row in rows:
    print(row)

conn.close()