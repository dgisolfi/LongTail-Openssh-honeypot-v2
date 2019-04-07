#!/usr/bin/python3

import sys
import socket
import datetime

class Server:
    def __init__(self, port):
        self.sock = None
        self.host = None
        self.port = port
        self.ver = 1.0
        self.setupSocket()

    def setupSocket(self):
        # Get new socket object
        self.sock = socket.socket()
        # Get hostname of the Docker Container
        self.host = socket.gethostname()
        try:
            # Now bind that port to the Socket!!
            self.sock.bind(('', self.port))
        except OSError:
            print('Error Port already in use')
            sys.exit(1)
       

    # Logging to ensure we arent losing any data
    def logger(self, log):
        try:
            file = open('server.log', 'a+')
            file.write(log + '\n')
            file.close()
        except:
            print('Server: Error logging to File!')

    # Handle all incoming client connections
    def handleConnections(self):
        print(f'SocketStream Server v{self.ver}')
        try:
            # Wait for a client to connect to the Server
            print('Server: Listening for Messages...')
            self.sock.listen(5)
            while True:
                print('--------------------')
                conn, addr = self.sock.accept()
                print('Message Received from Client')

                # There should never be a message larger than this...
                msg = conn.recv(10096).decode()
                attack_log = f'[{datetime.datetime.now()}] Client: {addr[1]} Message: {msg}'
                print(attack_log)
                self.logger(attack_log)

                conn.send(f'Message Received'.encode())
                conn.close()
        except KeyboardInterrupt:
            print('Server: Shutting Down')
            sys.exit(1)
        
def main():
    server = Server(5050)
    server.handleConnections()
        

if __name__ == '__main__':
    main()