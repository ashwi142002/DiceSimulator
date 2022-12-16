import random as r
import tkinter as tk
class rolling():
    def __init__(self,root):# 'root' is taking because i want the root window in my class
        self.root=root
        l1=tk.Label(self.root,text="Rolling dice",font="arial 20 bold",bg="red").pack()
        self.b1=tk.Button(self.root,text="Let's started",font="arial 20 bold",command=self.roll)
        self.b1.pack(pady=50)
    def roll(self):
        self.num = r.randrange(0,6)
        self.b1.forget()
        self.image()
        self.b1=tk.Button(self.root,image=self.p1,command=self.roll)

        self.b1.pack(pady=50)
    def image(self):
        img= ['dice1.png','dice2.png','dice3.png','dice4.png','dice5.png','dice6.png']
        self.p1=tk.PhotoImage(file=img[self.num])
root= tk.Tk() #for creating GUI(blank screen)
root.title("Rolling dice")
root.geometry("250x250")
run= rolling(root)
root.mainloop()#for creating GUI(a balnk window)
