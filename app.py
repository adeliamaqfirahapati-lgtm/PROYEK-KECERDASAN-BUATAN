from flask import Flask, render_template, request, jsonify
from chatbot import get_bot_response
import os

app = Flask(_name_)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "")
    bot_reply = get_bot_response(user_message)
    return jsonify({"reply": bot_reply})

if _name_ == "_main_":
    port = int(os.environ.get("PORT", 5000)) 
    app.run(host="0.0.0.0", port=port)