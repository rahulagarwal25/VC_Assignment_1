from flask import Flask, jsonify, request
import requests
import threading
import time

app = Flask(__name__)
blockchain = []

@app.route('/get_block', methods=['GET'])
def get_block():
    index = request.args.get('index')

    if index is None:  
        return jsonify({'blocks': blockchain}), 200

    try:
        index = int(index)
    except ValueError:
        return jsonify({'error': "'index' must be an integer"}), 400

    if index <= 0 or index > len(blockchain):
        return jsonify({'error': 'Invalid block index'}), 400

    return jsonify({'block': blockchain[index - 1]}), 200

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
            print("Blockchain auto-synced successfully!")
        except Exception as e:
            print(f"Error auto-syncing: {e}")
        
        time.sleep(10)  
threading.Thread(target=auto_sync, daemon=True).start()

if __name__ == '__main__':
    app.run(host='192.168.1.12', port=5000)
