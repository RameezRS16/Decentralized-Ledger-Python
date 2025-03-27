import logging

# Logging Configuration
logging.basicConfig(
    filename="blockchain.log",  # Logs will be saved in this file
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

def log_event(event_type, message):
    """
    Logs an event with a specific type and message.
    
    :param event_type: INFO, WARNING, ERROR
    :param message: The event message
    """
    if event_type == "INFO":
        logging.info(message)
    elif event_type == "WARNING":
        logging.warning(message)
    elif event_type == "ERROR":
        logging.error(message)
    else:
        logging.debug(message)


from logger import log_event

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        log_event("INFO", "Blockchain initialized with Genesis Block.")

    def add_block(self, data):
        latest_block = self.get_latest_block()
        new_block = Block(len(self.chain), time.time(), data, latest_block.hash)
        self.chain.append(new_block)
        log_event("INFO", f"New block added: Index {new_block.index}, Hash {new_block.hash}")


from logger import log_event

@app.route('/mine', methods=['POST'])
def mine_block():
    data = request.json.get("data")
    if not is_valid_transaction(data):
        log_event("WARNING", "Invalid transaction data received.")
        return jsonify({"error": "Invalid transaction data"}), 400

    blockchain.add_block(data)
    latest_block = blockchain.get_latest_block()

    log_event("INFO", f"Block {latest_block.index} mined successfully.")
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


