from Tkinter import *
import serial
import functions as fun
import thread

class App:

    def __init__(self, master):
        self.refresh = "0"

        frame = Frame(master)
        frame.pack()
        self.ser = None

        self.button = Button(
            frame, text="Connect", fg="red", command=self.connect
            )
        self.button.pack(side=LEFT)


        self.zenter = Button(
            frame, text="CENTER", fg="red", command=self.cent
            )
        self.zenter.pack(side=LEFT)
        self.right = Button(
            frame, text="Right", fg="red", command=self.right
            )
        self.right.pack(side=LEFT)


        self.left = Button(
            frame, text="Left", fg="red", command=self.left
            )
        self.left.pack(side=LEFT)


        self.set = Button(
            frame, text="SET", fg="red", command=self.set
            )
        self.set.pack(side=LEFT)


        self.c = Checkbutton(master, text="Refresh", variable=self.refresh,command=self.refreshvar)
        self.c.pack()
        self.c.var=self.refresh


        self.slider = Scale(master, from_=0, to=180, orient=HORIZONTAL)
        self.slider.pack()
        self.message= Message(master, text="ServoControl\nV0.1")
        self.message.pack()

        self.servselect = Spinbox(master,from_=1, to=32)
        self.servselect.pack()

    def refreshvar(self):
        if self.refresh=="0":
            self.refresh="1"
        else:
            self.refresh="0"



    def connect(self):
        self.ser = serial.Serial('/dev/tty.usbmodem1421', 19200, timeout=1)


    def cent(self):

        fun.center(self.servselect.get(),self.ser)


    def right(self):
        fun.move(0,0.1,self.servselect.get(),self.ser)
    def left(self):
        fun.move(180,0.1,self.servselect.get(),self.ser)

    def slidethread(self):
         while self.refresh=="1":
                fun.move(int(self.slider.get()),0.1, self.servselect.get(), self.ser)

    def set(self):
        if self.refresh=="1":
           thread.start_new_thread(self.slidethread,())

        else:
            fun.move(int(self.slider.get()),0.1, self.servselect.get(), self.ser)


root = Tk()

app = App(root)

root.mainloop()
root.destroy() # optional; see description below