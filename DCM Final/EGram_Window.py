#####################################################################
#    DCM Version 2.0 , Nov 15,2019                                  #
#    -> Module for the Egram plot, currently has no function        #
#                                                                   #
#####################################################################

import tkinter as tk
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
from tkinter import *
import Notifiy_Window
import Login_Screen
import Menu_Window


class Electrogram: # Still need to impletment
    def __init__(self,master,user):
        self.frame_root = Frame(master, width=1500, height=500)
        self.frame_root.pack()
        self.background_image = tk.PhotoImage(file="backgroundegram.png")
        self.label = Label(self.frame_root, image=self.background_image)
        self.label.image = self.background_image
        self.label.pack()
        self.user = user
        self.master = master

        self.signout_image = tk.PhotoImage(file="signout.png")
        self.button_signout = Button(self.frame_root, image=self.signout_image)
        self.button_signout.config(command=self.from_Egram)
        self.button_signout.place(x=1400, y=70)

        self.Back_image = tk.PhotoImage(file="Back.png")
        self.button_back = Button(self.frame_root, image=self.Back_image)
        self.button_back.config(command=self.To_Menu)
        self.button_back.place(x=1400, y=30)

    def from_Egram(self):
        self.frame_root.pack_forget()
        choice = Notifiy_Window.Notify_window(9)
        if choice:
            self.LoginScreen = Login_Screen.Login_Window(self.master)
        else:
            return

    def To_Menu(self):
        self.frame_root.pack_forget()
        self.menu = Menu_Window.menu(self.master, self.user)

