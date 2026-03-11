def handle_command(msg):

    msg = msg.lower()

    if msg.startswith("/news"):
        return "Fetching news..."

    return "Command not recognized"