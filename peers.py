import requests

class PeerNetwork:
    def __init__(self):
        self.peers = set()

    def add_peer(self, peer_url):
        """Add a new peer to the network."""
        self.peers.add(peer_url)
        print(f"New peer added: {peer_url}")

    def remove_peer(self, peer_url):
        """Remove a peer from the network."""
        if peer_url in self.peers:
            self.peers.remove(peer_url)
            print(f"Peer removed: {peer_url}")

    def broadcast_new_block(self, block):
        """Send the new block to all peers."""
        for peer in self.peers:
            try:
                response = requests.post(f"{peer}/receive_block", json=block)
                if response.status_code == 200:
                    print(f"Block sent to {peer}")
            except requests.exceptions.RequestException:
                print(f"Failed to send block to {peer}")

if __name__ == "__main__":
    network = PeerNetwork()
    network.add_peer("http://127.0.0.1:5001")
    network.add_peer("http://127.0.0.1:5002")
    print("Current peers:", network.peers)


from peers import PeerNetwork
peer_network = PeerNetwork()

@app.route('/add_peer', methods=['POST'])
def add_peer():
    peer_url = request.json.get("peer_url")
    peer_network.add_peer(peer_url)
    return jsonify({"message": "Peer added", "peers": list(peer_network.peers)}), 201


git add peers.py
git commit -m "Added peer-to-peer networking system"
git push origin main

