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
        my_dict = {}
        self.socket.listen(5)
        while True: 
            client, address = self.socket.accept()
            self.clients_connected += 1
            print('Address:', address[1])
            name_of_client = client.recv(1024).decode()
            if('Name:' in name_of_client):
                my_dict[name_of_client[5:]] = address
                print(my_dict[name_of_client[5:]])




server = ThreadedServer('localhost', 8002).listen()











