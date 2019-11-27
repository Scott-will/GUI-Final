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

from tkinter import*
import Login_Screen
import Excel_Handling as ex

root = Tk()  # Created the window where the entire program is run
df = ex.CreateDataFrame()
# This make it so the users cannot adjust the side of the window, we do this because expanding
# the window will ruin the background and layout fo the widgets
root.resizable(0, 0)

# Here we take the window we just created and we place the first frame onto it which is the login frame
LoginScreen =Login_Screen.Login_Window(root, df)

# Creates a infinite loop that keeps the program from closing
root.mainloop()