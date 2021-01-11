import tkinter
import socket
import selectors
import threading    

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind(ADDRESS)
# s.listen()

class ThreadedServer(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.address = (self.host, self.port)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients_connected = 0
        self.socket.bind(self.address)

    def listen(self):
        self.socket.listen(5)
        while True: 
            client, address = self.socket.accept()
            self.clients_connected += 1
    
server = ThreadedServer('localhost', 8002)











