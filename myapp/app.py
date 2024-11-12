from flask import Flask
from flask_socketio import SocketIO, send

# Initialize Flask app and SocketIO
app = Flask(__name__)
socketio = SocketIO(app)

# Serve a simple message to confirm server is running
@app.route('/')
def index():
    return "WebSocket Server is running!"

@app.route('/test')
def testmethod():
    return "WebSocket Server is running!"
    
# WebSocket event listener for handling messages
@socketio.on('message')
def handle_message(message):
    print('Received message:', message)
    send(f"Echo: {message}", broadcast=True)

# Start the Flask app with SocketIO
if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0", port=5000)
