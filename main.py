from flask import session
from flask_socketio import SocketIO
from app import create_app
from app.database import DataBase
import config

# SETUP
app = create_app() # From app/init.py
socketio = SocketIO(app)  # For user communication

# MESSAGE ENCRYPTION AND DECRYPTION
def encrypt(key, msg):
    enc = []
    for i, c in enumerate(msg):
        key_c = ord(key[i % len(key)])
        msg_c = ord(c)
        enc.append(chr((msg_c + key_c) % 127))
    return ''.join(enc)


# COMMUNICATION FUNCTIONS
@socketio.on('event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    """
    handles saving messages once received from web server
    and sending message to other clients
    :param json: json
    :param methods: POST GET
    :return: None
    """
    data = dict(json)
    if "name" in data:
        db = DataBase()
        # data['name'] = encrypt(config.Config.SECRET_KEY, data['name'])
        db.save_message(data["name"], encrypt(config.Config.SECRET_KEY, data["message"]))

    socketio.emit('message response', json)


if __name__ == "__main__":  # Starting the web server
    socketio.run(app, debug=True, host=str(config.Config.SERVER))
