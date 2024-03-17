import socket
import tkinter as tk
from tkinter import font
from tkinter import ttk
from tkinter import filedialog
import time
import threading
import os
from tkinter import PhotoImage


class GUI:
    
    def __init__(self, ip_address, port):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.connect((ip_address, port))

        self.Window = tk.Tk()
        self.Window.withdraw()

        self.login = tk.Toplevel()

        self.login.title("Thrift Store")
        self.login.resizable(width=False, height=False)
        self.login.configure(width=600, height=600)

        
        self.pls = tk.Label(self.login, 
                            text="Thrift Store\n\n\nPlease Join the negotiation platform of your choice", 
                            justify=tk.CENTER,
                            font="Helvetica 12 bold")

        self.pls.place(relheight=0.15, relx=0.3, rely=0.03)

        original_image = PhotoImage(file="image1.png")
        scale_factor = 0.3
        small_image = original_image.subsample(int(1/scale_factor), int(1/scale_factor))
        label_image1 = tk.Label(self.login, image=small_image)
        label_image1.place(height=200,width=150,relx=0.1, rely=0.2)
        title1_1 = tk.Label(self.login, text="Shirt", font="Helvetica 10 bold")
        title1_1.place(relx=0.20, rely=0.525)
        title1_2 = tk.Label(self.login, text="Price: 600", font="Helvetica 10 bold")
        title1_2.place(relx=0.18, rely=0.55)        
        title1_3 = tk.Label(self.login, text="Product Code: 123", font="Helvetica 10 bold")
        title1_3.place(relx=0.15, rely=0.575)

        original_image2 = PhotoImage(file="image2.png")
        scale_factor2 = 0.52
        small_image2 = original_image2.subsample(int(1/scale_factor2), int(1/scale_factor2))
        label_image2 = tk.Label(self.login, image=small_image2)
        label_image2.place(height=200,width=150,relx=0.4, rely=0.2)
        title2_1 = tk.Label(self.login, text="Pant", font="Helvetica 10 bold")
        title2_1.place(relx=0.51, rely=0.54)
        title2_2 = tk.Label(self.login, text="Price: 1000", font="Helvetica 10 bold")
        title2_2.place(relx=0.48, rely=0.565)
        title2_3 = tk.Label(self.login, text="Product Code: 456", font="Helvetica 10 bold")
        title2_3.place(relx=0.45, rely=0.59)

        original_image3 = PhotoImage(file="image3.png")
        scale_factor3 = 0.4
        small_image3 = original_image3.subsample(int(1/scale_factor3), int(1/scale_factor3))
        label_image3 = tk.Label(self.login, image=small_image3)
        label_image3.place(height=200,width=150,relx=0.7, rely=0.2)
        title3_1 = tk.Label(self.login, text="Dress", font="Helvetica 10 bold")
        title3_1.place(relx=0.80, rely=0.54)
        title3_2 = tk.Label(self.login, text="Price: 900", font="Helvetica 10 bold")
        title3_2.place(relx=0.78, rely=0.565)
        title3_3 = tk.Label(self.login, text="Product Code: 789", font="Helvetica 10 bold")
        title3_3.place(relx=0.75, rely=0.59)
        

        self.userLabelName = tk.Label(self.login, text="Your Username: ", font="Helvetica 11")
        self.userLabelName.place(relheight=0.2, relx=0.1, rely=0.60)

        self.userEntryName = tk.Entry(self.login, font="Helvetica 12")
        self.userEntryName.place(relwidth=0.4 ,relheight=0.075, relx=0.27, rely=0.66)
        self.userEntryName.focus()

        self.roomLabelName = tk.Label(self.login, text="Product Code: ", font="Helvetica 12")
        self.roomLabelName.place(relheight=0.2, relx=0.1, rely=0.71)

        self.roomEntryName = tk.Entry(self.login, font="Helvetica 11", show="*")
        self.roomEntryName.place(relwidth=0.4 ,relheight=0.075, relx=0.27, rely=0.77)
        
        self.go = tk.Button(self.login, 
                            text="JOIN", 
                            font="Helvetica 12 bold", 
                            command = lambda: self.goAhead(self.userEntryName.get(), self.roomEntryName.get()))
        
        self.go.place(relx=0.35, rely=0.90)

        self.Window.mainloop()


    def goAhead(self, username, room_id=0):
        self.name = username
        self.server.send(str.encode(username))
        time.sleep(0.1)
        self.server.send(str.encode(room_id))
        
        self.login.destroy()
        self.layout()

        rcv = threading.Thread(target=self.receive) 
        rcv.start()


    def layout(self):
        self.Window.deiconify()
        self.Window.title("Negotiation Dailogue")
        self.Window.resizable(width=False, height=False)
        self.Window.configure(width=470, height=550, bg="#C74F54")
        self.chatBoxHead = tk.Label(self.Window, 
                                    bg = "#C74F54", 
                                    fg = "#EAECEE", 
                                    text = self.name , 
                                    font = "Helvetica 11 bold", 
                                    pady = 5)

        self.chatBoxHead.place(relwidth = 1)

        self.line = tk.Label(self.Window, width = 450, bg = "#ABB2B9") 
		
        self.line.place(relwidth = 1, rely = 0.07, relheight = 0.012) 
		
        self.textCons = tk.Text(self.Window, 
                                width=20, 
                                height=2, 
                                bg="#F1BFAD", 
                                fg="#0a0a0a", 
                                font="Helvetica 11", 
                                padx=5, 
                                pady=5) 
		
        self.textCons.place(relheight=0.745, relwidth=1, rely=0.08) 
		
        self.labelBottom = tk.Label(self.Window, bg="#ABB2B9", height=80) 
		
        self.labelBottom.place(relwidth = 1, 
							    rely = 0.8) 
		
        self.entryMsg = tk.Entry(self.labelBottom, 
                                bg = "#2C3E50", 
                                fg = "#EAECEE", 
                                font = "Helvetica 11")
        self.entryMsg.place(relwidth = 0.74, 
							relheight = 0.03, 
							rely = 0.008, 
							relx = 0.011) 
        self.entryMsg.focus()

        self.buttonMsg = tk.Button(self.labelBottom, 
								text = "Send", 
								font = "Helvetica 10 bold", 
								width = 20, 
								bg = "#ABB2B9", 
								command = lambda : self.sendButton(self.entryMsg.get())) 
        self.buttonMsg.place(relx = 0.77, 
							rely = 0.008, 
							relheight = 0.03, 
							relwidth = 0.22) 


       

        
    

        self.textCons.config(cursor = "arrow")
        scrollbar = tk.Scrollbar(self.textCons) 
        scrollbar.place(relheight = 1, 
						relx = 0.974)

        scrollbar.config(command = self.textCons.yview)
        self.textCons.config(state = tk.DISABLED)


    

    


    def sendButton(self, msg):
        self.textCons.config(state = tk.DISABLED) 
        self.msg=msg 
        self.entryMsg.delete(0, tk.END) 
        snd= threading.Thread(target = self.sendMessage) 
        snd.start() 


    def receive(self):
        while True:
            try:
                message = self.server.recv(1024).decode()

                if str(message) == "FILE":
                    file_name = self.server.recv(1024).decode()
                    lenOfFile = self.server.recv(1024).decode()
                    send_user = self.server.recv(1024).decode()

                    if os.path.exists(file_name):
                        os.remove(file_name)

                    total = 0
                    with open(file_name, 'wb') as file:
                        while str(total) != lenOfFile:
                            data = self.server.recv(1024)
                            total = total + len(data)     
                            file.write(data)
                    
                    self.textCons.config(state=tk.DISABLED)
                    self.textCons.config(state = tk.NORMAL)
                    self.textCons.insert(tk.END, "<" + str(send_user) + "> " + file_name + " Received\n\n")
                    self.textCons.config(state = tk.DISABLED) 
                    self.textCons.see(tk.END)

                else:
                    self.textCons.config(state=tk.DISABLED)
                    self.textCons.config(state = tk.NORMAL)
                    self.textCons.insert(tk.END, 
                                    message+"\n\n") 

                    self.textCons.config(state = tk.DISABLED) 
                    self.textCons.see(tk.END)

            except: 
                print("An error occured!") 
                self.server.close() 
                break

    def sendMessage(self):
        self.textCons.config(state=tk.DISABLED) 
        while True:  
            self.server.send(self.msg.encode())
            self.textCons.config(state = tk.NORMAL)
            self.textCons.insert(tk.END, 
                            "<You> " + self.msg + "\n\n") 

            self.textCons.config(state = tk.DISABLED) 
            self.textCons.see(tk.END)
            break



if __name__ == "__main__":
    ip_address = "172.16.10.74"
    port = 12345
    g = GUI(ip_address, port)
