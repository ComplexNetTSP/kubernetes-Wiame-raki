from flask import Flask
import socket
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"""
    <html>
    <head><title>Website</title></head>
    <body>
        <h1>Challenge 1</h1>
        <p>Your Name: <strong>Wiame RAKI</strong></p>
        <p>Project Name: <strong>My Flask App</strong></p>
        <p>Website Version: <strong>V1</strong></p>

        <p>Server IP Address: <strong>{ip_address}</strong></p>
        <p>Current Date and Time: <strong>{current_date}</strong></p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
