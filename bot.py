from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from command_router import handle_comman

app = Flask(__name__

@app.route("/whatsapp", methods=["POST"])
def whatsapp()
    body = request.form.get("Body", "")

    reply = handle_command(body)

    resp = MessagingResponse()
    resp.message(reply)

    return str(resp)

@app.route("/")
def index():
    return "Bot is running"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)