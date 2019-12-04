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

import Lists
import Login_Screen
from tkinter import *
import tkinter as tk
import Pacing_Screen



class Notify_window():  # Class to warn users of errors various errors or to notify them of a conformation
    # If you want to add more errors or conformations, start a new block of if and elif cases
    # Use this class for any notifications that require a separate window
    ## need a window to: show file writing was success && paramaters saved, user added,
    def __init__(self, error, frame, master, df, choice, user):
        winsound.PlaySound("sound.wav", winsound.SND_ASYNC)  # Basic windows error sound to notify users
        self.box = tk.Toplevel()  # Creating a separate tk window for the errors
        self.box.geometry('300x100')
        self.box.resizable(0, 0)

        self.frame = frame
        self.master = master
        self.df =df
        self.user = user
        # Button for closing the error window
        if choice == 0:
            Ok_button = Button(self.box, text="        OK        ", command=lambda: self.signout(1, self.frame,self.master,self.df))
            Ok_button.place(x=80, y=50)

            Ok_button = Button(self.box, text="      Cancel      ", command=lambda: self.signout(0, self.frame,self.master,self.df))
            Ok_button.place(x=160, y=50)

            if error == 9:
                error8_label = Label(self.box, text="Are you sure you want to sign out?\n all unsaved progress will be lost.")
                error8_label.place(x=80, y=20)

        elif choice == 1:
            Ok_button = Button(self.box, text="        OK        ", command=lambda: self.back(1, self.frame,self.master,self.df,self.user))
            Ok_button.place(x=80, y=50)

            Ok_button = Button(self.box, text="      Cancel      ", command=lambda: self.back(0, self.frame,self.master,self.df,self.user))
            Ok_button.place(x=160, y=50)

            if error == 10:
                error8_label = Label(self.box, text="Are you sure you want to back? \n all unsaved progress will be lost.")
                error8_label.place(x=80, y=20)


        elif choice == 2:
            Ok_button = Button(self.box, text="        OK        ", command=lambda: self.action(1))
            Ok_button.place(x=80, y=50)

            Ok_button = Button(self.box, text="      Cancel      ",command=lambda: self.action(0))
            Ok_button.place(x=160, y=50)

            if error == 1:  # For no username entered in register
                error1_label = Label(self.box, text="Username already exists")
                error1_label.place(x=80, y=20)

            elif error == 2:  # For after save/apply is pressed
                error2_label = Label(self.box, text="Parameters successfully updated")
                error2_label.place(x=80, y=20)

            elif error == 3:  # For no confirm password in register
                error3_label = Label(self.box,
                                     text="Username/Password must have at least\n5 characters and contain a number")
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
                Ok_button.pack_forget()
                Ok_button.pack_forget()

                self.list = Lists.Parameter_List()

                Ok_button = Button(self.box, text="        OK        ", command=lambda: self.action2(1))
                Ok_button.place(x=80, y=50)

                Ok_button = Button(self.box, text="      Cancel      ", command=lambda: self.action2(0))
                Ok_button.place(x=160, y=50)



            elif error == 9:
                error9_label = Label(self.box, text = "No board connected")
                error9_label.place(x = 80, y = 20)




    def action(self, choice):
        if choice == 0:
            self.box.destroy()
        elif choice == 1:
            self.box.destroy()

    def action2(self, choice):
        if choice == 0:
            self.box.destroy()
            self.list.remove()
        elif choice == 1:
            self.box.destroy()
            self.list.remove()


    def signout(self, choice, frame, master, df):
        self.frame = frame
        self.master = master
        self.df = df
        if choice == 0:
            self.box.destroy()
        elif choice == 1:
            self.box.destroy()
            self.frame.pack_forget()
            self.login_window = Login_Screen.Login_Window(self.master, self.df)

    def back(self, choice, frame, master, df, user):
        self.frame = frame
        self.master = master
        self.df = df
        self.user = user
        if choice == 0:
            self.box.destroy()
        elif choice == 1:
            self.box.destroy()
            self.frame.pack_forget()
            self.pacing_screen = Pacing_Screen.Pacing_Window(self.master, self.user, self.df)

