import requests

class Consensus:
    def __init__(self, blockchain, peer_network):
        self.blockchain = blockchain
        self.peer_network = peer_network

    def fetch_chain_from_peers(self):
        """Get the blockchain from all peers and return the longest valid chain."""
        longest_chain = None
        max_length = len(self.blockchain.chain)

        for peer in self.peer_network.peers:
            try:
                response = requests.get(f"{peer}/chain")
                peer_chain = response.json()["chain"]
                peer_length = response.json()["length"]

                if peer_length > max_length and self.is_valid_chain(peer_chain):
                    longest_chain = peer_chain
                    max_length = peer_length

            except requests.exceptions.RequestException:
                print(f"Failed to fetch chain from {peer}")

        return longest_chain

    def is_valid_chain(self, chain):
        """Validate an entire blockchain received from a peer."""
        for i in range(1, len(chain)):
            if chain[i]["previous_hash"] != chain[i - 1]["hash"]:
                return False
        return True

    def resolve_conflicts(self):
        """Resolve conflicts by adopting the longest valid chain."""
        new_chain = self.fetch_chain_from_peers()
        if new_chain:
            self.blockchain.chain = new_chain
            print("Blockchain replaced with a longer valid chain from the network.")
            return True
        return False

from consensus import Consensus
consensus = Consensus(blockchain, peer_network)

@app.route('/resolve_conflicts', methods=['GET'])
def resolve_conflicts():
    replaced = consensus.resolve_conflicts()
    return jsonify({"message": "Blockchain replaced" if replaced else "Current chain is authoritative"}), 200

git add consensus.py
git commit -m "Added consensus mechanism with longest chain rule"
git push origin main


