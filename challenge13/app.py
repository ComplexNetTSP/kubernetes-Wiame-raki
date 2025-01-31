from flask import Flask, request
import socket
from datetime import datetime
from pymongo import MongoClient
import os 
from flask import jsonify

app = Flask(__name__)

# Retrieve environment variables
mongo_uri = os.getenv("MONGO_URI")

# MongoDB connection
client = MongoClient(mongo_uri)
db = client.flask_app
collection = db.requests

@app.route("/health-check")
def health():
    return jsonify({"status": "healthy", "message": "Service is running smoothly"})

@app.route("/")
def home():
    # Server details
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Client details
    client_ip = request.remote_addr

    # Record the request in MongoDB
    record = {"client_ip": client_ip, "access_time": current_date}
    collection.insert_one(record)

    # Retrieve the last 10 records
    last_records = list(collection.find().sort("_id", -1).limit(10))

    # Format records for display
    records_html = "<ul>"
    for record in last_records:
        records_html += f"<li>{record['access_time']} - {record['client_ip']}</li>"
    records_html += "</ul>"

    return f"""
    <html>
    <head><title>HA with k8s</title></head>
    <body>
        <h1>Challenge 13</h1>
        <p>Your Name: <strong>Wiame RAKI</strong></p>
        <p>Project Name: <strong>THE APP</strong></p>
        <p>Website Version: <strong>V13</strong></p>

        <p>Server IP Address: <strong>{ip_address}</strong></p>
        <p>Server Hostname: <strong>{hostname}</strong></p>
        <p>Current Date and Time: <strong>{current_date}</strong></p>
        
        <h2>Last 10 Requests</h2>
        {records_html}
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
