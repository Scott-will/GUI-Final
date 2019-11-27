#####################################################################
#    DCM Version 2.0 , Nov 15,2019                                  #
#    -> Module for the mode selection screen                        #
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
#import panda as pd             #
#import Excel_Handling as ex    #
#################################

# Note:
# The lambda keyword allows use to pass parameters to function calls that are tied to buttons


from tkinter import *
import tkinter as tk
import Login_Screen
import Menu_Window
import Paramter_Window





class Pacing_Window:
    def __init__(self, master, user, df):
        self.frame_root = Frame(master, width=500, height=500)
        self.frame_root.pack()
        self.background_image = tk.PhotoImage(file="backgroundpacing.png")
        self.label = Label(self.frame_root, image=self.background_image)
        self.label.image = self.background_image
        self.label.pack()
        self.text = Label(self.frame_root, text="Please select a Pacing mode")
        self.text.config(font=("Courier", 15))
        self.text.place(x=270, y=100)
        self.user = user
        self.master = master
        self.df = df

        self.signout_image = tk.PhotoImage(file="signout.png")
        self.button_signout = Button(self.frame_root, image=self.signout_image)
        self.button_signout.config(command=self.from_Pacing_Window)
        self.button_signout.place(x=770, y=90)

        self.Back_image = tk.PhotoImage(file="Back.png")
        self.button_back = Button(self.frame_root, image=self.Back_image)
        self.button_back.config(command=self.To_Menu)
        self.button_back.place(x=770, y=50)

        # The lambda keyword allows use to pass parameters to function calls that are tied to buttons
        self.AOO_image = tk.PhotoImage(file="AOO.png")
        self.AOO_button = Button(self.frame_root, image=self.AOO_image)
        self.AOO_button.config(command=lambda: self.To_Parameters(1))
        self.AOO_button.place(x=80, y=150)

        self.VOO_image = tk.PhotoImage(file="VOO.png")
        self.VOO_button = Button(self.frame_root, image=self.VOO_image)
        self.VOO_button.config(command=lambda: self.To_Parameters(2))
        self.VOO_button.place(x=80, y=250)

        self.AAI_image = tk.PhotoImage(file="AAI.png")
        self.AAI_button = Button(self.frame_root, image=self.AAI_image)
        self.AAI_button.config(command=lambda: self.To_Parameters(3))
        self.AAI_button.place(x=280, y=150)

        self.VVI_image = tk.PhotoImage(file="VVI.png")
        self.VVI_button = Button(self.frame_root, image=self.VVI_image)
        self.VVI_button.config(command=lambda: self.To_Parameters(4))
        self.VVI_button.place(x=280, y=250)

        self.DOO_image = tk.PhotoImage(file="DOO.png")
        self.DOO_button = Button(self.frame_root, image=self.DOO_image)
        self.DOO_button.config(command=lambda: self.To_Parameters(5))
        self.DOO_button.place(x=80, y=350)

        self.DOOR_image = tk.PhotoImage(file="DOOR.png")
        self.DOOR_button = Button(self.frame_root, image=self.DOOR_image)
        self.DOOR_button.config(command=lambda: self.To_Parameters(6))
        self.DOOR_button.place(x=280, y=350)

        self.DDDR_image = tk.PhotoImage(file="DDDR.png")
        self.DDDR_button = Button(self.frame_root, image=self.DDDR_image)
        self.DDDR_button.config(command=lambda: self.To_Parameters(7))
        self.DDDR_button.place(x=480, y=350)

        self.AAIR_image = tk.PhotoImage(file="AAIR.png")
        self.AAIR_button = Button(self.frame_root, image=self.AAIR_image)
        self.AAIR_button.config(command=lambda: self.To_Parameters(8))
        self.AAIR_button.place(x=480, y=150)

        self.AOOR_image = tk.PhotoImage(file="AOOR.png")
        self.AOOR_button = Button(self.frame_root, image=self.AOOR_image)
        self.AOOR_button.config(command=lambda: self.To_Parameters(9))
        self.AOOR_button.place(x=680, y=150)

        self.VVIR_image = tk.PhotoImage(file="VVIR.png")
        self.VVIR_button = Button(self.frame_root, image=self.VVIR_image)
        self.VVIR_button.config(command=lambda: self.To_Parameters(10))
        self.VVIR_button.place(x=480, y=250)

        self.VOOR_image = tk.PhotoImage(file="VOOR.png")
        self.VOOR_button = Button(self.frame_root, image=self.VOOR_image)
        self.VOOR_button.config(command=lambda: self.To_Parameters(11))
        self.VOOR_button.place(x=680, y=250)

    def from_Pacing_Window(self):  # Transition function from new user window to the login screen
        self.frame_root.pack_forget()
        self.LoginScreen = Login_Screen.Login_Window(self.master, self.df)

    def To_Parameters(self,mode):
        self.frame_root.pack_forget()
        self.ParameterWindow = Paramter_Window.Parameter_Window(self.master, mode, self.user, self.df)

    def To_Menu(self):
        self.frame_root.pack_forget()
        self.menu = Menu_Window.menu(self.master,self.user, self.df)
