import rsa

class Wallet:
    def __init__(self):
        self.private_key, self.public_key = rsa.newkeys(512)

    def sign_transaction(self, message):
        """Sign a transaction using the private key."""
        return rsa.sign(message.encode(), self.private_key, 'SHA-256')

    def verify_signature(self, message, signature, sender_public_key):
        """Verify the transaction signature."""
        try:
            return rsa.verify(message.encode(), signature, sender_public_key) == 'SHA-256'
        except rsa.VerificationError:
            return False

if __name__ == "__main__":
    wallet = Wallet()
    message = "Send 10 coins to Alice"

    signature = wallet.sign_transaction(message)
    print("Signature:", signature)

    is_valid = wallet.verify_signature(message, signature, wallet.public_key)
    print("Signature valid:", is_valid)




from wallet import Wallet
wallet = Wallet()

@app.route('/sign', methods=['POST'])
def sign_transaction():
    data = request.json.get("data")
    signature = wallet.sign_transaction(data)
    return jsonify({"signature": signature.hex()}), 200


git add wallet.py
git commit -m "Added wallet system with digital signatures"
git push origin main

