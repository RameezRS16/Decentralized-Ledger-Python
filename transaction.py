import json
import time
from wallet import Wallet

class Transaction:
    def __init__(self, sender_public_key, recipient_public_key, amount, signature):
        self.sender_public_key = sender_public_key
        self.recipient_public_key = recipient_public_key
        self.amount = amount
        self.signature = signature
        self.timestamp = time.time()

    def to_dict(self):
        """Convert transaction data to dictionary format."""
        return {
            "sender": self.sender_public_key,
            "recipient": self.recipient_public_key,
            "amount": self.amount,
            "signature": self.signature.hex(),
            "timestamp": self.timestamp
        }

    def is_valid(self):
        """Verify if the transaction signature is valid."""
        wallet = Wallet()
        return wallet.verify_signature(
            f"{self.sender_public_key}{self.recipient_public_key}{self.amount}{self.timestamp}",
            bytes.fromhex(self.signature),
            self.sender_public_key
        )

# Example usage
if __name__ == "__main__":
    wallet = Wallet()
    
    sender_key = wallet.public_key
    recipient_key = wallet.public_key  # Dummy recipient for testing
    amount = 50

    message = f"{sender_key}{recipient_key}{amount}{time.time()}"
    signature = wallet.sign_transaction(message)

    transaction = Transaction(sender_key, recipient_key, amount, signature.hex())
    print("Transaction Valid:", transaction.is_valid())




from transaction import Transaction

@app.route('/new_transaction', methods=['POST'])
def new_transaction():
    data = request.json
    transaction = Transaction(
        sender_public_key=data["sender"],
        recipient_public_key=data["recipient"],
        amount=data["amount"],
        signature=data["signature"]
    )

    if not transaction.is_valid():
        return jsonify({"error": "Invalid transaction signature"}), 400

    blockchain.add_block(transaction.to_dict())
    return jsonify({"message": "Transaction added to blockchain"}), 201



git add transaction.py
git commit -m "Added transaction structure with digital signatures"
git push origin main



