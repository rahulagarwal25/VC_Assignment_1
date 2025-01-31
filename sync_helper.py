import requests
import threading


NODE_ADDRESSES = [
    'http://192.168.1.11:5000',  # VM2
    'http://192.168.1.12:5000'   # VM3
]

def sync_blockchain(blockchain_data):
    def sync_task():
        for node in NODE_ADDRESSES:
            try:
                requests.post(f"{node}/sync_blockchain", json={'chain': blockchain_data})
            except Exception as e:
                print(f"Error syncing with {node}: {e}")
    threading.Thread(target=sync_task).start()