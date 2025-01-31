from flask import Flask, jsonify, request
import threading
import requests

app = Flask(__name__)
blockchain = []

@app.route('/get_chain', methods=['GET'])
def get_chain():
    response = {'chain': blockchain, 'length': len(blockchain)}
    return jsonify(response), 200

@app.route('/sync_blockchain', methods=['POST'])
def sync_blockchain_data():
    global blockchain
    data = request.get_json()
    blockchain = data.get('chain', [])
    return jsonify({'message': 'Blockchain synchronized'}), 200

def auto_sync():
    while True:
        try:
            response = requests.get('http://192.168.1.10:5000/get_chain')
            global blockchain
            blockchain = response.json().get('chain', blockchain)
        except Exception as e:
            print(f"Error auto-syncing: {e}")

threading.Thread(target=auto_sync, daemon=True).start()

if __name__ == '__main__':
    app.run(host='192.168.1.11', port=5000)