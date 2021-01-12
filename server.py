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
            message = client.recv(1024).decode('utf-8')
            print(message)
            if('Name:' in message):
                my_dict[message[5:]] = client
            elif(':' in message):
                print('RAN')
                name = message[:message.find(':')]
                for index, clr in my_dict.items:
                    if(index != name):
                        clr.sendall(bytes(message[:],'utf-8'))

server = ThreadedServer('localhost', 8002).listen()











