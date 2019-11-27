#####################################################################
#    DCM Version 2.0 , Nov 15,2019                                  #
#    -> Moved for a single definitions file where all classes are   #
#       defined to each class having its own python file            #
#####################################################################

#################################
# Import classes as needed      #
# Class list:                   #
# import winsound               #
# from tkinter import *         #
# import tkinter as tk          #
# import pickle                 #
# import Login_Screen           #
# import New_User_Screen        #
# import Menu_Window            #
# import Parameter_Window       #
# import Pacing_Screen          #
# import EGram_Window           #
# import Notify_Window          #
# import serial                 #
# import Serial_com             #
# import time                   #
#import panda as pd             #
#import Excel_Handling as ex    #
#################################
import tkinter as tk
from tkinter import*
import Login_Screen
import Excel_Handling as ex
from serial import Serial
import threading
import time
import serial.tools.list_ports

serial_init = 0 # keeps track if the serial port has been initialized or not
refresh = 0.5 # Variable used to change the refresh speed of the serial status



class State:
    state = False

    def __init__(self, x):
        self.state = x

status = State(False)

def check_serial():
    try:
        s = Serial()
        s.port = 'COM8'
        s.baudrate = 9600
        s.timeout = 0.5
        s.dtr = 0
        s.open()
        serial_init = 1
        myports = [tuple(p) for p in list(serial.tools.list_ports.comports())]
        print(myports)
        serial_port = [port for port in myports if 'COM8' in port][0]
        status.state = True
    except:
        print("serial not open")
        serial_init = 0
        serialclosed_image = tk.PhotoImage(file="serialclosed.png")
        label_serialclosed = Label(root, image=serialclosed_image)
        label_serialclosed.pack(side=BOTTOM)
        time.sleep(refresh)
        label_serialclosed.pack_forget()
        status.state = False

    while (1):
        if (serial_init == 1):
            if status.state:
                serialopen_image = tk.PhotoImage(file="serialopen.png")
                label_serialopen = Label(root, image=serialopen_image)
                label_serialopen.pack(side=TOP)
                time.sleep(refresh)
                label_serialopen.pack_forget()


            elif (not status.state):
                serialclosed_image = tk.PhotoImage(file="serialclosed.png")
                label_serialclosed = Label(root, image=serialclosed_image)
                label_serialclosed.pack(side=TOP)
                time.sleep(refresh)
                label_serialclosed.pack_forget()


            myports = [tuple(p) for p in list(serial.tools.list_ports.comports())]
            if serial_port not in myports:
                status.state = False
                serialclosed_image = tk.PhotoImage(file="serialclosed.png")
                label_serialclosed = Label(root, image=serialclosed_image)
                label_serialclosed.pack(side=TOP)
                time.sleep(refresh)
                label_serialclosed.pack_forget()

            time.sleep(0.1)

        elif (serial_init == 0):
            serialclosed_image = tk.PhotoImage(file="serialclosed.png")
            label_serialclosed = Label(root, image=serialclosed_image)
            label_serialclosed.pack(side=BOTTOM)
            time.sleep(refresh)
            label_serialclosed.pack_forget()
            try:
                s = Serial()
                s.port = 'COM8'
                s.baudrate = 9600
                s.timeout = 0.5
                s.dtr = 0
                s.open()
                serial_init = 1
                myports = [tuple(p) for p in list(serial.tools.list_ports.comports())]
                print(myports)
                serial_port = [port for port in myports if 'COM8' in port][0]
                status.state = True
            except:
                print("serial not open")
                serial_init = 0
                status.state = False

def start_threading():
    try:
        port_controller = threading.Thread(target=check_serial)
        port_controller.setDaemon(True)  # set thread to daemon ('ok' won't be printed in this case)
        port_controller.start()
        print("Thread started")
    except:
        print("Error: unable to start thread")


root = Tk()  # Created the window where the entire program is run
df = ex.CreateDataFrame()
# This make it so the users cannot adjust the side of the window, we do this because expanding
# the window will ruin the background and layout fo the widgets
root.resizable(0, 0)
root.configure(background="#A21F03")
# Here we take the window we just created and we place the first frame onto it which is the login frame
LoginScreen =Login_Screen.Login_Window(root, df)
start_threading()
# Creates a infinite loop that keeps the program from closing
root.mainloop()