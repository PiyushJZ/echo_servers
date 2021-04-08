import socket

def tcp_client(ip, port, message):
    recv_msg = ""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP) as s:
        s.connect((ip, port))
        s.sendall(message)
        while True:
            msg = s.recv(1024).decode("utf8")
            if len(msg) <= 0:
                break
            recv_msg += msg
    print(recv_msg)

def udp_client(ip, port, message):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP) as s:
        s.settimeout(1)
        s.sendto(message, (ip, port))
        data, server = s.recvfrom(1024)
        print(data.decode("utf8"))

def main():
    IP = "127.0.0.1"
    message = input("Enter Message\n").encode("utf8")
    # tcp_client(IP, 8000, message)
    udp_client(IP, 8888, message)

if __name__ == "__main__":
    main()