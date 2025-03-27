import hashlib
import json

DIFFICULTY = 4  # Number of leading zeros required in hash

def proof_of_work(block):
    block.nonce = 0
    computed_hash = calculate_hash(block)
    
    while not computed_hash.startswith('0' * DIFFICULTY):
        block.nonce += 1
        computed_hash = calculate_hash(block)
    
    return computed_hash

def calculate_hash(block):
    block_string = json.dumps({
        "index": block.index,
        "timestamp": block.timestamp,
        "data": block.data,
        "previous_hash": block.previous_hash,
        "nonce": block.nonce
    }, sort_keys=True)
    
    return hashlib.sha256(block_string.encode()).hexdigest()

def is_valid_transaction(data):
    return isinstance(data, str) and len(data) > 0
