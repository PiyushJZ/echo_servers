# ============================= #
# ====== SERVER ==== TCP ====== #
# ============================= #
import socket

IP = "127.0.0.1"
PORT = 8000

def server(ip, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((ip, port))
        s.listen(1)
        while True:
            conn, addr = s.accept()
            print(f"Connected to {addr}")
            data = ""
            response = ""
            with conn:
                request = conn.recv(1024).decode('utf8')
                data += request.upper()
                conn.sendall(data.encode("utf8"))
                conn.close()

def main():
    server(IP, PORT)

if __name__ == "__main__":
    main()