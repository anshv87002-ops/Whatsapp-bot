from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from command_router import handle_command

app = Flask(__name__)

@app.route("/whatsapp", methods=["POST"])
def whatsapp():
    msg = request.form.get("Body")

    reply = handle_command(msg)

    resp = MessagingResponse()
    resp.message(reply)

    return str(resp)

if __name__ 