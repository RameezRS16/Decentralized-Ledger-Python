from flask import Flask, jsonify, request
from blockchain import Blockchain
from utils import is_valid_transaction

app = Flask(__name__)

# Initialize blockchain
blockchain = Blockchain()

@app.route('/chain', methods=['GET'])
def get_chain():
    chain_data = []
    for block in blockchain.chain:
        chain_data.append({
            "index": block.index,
            "timestamp": block.timestamp,
            "data": block.data,
            "previous_hash": block.previous_hash,
            "nonce": block.nonce,
            "hash": block.hash
        })
    return jsonify({"length": len(chain_data), "chain": chain_data}), 200

@app.route('/mine', methods=['POST'])
def mine_block():
    data = request.json.get("data")
    if not is_valid_transaction(data):
        return jsonify({"error": "Invalid transaction data"}), 400

    blockchain.add_block(data)
    latest_block = blockchain.get_latest_block()

    return jsonify({
        "message": "Block successfully mined!",
        "block": {
            "index": latest_block.index,
            "timestamp": latest_block.timestamp,
            "data": latest_block.data,
            "previous_hash": latest_block.previous_hash,
            "nonce": latest_block.nonce,
            "hash": latest_block.hash
        }
    }), 201

@app.route('/transaction', methods=['POST'])
def add_transaction():
    data = request.json.get("data")
    if not is_valid_transaction(data):
        return jsonify({"error": "Transaction data is required"}), 400
    
    blockchain.add_block(data)
    return jsonify({"message": "Transaction added to blockchain", "data": data}), 201

if __name__ == '__main__':
    app.run(debug=True, port=5000)
