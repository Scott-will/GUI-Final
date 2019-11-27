#####################################################################
#    DCM Version 2.0 , Nov 15,2019                                  #
#    -> Module for the Login Screen and its required functions       #
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
from tkinter import *
import tkinter as tk
import pickle
import New_User_Screen
import Menu_Window
import Notifiy_Window
import pandas as pd
import Excel_Handling as ex




class Login_Window:  # Class for the create of the main login window
    def __init__(self, master, df):  ##initializes the class, root is the master

        # We will be using the same root window and placing and removing frames different frames, every class will
        # have its own frame
        self.frame_root = Frame(master, width=500, height=500)
        self.frame_root.pack()
        self.master = master
        self.df = df

        # Here we are setting the background image for the window. line 46 creates a reference to the image as python
        # will garbage collect the image if there is no reference made
        self.background_image = tk.PhotoImage(file='newbackground.png')
        self.label = Label(self.frame_root, image=self.background_image)
        self.label.image = self.background_image
        self.label.pack()

        # Block for the creation of text labels for the login frame
        self.label_user = Label(self.frame_root, text="UserID:")
        self.label_user.place(x=125, y=350)
        self.label_pass = Label(self.frame_root, text="Password:")
        self.label_pass.place(x=110, y=380)
        self.label_remember = Label(self.frame_root, text="Remember me")
        self.label_remember.place(x=190, y=401)

        # Block for the creation of the entry boxes for the login frame
        self.entry_user = Entry(self.frame_root)
        self.entry_user.place(x=170, y=350)
        self.entry_pass = Entry(self.frame_root)
        self.entry_pass.config(show="*")
        self.entry_pass.place(x=170, y=380)

        # Block for the creation of the checkboxes for the login frame
        self.check_state_var = IntVar()  ##variable to check the state of the checkbox
        self.checkbutton_remember = Checkbutton(self.frame_root,
                                                variable=self.check_state_var)  ##, command=self.remember_me())

        # Block for the creation of the buttons for the login frame
        self.button_login = Button(self.frame_root, text="Login",
                                   command=self.menu_screen)  # command = self.check_user(self.entry_user.get(), self.entry_pass.get()))
        self.button_login.place(x=170, y=425)
        # self.button_login.config(command=self.check_user(self.entry_user.get(), self.entry_pass.get()))
        self.button_create = Button(self.frame_root, text="New User", command=self.new_user_window)
        self.button_create.place(x=235, y=425)

    def menu_screen(self):
        password = self.entry_pass.get()
        username = self.entry_user.get()
        success = 0  ##variable to check if need to call error window

        for i in range(0, 20, 2):  # checks if user exists and password is correct
            if self.df['Users'].iloc[i] == username:
                if password == self.df['Users'].iloc[i + 1]:
                    self.frame_root.pack_forget()
                    self.menuscreen = Menu_Window.menu(self.master, username, self.df)
                    success = 1
                    break
        if success == 0:
            Error = Notifiy_Window.Notify_window(6)  ##user does not exist


    def new_user_window(self):  # calls new user screen
        self.frame_root.pack_forget()
        self.NewUserWindow = New_User_Screen.New_User_Window(self.master, self.df)