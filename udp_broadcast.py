# ============================= #
# ====== SERVER ==== UDP ====== #
# ============================= #

import socket
import time

IP = "127.0.0.1"
PORT = 2020
roll_numbers = {"127.0.0.1": "2019501034"}

def broadcast_roll(ip, port):
    message = "2019501034".encode("utf8")
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((ip, port))
    for address in roll_numbers:
        s.sendto(message, (address, 2020))
    try:
        s.settimeout(5)
        while True:
            msg, address = s.recvfrom(128)
            if msg.decode("utf8") in roll_numbers.values():
                roll_numbers.pop(address[0])
    except:
        pass
    finally:
        s.close()

def main():
    broadcast_roll(IP, PORT)
    print("================Absentees==============")
    for address in roll_numbers:
            print(roll_numbers[address])

if __name__ == "__main__":
    main()