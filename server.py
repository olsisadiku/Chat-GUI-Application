import tkinter
import socket
import selectors
from _thread import *
import threading  

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind(ADDRESS)
# s.listen()
    
print_lock = threading.Lock() 

class ThreadedServer(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.address = (self.host, self.port)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients_connected = 0
        self.socket.bind(self.address)
        self.socket.setblocking(False)
        
    def threaded(self, client):
        while True:
            data = client.recv(1024).decode()
            if not data:
                print('BYEEE')
                print_lock.release()

                

    def listen(self):
        my_dict = {}
        self.socket.listen(5)
        clients = []
        # Client 1 code to take in their info
        while True:
            try:
                c, add = self.socket.accept()
            except:
                continue
            while True: 
                try:    
                    string_sent = c.recv(1024).decode('utf-8')
                    name_client1 = string_sent[string_sent.find(':') + 1:]
                    break
                except:
                    continue
            break
        #Client 2 code to take in their name info    
        while True:
            try:
                client, address = self.socket.accept()
            except:
                continue
            while True:
                try:  
                    string_sent = client.recv(1024).decode('utf-8')
                    name_client2 = string_sent[string_sent.find(':') + 1:]
                    break
                except:
                    continue
            break
        print('Name of client 1',  name_client1)
        print('Name of client 2', name_client2)
        
        
        
        # while True: 
        #     if(self.clients_connected != 2):
        #         client, address = self.socket.accept()
        #         self.clients_connected += 1
        #         clients.append(client)
        #     message = client.recv(1024).decode() 
        #     if('Name:' in message):
        #         my_dict[message[5:]] = client
        #     elif(':' in message):
        #         print('RAN')
        #         name = message[:message.find(':')]
        #         for index, clr in my_dict.items():
        #             if(index != name):
        #                 clr.sendall(bytes(message[:],'utf-8'))

server = ThreadedServer('localhost', 8002).listen()











