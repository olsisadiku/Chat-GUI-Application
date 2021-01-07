import socket 
import selectors
import tkinter as tk


HOST = 'localhost'
PORT = 8002

ADDRESS = (HOST,PORT)

FORMAT = 'utf-8'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(ADDRESS)

s.sendall(b'whats poppin brand new whip just hopped in')

s.close()







