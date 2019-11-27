#####################################################################
#    DCM Version 2.0 , Nov 15,2019                                  #
#    -> Module for the various notifications                       #
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
# import time                   #
#################################

import winsound
from tkinter import *


class Notify_window():  # Class to warn users of errors various errors or to notify them of a conformation
    # If you want to add more errors or conformations, start a new block of if and elif cases
    # Use this class for any notifications that require a separate window
    ## need a window to: show file writing was success && paramaters saved, user added,
    def __init__(self, error):
        winsound.PlaySound("sound.wav", winsound.SND_ASYNC)  # Basic windows error sound to notify users
        self.box = Tk()  # Creating a separate tk window for the errors
        self.box.geometry('300x100')
        self.box.resizable(0, 0)
        # Button for closing the error window
        Ok_button = Button(self.box, text="        OK        ", command=lambda: self.action(1))
        Ok_button.place(x=80, y=50)

        Ok_button = Button(self.box, text="      Cancel      ", command=lambda: self.action(0))
        Ok_button.place(x=160, y=50)

        # Add more statements if you have more errors to throw, please label the errors
        if error == 1:  # For no username entered in register
            error1_label = Label(self.box, text="Username already exists")
            error1_label.place(x=80, y=20)

        elif error == 2:  # For after save/apply is pressed
            error2_label = Label(self.box, text="Parameters successfully updated")
            error2_label.place(x=80, y=20)

        elif error == 3:  # For no confirm password in register
            error3_label = Label(self.box, text="Username/Password must have at least\n5 characters and contain a number")
            error3_label.place(x=55, y=20)

        elif error == 4:  # For non matching passwords entered in register
            error4_label = Label(self.box, text="Passwords do not match")
            error4_label.place(x=80, y=20)

        elif error == 5:  # For successful creation of new user
            created_label = Label(self.box, text="Registration confrimed!")
            created_label.place(x=80, y=20)

        elif error == 6:
            error6_label = Label(self.box, text="Username or Password is incorrect")
            error6_label.place(x=80, y=20)

        elif error == 7:
            error7_label = Label(self.box, text="There are already 10 users")
            error7_label.place(x=80, y=20)

        elif error == 8:
            error7_label = Label(self.box, text="Invalid Parameter")
            error7_label.place(x=80, y=20)

        elif error == 9:
            error8_label = Label(self.box, text="Are you sure you want to sign out?")
            error8_label.place(x=80, y=20)

    def action(self, choice):
        if choice == 0:
            self.box.destroy()
            return 0
        elif choice == 1:
            self.box.destroy()
            return 1
