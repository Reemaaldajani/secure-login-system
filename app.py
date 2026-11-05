from flask import Flask, request
import sqlite3
from werkzeug.security import check_password_hash
import datetime

app = Flask(__name__)

failed_attempts = {}


def get_db():
    return sqlite3.connect("users.db")


def is_locked(username):
    attempts = failed_attempts.get(username, [])
    attempts = [
        t for t in attempts
        if (datetime.datetime.now() - t).total_seconds() < 300
    ]
    failed_attempts[username] = attempts
    return len(attempts) >= 3


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if not username or not password:
            return "Invalid input"

        if is_locked(username):
            return """
            <h3 style="color:red; text-align:center;">
                 Account Locked<br>
                Try again after 5 minutes
            </h3>
            """

        db = get_db()
        cursor = db.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE username = ?",
            (username,)
        )
        user = cursor.fetchone()
        db.close()

        if user and check_password_hash(user[1], password):
            failed_attempts[username] = []

            return f"""
            <h2 style="text-align:center;">
                 Welcome {user[0]}
            </h2>
            <p style="text-align:center;">
                Login successful 
            </p>
            """
        else:
            failed_attempts.setdefault(username, []).append(
                datetime.datetime.now()
            )

            return """
            <h3 style="color:red; text-align:center;">
                 Login Failed
            </h3>
            <a href="/">Try Again</a>
            """

    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Secure Login</title>
        <style>
            body {
                margin: 0;
                height: 100vh;
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #667eea, #764ba2);
                display: flex;
                justify-content: center;
                align-items: center;
            }

            .login-box {
                background: white;
                width: 350px;
                padding: 35px;
                border-radius: 15px;
                box-shadow: 0 10px 25px rgba(0,0,0,0.2);
                text-align: center;
            }

            h2 {
                margin-bottom: 10px;
                color: #333;
            }

            p {
                color: #666;
                font-size: 14px;
                margin-bottom: 25px;
            }

            input {
                width: 100%;
                padding: 12px;
                margin: 10px 0;
                border: 1px solid #ccc;
                border-radius: 8px;
                font-size: 14px;
                box-sizing: border-box;
            }

            button {
                width: 100%;
                padding: 12px;
                margin-top: 15px;
                background: #667eea;
                color: white;
                border: none;
                border-radius: 8px;
                font-size: 16px;
                cursor: pointer;
            }

            button:hover {
                background: #5563c1;
            }

            .footer {
                margin-top: 20px;
                font-size: 12px;
                color: #999;
            }
        </style>
    </head>

    <body>
        <div class="login-box">
            <h2>Secure Login System</h2>
            <p>Protected against SQL Injection attacks</p>

            <form method="post">
                <input name="username"
                       placeholder="Username" required>

                <input name="password"
                       type="password"
                       placeholder="Password" required>

                <button type="submit">Login</button>
            </form>

            <div class="footer">
                CS471 Computer Security Project
            </div>
        </div>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(debug=False)