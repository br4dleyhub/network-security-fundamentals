import socket

HOST = "127.0.0.1"
PORT = 9000

def connect_to_server():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))
    print("[+] Connected to server")
    client_socket.close()

if __name__ == "__main__":
    connect_to_server()
