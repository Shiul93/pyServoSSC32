from Tkinter import *
import serial
import time
import thread

class App:

    def __init__(self, master):
        self.refresh = "0"

        frame = Frame(master)
        frame.pack()
        self.ser = serial.Serial('/dev/tty.usbmodem1421', 19200, timeout=1)

        self.button = Button(
            frame, text="QUIT", fg="red", command=frame.quit
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

    def refreshvar(self):
        if self.refresh=="0":
            self.refresh="1"
        else:
            self.refresh="0"

    def mappossition(self, x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;


    def move(self, grados, tiempo, servo, ser):
        gradstr = str(self.mappossition(grados, 0, 180, 600, 2500))
        retstr = '#' + str(servo) + 'P'
        retstr += gradstr
        retstr += 'T'
        retstr += str(int(tiempo * 1000))
        retstr += '\r\n'
        print(retstr)
        print(self.refresh)
        self.message.config(text="Servo #"+str(servo)+ "\nPosicion: "+str(grados))
        ser.write(retstr)


    def center(self, servo, ser):
        self.move(90, 0.1, servo, ser)

    def cent(self):
        self.center(1,self.ser)


    def right(self):
        self.move(180,0.1,1,self.ser)
    def left(self):
        self.move(0,0.1,1,self.ser)

    def slidethread(self):
         while self.refresh=="1":
                self.move(int(self.slider.get()),0.1, 1, self.ser)

    def set(self):
        if self.refresh=="1":
           thread.start_new_thread(self.slidethread,())

        else:
            self.move(int(self.slider.get()),0.1, 1, self.ser)


root = Tk()

app = App(root)

root.mainloop()
root.destroy() # optional; see description below