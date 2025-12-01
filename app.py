from flask import Flask, render_template, request, jsonify
from chatbot import get_bot_response

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
    app.run(debug=True)
