from flask import Flask, request, send_file
from datetime import datetime

app = Flask(__name__)

@app.route("/pixel")
def pixel():
    email = request.args.get("email", "desconhecido")
    with open("log.txt", "a") as f:
        f.write(f"{datetime.now()} - {email}\n")
    return send_file("pixel.png", mimetype='image/png')
