#####################################################################
#    DCM Version 2.0 , Nov 15,2019                                  #
#    -> Module for the menu                                         #
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
# import Serial_com             #
# import time                   #
#################################
from tkinter import *
import tkinter as tk
import Login_Screen
import Pacing_Screen
import EGram_Window
import Serial_com
import pandas as pd
import Excel_Handling as ex





class menu:
    def __init__(self, master, user, df):
        self.frame_root = Frame(master, width=500, height=500)
        self.frame_root.pack()
        self.background_image = tk.PhotoImage(file="backgroundpacing1.png")
        self.label = Label(self.frame_root, image=self.background_image)
        self.label.image = self.background_image
        self.label.pack()
        self.user = user
        self.master = master
        self.df = df

        self.parameter_editor_image = tk.PhotoImage(file="Parametereditor.png")
        self.parameter_editor = Button(self.frame_root, image=self.parameter_editor_image)
        self.parameter_editor.config(command=self.to_pacing)
        self.parameter_editor.place(x=150, y=140)

        self.Serialsettings_image = tk.PhotoImage(file="Serialsettings.png")
        self.Serialsettings = Button(self.frame_root, image=self.Serialsettings_image)
        self.Serialsettings.config(command=self.to_Serialsettings)
        self.Serialsettings.place(x=150, y=250)

        self.Egram_image = tk.PhotoImage(file="Egrambutton.png")
        self.Egram = Button(self.frame_root, image=self.Egram_image)
        self.Egram.config(command=self.to_egram)
        self.Egram.place(x=150, y=360)

        self.sign_image = tk.PhotoImage(file="signout.png")
        self.button_sign = Button(self.frame_root, image=self.sign_image)
        self.button_sign.config(command=self.from_menu)
        self.button_sign.place(x=400, y=50)

    def from_menu(self):
        self.frame_root.pack_forget()
        self.login = Login_Screen.Login_Window(self.master, self.df)

    def to_pacing(self):
        self.frame_root.pack_forget()
        self.pacing = Pacing_Screen.Pacing_Window(self.master, self.user, self.df)

    def to_egram(self):
        self.frame_root.pack_forget()
        self.egram = EGram_Window.Electrogram(self.master,self.user, self.df)

    def to_Serialsettings(self):
        self.frame_root.pack_forget()
        self.settings = Serial_com.Serial_Window(self.master, self.user, self.df)
