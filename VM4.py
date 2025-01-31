from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

NODE_URLS = {
    'mine': 'http://192.168.1.10:5000/mine_block',
    'chain': 'http://192.168.1.11:5000/get_chain',
    'block': 'http://192.168.1.12:5000/get_block'
}

def fetch_data(url, params=None):
    """Helper function to make GET requests with error handling."""
    try:
        response = requests.get(url, params=params, timeout=5) 
        response.raise_for_status()  
        return response.json(), response.status_code
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}, 500

@app.route('/mine_block', methods=['GET'])
def mine_block():
    data, status = fetch_data(NODE_URLS['mine'])
    return jsonify(data), status

@app.route('/get_chain', methods=['GET'])
def get_chain():
    data, status = fetch_data(NODE_URLS['chain'])
    return jsonify(data), status

@app.route('/get_block', methods=['GET'])
def get_block():
    block_index = request.args.get('index')

    if block_index is None:  
        data, status = fetch_data(NODE_URLS['chain']) 
        if "chain" in data:
            return jsonify({"blocks": data["chain"]}), status
        return jsonify(data), status

    try:
        index = int(block_index)  
    except ValueError:
        return jsonify({"error": "'index' must be an integer"}), 400

    data, status = fetch_data(NODE_URLS['block'], params={"index": index})
    return jsonify(data), status

if __name__ == '__main__':
    app.run(host='192.168.1.13', port=5000)
