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
import Serial_com as sc






def start_threading():
    try:
        port_controller = threading.Thread(target=sc.check_serial)
        port_controller.setDaemon(True)  # set thread to daemon ('ok' won't be printed in this case)
        port_controller.start()
        print("Thread started")
    except:
        print("Error: unable to start thread")


#root = Tk()  # Created the window where the entire program is run
df = ex.CreateDataFrame()
# This make it so the users cannot adjust the side of the window, we do this because expanding
# the window will ruin the background and layout fo the widgets
sc.root.resizable(False, True)
sc.root.configure(background="#A21F03")
# Here we take the window we just created and we place the first frame onto it which is the login frame
LoginScreen =Login_Screen.Login_Window(sc.root, df)
start_threading()
# Creates a infinite loop that keeps the program from closing
sc.root.mainloop()