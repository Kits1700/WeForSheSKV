#!/bin/env python
from app import create_app, socketio
from flask_ngrok import run_with_ngrok
app = create_app(debug=True)


if __name__ == '__main__':
    socketio.run(app)
