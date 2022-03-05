from ctypes import resize
import socket
from threading import Thread
from tkinter import *

# nickname = input("Choose your nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = '127.0.0.1'
port = 8000

client.connect((ip_address, port))

print("Connected with the server...")

class GUI:
    def __init__(self):
        self.Window = Tk()
        self.Window.withdraw()

        self.login = Toplevel()
        self.login.title("Login")

        self.login.resizable(width=False, height=False)
        self.login.configure(width=400, height=300)
        
        self.pls = Label(self.login,
					text = "Please login to continue",
					justify = CENTER,
					font = "Helvetica 14 bold")
        self.pls.place( relheight = 0.15,
                        relx = 0.2,
                        rely = 0.07)

        self.labelName = Label(self.login,
							text = "Name: ",
							font = "Helvetica 12")
        self.labelName.place(   relheight = 0.2,
							    relx = 0.1,
							    rely = 0.2)

        self.entryName = Entry(self.login,
							font = "Helvetica 14")
        self.entryName.place(relwidth = 0.4,
							relheight = 0.12,
							relx = 0.35,
							rely = 0.2)
        self.entryName.focus()

        self.go = Button(self.login,
						text = "CONTINUE",
						font = "Helvetica 14 bold",
						command = lambda: self.goAhead(self.entryName.get()))
        self.go.place(  relx = 0.4,
					    rely = 0.55)
        
        self.Window.mainloop()

    def goAhead(self, name):
        self.login.destroy()
        self.layout(name)
        rcv = Thread(target=self.receive)
        rcv.start()

    def layout(self,name):
        self.name=name
        self.Window.deiconify()
        self.Window.title("chat room")
        self.Window.resizable(width=False, height=False)
        self.Window.configure(width=470,height=550,bg="#17202a")
        self.labelhead=Label(self.Window, bg="#17202a",fg="#eaecee", text=self.name, font="Helvetica 13 bold",pady=5)
        self.labelhead.place(relwidth=1)
        self.line=Label(self.Window, width=450, bg="#abb2b9")
        self.line.place(relwidth=1, rely=0.07,relheight=0.012)
        self.textscreen=Text(self.Window, width=20, height=2, bg="#17202a",fg="#eaecee", font="Helvetica 14", padx=5,pady=5)
        self.textscreen.place(relheight=0.745, relwidth=1,rely=0.08)
        self.labelbottom=Label(self.Window,bg="#abb2b9")
        self.labelbottom.place(relwidth=1, rely=0.825)
        self.entrymsg=Entry(self.labelbottom,bg="#2c3e50",fg="#eaecee", font="Helvetica 13")
        self.entrymsg.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
        self.entrymsg.focus()

    def receive(self):
        while True:
            try:
                message = client.recv(2048).decode('utf-8')
                if message == 'NICKNAME':
                    client.send(self.name.encode('utf-8'))
                else:
                    pass
            except:
                print("An error occured!")
                client.close()
                break

g = GUI()

# def write():
#     while True:
#         message = '{}: {}'.format(nickname, input(''))
#         client.send(message.encode('utf-8'))

# receive_thread = Thread(target=receive)
# receive_thread.start()
# write_thread = Thread(target=write)
# write_thread.start()