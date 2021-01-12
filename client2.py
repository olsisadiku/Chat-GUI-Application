import socket 
import selectors
import tkinter as tk


HOST = 'localhost'
PORT = 8002

ADDRESS = (HOST,PORT)

FORMAT = 'utf-8'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(ADDRESS)
s.setblocking(False)

my_name = input('What is your name? ')
s.sendall(str.encode('Name:'+my_name))


def person2_window():
    import tkinter as tk

    root = tk.Tk()
    root.title('Sadiku Messaging')
    root.iconbitmap('thunderbird1_ico.ico')

    def send():
        send = my_name + ': ' + e.get()
        s.sendall(str.encode(send))

    while True:
        try:
            value = s.recv(1024).decode('utf-8')
        except BlockingIOError:
            break
        txt.insert(tk.END, '\n' + value)

    txt = tk.Text(root)
    txt.grid(row = 0, column = 0, columnspan = 2)
    e = tk.Entry(root, width = 100)
    send = tk.Button(root, text = 'Send Message', command = send).grid(row=1, column =1)
    e.grid(row = 1, column = 0)

    root.resizable(False, False) 
    root.mainloop()

person2_window()