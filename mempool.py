class Mempool:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        """Add a new transaction to the mempool."""
        self.transactions.append(transaction)
        print(f"Transaction added to mempool: {transaction}")

    def get_pending_transactions(self):
        """Return all pending transactions."""
        return self.transactions

    def clear_mempool(self):
        """Clear mempool after mining a new block."""
        self.transactions = []
        print("Mempool cleared after block mining.")

from mempool import Mempool
mempool = Mempool()

@app.route('/pending_transactions', methods=['GET'])
def get_pending_transactions():
    return jsonify({"pending_transactions": mempool.get_pending_transactions()}), 200

@app.route('/add_transaction', methods=['POST'])
def add_transaction():
    data = request.json
    mempool.add_transaction(data)
    return jsonify({"message": "Transaction added to mempool"}), 201


git add mempool.py
git commit -m "Added mempool for pending transactions"
git push origin main


