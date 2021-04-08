# ============================= #
# ====== SERVER ==== UDP ====== #
# ============================= #
import socket

IP = "127.0.0.1"
PORT = 8888

def server(ip, port):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((ip, port))
        while True:
            msg, addr = s.recvfrom(1024)
            msg = msg.decode("utf8").upper()
            s.sendto(msg.encode("utf8"), addr)

def main():
    server(IP, PORT)

if __name__ == "__main__":
    main()