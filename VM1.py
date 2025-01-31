from flask import Flask, jsonify
import datetime
import hashlib
from sync_helper import sync_blockchain

app = Flask(__name__)

blockchain = []

def create_block(proof, previous_hash):
    block = {
        'index': len(blockchain) + 1,
        'timestamp': str(datetime.datetime.now()),
        'proof': proof,
        'previous_hash': previous_hash
    }
    blockchain.append(block)
    sync_blockchain(blockchain)
    return block

def get_previous_block():
    return blockchain[-1]

def proof_of_work(previous_proof):
    new_proof = 1
    check_proof = False
    while not check_proof:
        hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
        if hash_operation[:4] == '0000':
            check_proof = True
        else:
            new_proof += 1
    return new_proof

def hash(block):
    encoded_block = str(block).encode()
    return hashlib.sha256(encoded_block).hexdigest()

@app.route('/mine_block', methods=['GET'])
def mine_block():
    previous_block = get_previous_block() if blockchain else {'proof': 1, 'previous_hash': '0'}
    previous_proof = previous_block['proof']
    proof = proof_of_work(previous_proof)
    previous_hash = hash(previous_block)
    block = create_block(proof, previous_hash)
    response = {'message': 'Block mined successfully', 'block': block}
    return jsonify(response), 200



@app.route('/get_chain', methods=['GET'])
def get_chain():
    response = {
        'chain': blockchain,
        'length': len(blockchain)
    }
    return jsonify(response), 200

if __name__ == '__main__':
    if not blockchain:
        create_block(proof=1, previous_hash='0')
    app.run(host='192.168.1.10', port=5000)