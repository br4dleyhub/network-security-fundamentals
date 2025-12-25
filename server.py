import socket
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename="logs/connections.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

HOST = "127.0.0.1"
PORT = 9000

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    print(f"[+] Server listening on {HOST}:{PORT}")

    while True:
        client_socket, client_address = server_socket.accept()
        ip, port = client_address

        logging.info(f"Connection from {ip}:{port}")
        print(f"[+] Connection from {ip}:{port}")

        client_socket.close()

if __name__ == "__main__":
    start_server()
