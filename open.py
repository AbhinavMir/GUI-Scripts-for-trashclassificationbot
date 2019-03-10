from tkinter import *
import os
import subprocess

master = Tk()
f=open('C:/Users/HP/AppData/Local/Packages/CanonicalGroupLimited.UbuntuonWindows_79rhkp1fndgsc/LocalState/rootfs/home/abhinavmir/tf-demo/tensorflow-for-poets-2/out.txt','r')

howto = Label(master, text='To click photo presss <space> when camera is open,and to close camera press <esc> \n CLICK resart AFTER CLICKING NEW IMAGE \n Type in source init.sh after clicking predict in your terminal')
howto.pack()

def opencam():
    os.system('a.py')

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def opencam2():
    os.system('b.py')

def predict():
    subprocess.call(['C:/Windows/System32/bash.exe'])
    print(file_contents)
    label = Label(master, text=file_contents)
    #subprocess.call(['c:/users/hp/open.py'])
    label.pack()

a1 = Button(master, text="Open Webcam", command=opencam)
a1.pack()

a2 = Button(master, text="Open IP Cam", command=opencam2)
a2.pack()

b = Button(master, text="Predict and Display Results", command=predict)
b.pack()

w = Button(master, text="Restart", command=restart_program)
w.pack()




file_contents = f.read()

f.close()
mainloop()
