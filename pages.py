import tkinter as tk

root = tk.Tk()
root.title('Sadiku Messaging')
root.iconbitmap('thunderbird1_ico.ico')

def send():
    send = 'You=> ' + e.get()
    txt.insert(tk.END, '\n' + send)


txt = tk.Text(root)
txt.grid(row = 0, column = 0, columnspan = 2)
e = tk.Entry(root, width = 100)
send = tk.Button(root, text = 'Send Message', command = send).grid(row=1, column =1)
e.grid(row = 1, column = 0)







root.resizable(False, False) 
root.mainloop()





