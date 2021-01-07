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
    while True:
        message = conn.recv(1024).decode()
        if message == 'exit the messaging platform': break
        print(message)
        break










