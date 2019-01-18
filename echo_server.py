#!/usr/bin/env python3

import socket
import time

HOST = "" #any requests coming in
PORT = 8001
BUFFER_SIZE = 1024


def main():
    with socket.socket(socket.AF_INET, 
    socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen(2) #listen 1 connection at a time
        while True:
            conn,address = s.accept()
            print("Connected by", address)


            full_data = b""
            while True:
                data = conn.recv(BUFFER_SIZE)
                print(data, "oooo")
                if not data: break
                full_data += data
                conn.send(data)

            time.sleep(0.5)
            conn.sendall(full_data)
            conn.close()

if __name__ == "__main__":
    main()