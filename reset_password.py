import sqlite3
from werkzeug.security import generate_password_hash

password = input("Enter new admin password: ")

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute(
    "UPDATE users SET password = ? WHERE username = ?",
    (generate_password_hash(password), "admin")
)

conn.commit()
print("Password updated successfully!")
conn.close()