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
        while True:
            try:
                string_sent = client.recv(1024).decode('utf-8')
                message = string_sent[string_sent.find(':') + 1:]
                print(message)
                if not message:
                    break
                c.sendall(bytes(name_client2+':'+ message,'utf-8'))
                
            except:
                pass
            try:
                string_sent = c.recv(1024).decode('utf-8')
                message = string_sent[string_sent.find(':') + 1:]
                print(message)
                if not message:
                    break
                client.sendall(bytes(name_client1+':'+ message,'utf-8'))
            except:
                pass

server = ThreadedServer('localhost', 8002).listen()











