from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import signal
app = Flask(__name__)

CORS(app) 



@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy server2'}), 200

@app.route('/hi', methods=['POST'])
def hello():
    return jsonify({'message': 'Hello from Server 2'})

@app.route('/kill', methods=['GET'])
def kill():
    try:
        os.kill(os.getpid(), signal.SIGINT)
    except SystemExit:
        return "Process terminated"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001)