import socket
import time

HOST = "127.0.0.1"
PORT = 9000

def simulate_bruteforce():
    for i in range(10):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((HOST, PORT))
            sock.close()
            time.sleep(0.5)
        except Exception as e:
            print("Connection failed:", e)

if __name__ == "__main__":
    simulate_bruteforce()
