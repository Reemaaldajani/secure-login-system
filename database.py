import sqlite3
from werkzeug.security import generate_password_hash
from getpass import getpass

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    role TEXT NOT NULL
)
""")

conn.commit()

if __name__ == "__main__":
    username = input("Enter username: ")
    password = getpass("Enter password: ")
    role = input("Enter role (admin/user): ").lower()

    if role not in ("admin", "user"):
        print("Invalid role")

    else:
        try:
            cursor.execute(
                "INSERT INTO users VALUES (?, ?, ?)",
                (username, generate_password_hash(password), role)
            )
            conn.commit()
            print("User created successfully!")

        except sqlite3.IntegrityError:
            print("Username already exists!")

    conn.close()