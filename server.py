import tkinter
import socket
import selectors


HOST = 'localhost'
PORT = 8002

ADDRESS = (HOST,PORT)

sel = selectors.DefaultSelector()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(ADDRESS)
s.listen()

while True: 
    
    conn, addr = s.accept()
    print('listening on', PORT)
    message = conn.recv(1024).decode()
    name = message[0:message.index(':')]
    if(name == 'Olsi'):
        num_client = '1'; 
        s.sendall()
    print(name)
    if message == 'e': break










