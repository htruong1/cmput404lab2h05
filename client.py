#!/usr/bin/env python3

import socket

HOST = "www.google.com"
PORT = 80 #80 specifies the main HTTP port
BUFFER_SIZE = 1024

payload = "GET / HTTP/1.0\r\nHost: {}\r\n\r\n".format(HOST)

#Q1 sock_stream
#put sockets in a try catch finally
def get_request(addr):
    (family, socktype, proto, canonname, sockaddr) = addr
    try:
        s = socket.socket(family, socktype, proto)
        s.connect(sockaddr) #now have to request something, want the home page
        s.sendall(payload.encode()) #cant send info to sockets as string, need to change ot bytes
        s.shutdown(socket.SHUT_WR)

        full_data = b""
        while True:
            data = s.recv(BUFFER_SIZE)
            if not data: break
            full_data += data

        print(full_data)

    except Exception as e:
        print(e)
    finally:
        s.close()

def main():
    addr_info = socket.getaddrinfo(HOST, PORT)
    for addr in addr_info:
        (family, socktype, proto, canonname, sockaddr) = addr
        if(family == socket.AF_INET and socktype == 
            socket.SOCK_STREAM):
                print(addr)
                get_request(addr)
    pass

if __name__ == "__main__":
    main()
