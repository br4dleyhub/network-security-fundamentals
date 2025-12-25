from datetime import datetime
from collections import defaultdict
import time
import socket
import logging

connection_tracker = defaultdict(list)
TIME_WINDOW = 10  # seconds
MAX_CONNECTIONS = 5

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
        current_time = time.time()

        connection_tracker[ip].append(current_time)

        # Remove old timestamps
        connection_tracker[ip] = [
            t for t in connection_tracker[ip]
            if current_time - t <= TIME_WINDOW
        ]

        logging.info(f"Connection from {ip}:{port}")

        if len(connection_tracker[ip]) > MAX_CONNECTIONS:
            logging.warning(
                f"Suspicious activity detected from {ip} "
                f"({len(connection_tracker[ip])} connections in {TIME_WINDOW}s)"
            )
            print(f"[!] Suspicious activity from {ip}")

        client_socket.close()

if __name__ == "__main__":
    start_server()
