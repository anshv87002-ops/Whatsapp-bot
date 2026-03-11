from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from command_router import handle_command

app = Flask(__name__)

@app.route("/whatsapp", methods=["POST"])
def whatsapp():
    incoming_msg = request.form.get("Body")

    reply = handle_command(incoming_msg)

    resp = MessagingResponse()
    resp.message(reply)

    return str(resp)


@app.route("/")
def home():
    return "WhatsApp Bot Running"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)