from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/hi', methods=['POST'])
def hello():
    return jsonify({'message': 'Hello from Server 2'})

@app.route('/kill', methods=['GET'])
def kill():
    print("Server 2 Down Initiated")
    os.kill(os.getpid(), signal.SIGINT)
    #return may not execute
    return "Server 2 killed"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001)