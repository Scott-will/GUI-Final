#####################################################################
#    DCM Version 2.0 , Nov 15,2019                                  #
#    -> Module for serial communication                             #
#                                                                   #
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
#################################

import tkinter as tk
from tkinter import *
import serial
from serial import Serial
import time
import serial.tools.list_ports




################################################
#           Serial configuration               #
#                                              #
################################################
class State:
    state = False

    def __init__(self, x):
        self.state = x

s = 0
serial_init = 0
serial_port = 0
myports = 0
refresh = 0.5 # Variable used to change the refresh speed of the serial status
status = State(False)
root = Tk()




def check_serial():
    global serial_init, serial_port, myports, status, s, refresh, root
    try:
        s = Serial()
        s.port = 'COM6'
        s.baudrate = 9600
        s.timeout = 0.5
        s.dtr = 0
        s.open()
        serial_init = 1
        myports = [tuple(p) for p in list(serial.tools.list_ports.comports())]
        print(myports)
        serial_port = [port for port in myports if 'COM6' in port][0]
        status.state = True
    except:
        print("serial not open")
        serial_init = 0
        status.state = False

    while (1):
        if (serial_init == 1):
            if status.state:
                serialopen_image = tk.PhotoImage(file="serialopen.png")
                label_serialopen = Label(root, image=serialopen_image)
                label_serialopen.pack()
                time.sleep(refresh)
                label_serialopen.pack_forget()


            elif (not status.state):
                serialclosed_image = tk.PhotoImage(file="serialclosed.png")
                label_serialclosed = Label(root, image=serialclosed_image)
                label_serialclosed.pack()
                time.sleep(refresh)
                label_serialclosed.pack_forget()



            myports = [tuple(p) for p in list(serial.tools.list_ports.comports())]
            if serial_port not in myports:
                status.state = False
                serialclosed_image = tk.PhotoImage(file="serialclosed.png")
                label_serialclosed = Label(root, image=serialclosed_image)
                label_serialclosed.pack()
                time.sleep(refresh)
                label_serialclosed.pack_forget()

            time.sleep(0.1)

        elif (serial_init == 0):
            serialclosed_image = tk.PhotoImage(file="serialclosed.png")
            label_serialclosed = Label(root, image=serialclosed_image)
            label_serialclosed.pack()
            time.sleep(refresh)
            label_serialclosed.pack_forget()
            try:
                s = Serial()
                s.port = 'COM6'
                s.baudrate = 9600
                s.timeout = 0.5
                s.dtr = 0
                s.open()
                serial_init = 1
                myports = [tuple(p) for p in list(serial.tools.list_ports.comports())]
                print(myports)
                serial_port = [port for port in myports if 'COM6' in port][0]
                status.state = True
            except:
                print("serial not open")
                serial_init = 0
                status.state = False