from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/whatsapp", methods=["POST"])
def whatsapp():
    incoming_msg = request.values.get("Body", "").lower()
    resp = MessagingResponse()
    msg = resp.message()

    if incoming_msg == "hi" or incoming_msg == "hello":
        msg.body("Hello 👋 I am your WhatsApp bot.")
    elif incoming_msg == "help":
        msg.body("Commands:\nhi\nhello\nhelp")
    else:
        msg.body("Command not recognized")

    return str(resp)

@app.route("/")
def home():
    return "Bot is running"