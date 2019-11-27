#####################################################################
#    DCM Version 2.0 , Nov 15,2019                                  #
#    -> Module for the parameter window                             #
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
import Login_Screen
import Pacing_Screen
import Notifiy_Window
import Excel_Handling as ex
import pandas as pd
import struct
from serial import Serial



class Parameter_Window:
    def __init__(self, master, mode, user, df):
        self.frame_root = Frame(master, width=1500, height=500)
        self.frame_root.pack()
        self.mode = mode
        self.user = user
        self.master = master
        self.df = df
        self.data = [0]*22
        self.board = openSerial()
        self.boardID = 22
        self.data[0] = self.boardID




        # The following 4 modes will display the correct set of titles depending on which pacing mode the user wants to
        # edit
        if self.mode == 1:
            self.background_image = tk.PhotoImage(file="backgroundpacingAOOVOO.png")
            self.label = Label(self.frame_root, image=self.background_image)
            self.label.image = self.background_image
            self.label.pack()
            # command's parameters are the x and y coordinates for the various widgets it creates
            self.common(125, 172, 125, 222, 30, 170, 30, 220, 300, 50, 300, 350, 300, 300, 300, 90)

            self.label_title1 = Label(self.frame_root, text="AOO Pacing Mode")
            self.label_title1.config(font=("Courier", 11))
            self.label_title1.place(x=130, y=145)
            self.label_Amp = Label(self.frame_root, text="Atrial Amplitude:")
            self.label_Amp.place(x=30, y=270)
            self.label_Pulse_Width = Label(self.frame_root, text="Atrial Pulse Width:")
            self.label_Pulse_Width.place(x=24, y=320)
            self.label_Sens = Label(self.frame_root, text="Atrial Sensitivity:")
            self.label_Sens.place(x=30, y=370)
            self.label_ARP = Label(self.frame_root, text="ARP:")
            self.label_ARP.place(x=93, y=420)
            self.label_PVARP = Label(self.frame_root, text="PVARP:")
            self.label_PVARP.place(x=80, y=470)

            self.entry_AV_Amp = Entry(self.frame_root) #self.entry_AV_Amp, self.entry_Pulse_Width,
            self.entry_AV_Amp.place(x=125, y=270)
            self.entry_Pulse_Width = Entry(self.frame_root)
            self.entry_Pulse_Width.place(x=125, y=320)
            self.entry_AV_Sens = Entry(self.frame_root)
            self.entry_AV_Sens.place(x=125, y=370)
            self.entry_ARP = Entry(self.frame_root)
            self.entry_ARP.place(x=125, y=420)
            self.entry_PVARP = Entry(self.frame_root)
            self.entry_PVARP.place(x=125, y=470)



        elif self.mode == 0:
            self.background_image = tk.PhotoImage(file="backgroundpacingAOOVOO.png")
            self.label = Label(self.frame_root, image=self.background_image)
            self.label.image = self.background_image
            self.label.pack()

            self.common(155, 192, 155, 242, 60, 190, 60, 240, 300, 50, 300, 310, 300, 260, 300, 90)

            self.label_title2 = Label(self.frame_root, text="VOO Pacing Mode")
            self.label_title2.config(font=("Courier", 15))
            self.label_title2.place(x=100, y=150)
            self.label_Amp = Label(self.frame_root, text="Ventricle Amplitude:")
            self.label_Amp.place(x=40, y=292)
            self.label_Pulse_Width = Label(self.frame_root, text="Ventricle Pulse Width:")
            self.label_Pulse_Width.place(x=33, y=342)

            self.entry_AV_Amp = Entry(self.frame_root)
            self.entry_AV_Amp.place(x=155, y=292)
            self.entry_Pulse_Width = Entry(self.frame_root)
            self.entry_Pulse_Width.place(x=155, y=342)



        elif self.mode == 3:
            self.background_image = tk.PhotoImage(file="backgroundpacingVIIAAI.png")
            self.label = Label(self.frame_root, image=self.background_image)
            self.label.image = self.background_image
            self.label.pack()

            self.common(155, 192, 155, 242, 60, 190, 60, 240, 430, 60, 400, 420, 400, 370, 430, 100)

            self.label_title3 = Label(self.frame_root, text="AAI Pacing Mode")
            self.label_title3.config(font=("Courier", 15))
            self.label_title3.place(x=200, y=150)
            self.label_Amp = Label(self.frame_root, text="Atrial Amplitude:")
            self.label_Amp.place(x=57, y=342)
            self.label_Pulse_Width = Label(self.frame_root, text="Atrial Pulse Width:")
            self.label_Pulse_Width.place(x=50, y=292)
            self.label_Sens = Label(self.frame_root, text="Atrial Sensitivity:")
            self.label_Sens.place(x=62, y=392)
            self.label_ARP = Label(self.frame_root, text="ARP:")
            self.label_ARP.place(x=125, y=442)
            self.label_PVARP = Label(self.frame_root, text="PVARP:")
            self.label_PVARP.place(x=365, y=192)
            self.label_Hyst = Label(self.frame_root, text="Hysteresis:")
            self.label_Hyst.place(x=345, y=242)
            self.label_Rate_Smooth = Label(self.frame_root, text="Rate Smoothing:")
            self.label_Rate_Smooth.place(x=315, y=292)

            self.entry_Pulse_Width = Entry(self.frame_root)
            self.entry_Pulse_Width.place(x=155, y=292)
            self.entry_AV_Amp = Entry(self.frame_root)
            self.entry_AV_Amp.place(x=155, y=342)
            self.entry_AV_Sens = Entry(self.frame_root)
            self.entry_AV_Sens.place(x=155, y=392)
            self.entry_ARP = Entry(self.frame_root)
            self.entry_ARP.place(x=155, y=442)

            self.entry_PVARP = Entry(self.frame_root)
            self.entry_PVARP.place(x=410, y=192)
            self.entry_Hyst = Entry(self.frame_root)
            self.entry_Hyst.place(x=410, y=242)
            self.entry_Rate_Smooth = Entry(self.frame_root)
            self.entry_Rate_Smooth.place(x=410, y=292)



        elif self.mode == 2:
            self.background_image = tk.PhotoImage(file="backgroundpacingVIIAAI.png")
            self.label = Label(self.frame_root, image=self.background_image)
            self.label.image = self.background_image
            self.label.pack()

            self.common(180, 182, 180, 232, 85, 182, 85, 232, 430, 60, 400, 350, 400, 300, 430, 100)

            self.label_title4 = Label(self.frame_root, text="VVI Pacing Mode")
            self.label_title4.config(font=("Courier", 12))
            self.label_title4.place(x=210, y=150)
            self.label_Amp = Label(self.frame_root, text="Ventricle Amplitude:")
            self.label_Amp.place(x=66, y=272)
            self.label_Pulse_Width = Label(self.frame_root, text="Ventricle Pulse Width:")
            self.label_Pulse_Width.place(x=60, y=322)
            self.label_Sens = Label(self.frame_root, text="Ventricle Sensitivity:")
            self.label_Sens.place(x=70, y=372)
            self.label_VRP = Label(self.frame_root, text="VRP:")
            self.label_VRP.place(x=150, y=422)
            self.label_Hyst = Label(self.frame_root, text="Hysteresis:")
            self.label_Hyst.place(x=335, y=172)
            self.label_Rate_Smooth = Label(self.frame_root, text="Rate Smoothing:")
            self.label_Rate_Smooth.place(x=317, y=222)

            self.entry_AV_Amp = Entry(self.frame_root)
            self.entry_AV_Amp.place(x=180, y=272)
            self.entry_Pulse_Width = Entry(self.frame_root)
            self.entry_Pulse_Width.place(x=180, y=322)
            self.entry_AV_Sens = Entry(self.frame_root)
            self.entry_AV_Sens.place(x=180, y=372)
            self.entry_VRP = Entry(self.frame_root)
            self.entry_VRP.place(x=180, y=422)
            self.entry_Hyst = Entry(self.frame_root)
            self.entry_Hyst.place(x=410, y=182)
            self.entry_Rate_Smooth = Entry(self.frame_root)
            self.entry_Rate_Smooth.place(x=410, y=232)


        elif self.mode == 4:
            self.background_image = tk.PhotoImage(file="backgroundpacingAOOVOO.png")
            self.label = Label(self.frame_root, image=self.background_image)
            self.label.image = self.background_image
            self.label.pack()

            self.label_title2 = Label(self.frame_root, text="DOO Pacing Mode")
            self.label_title2.config(font=("Courier", 13))
            self.label_title2.place(x=120, y=145)

            self.common(140, 172, 140, 222, 50, 170, 50, 220, 300, 50, 300, 350, 300, 300, 300, 90)

            self.label.AV_del = Label(self.frame_root,text="Fixed Av Delay:")
            self.label.AV_del.place(x=57, y=272)
            self.label_Amp = Label(self.frame_root, text="Atrial Amplitude:")
            self.label_Amp.place(x=45, y=322)
            self.label_Amp = Label(self.frame_root, text="Ventricle Amplitude:")
            self.label_Amp.place(x=27, y=372)
            self.label_Pulse_Width = Label(self.frame_root, text="Atrial Pulse Width:")
            self.label_Pulse_Width.place(x=40, y=422)
            self.label_Pulse_Width = Label(self.frame_root, text="Ventrical Pulse Width:")
            self.label_Pulse_Width.place(x=21, y=472)

            self.entry_AV_del = Entry(self.frame_root)
            self.entry_AV_del.place(x=140, y=272)
            self.entry_AV_Amp = Entry(self.frame_root)
            self.entry_AV_Amp.place(x=140, y=322)
            self.entry_AV_Amp = Entry(self.frame_root)
            self.entry_AV_Amp.place(x=140, y=372)
            self.entry_Pulse_Width = Entry(self.frame_root)
            self.entry_Pulse_Width.place(x=140, y=422)
            self.entry_Pulse_Width = Entry(self.frame_root)
            self.entry_Pulse_Width.place(x=140, y=472)

        elif self.mode == 9:
            self.background_image = tk.PhotoImage(file="backgroundpacingVIIAAI.png")
            self.label = Label(self.frame_root, image=self.background_image)
            self.label.image = self.background_image
            self.label.pack()

            self.label_title2 = Label(self.frame_root, text="DOOR Pacing Mode")
            self.label_title2.config(font=("Courier", 15))
            self.label_title2.place(x=180, y=145)

            self.common(145, 172, 145, 222, 50, 172, 50, 222, 430, 60, 230, 450, 300, 450, 430, 100)

            self.label_Sensor_Rate = Label(self.frame_root, text="Max Sensor Rate:")
            self.label_Sensor_Rate.place(x=50, y=270)
            self.label_AV_Delay = Label(self.frame_root, text="Fixed AV Delay:")
            self.label_AV_Delay.place(x=58, y=320)

            self.label_Amp = Label(self.frame_root, text="Atrial Amplitude:")
            self.label_Amp.place(x=300, y=170)
            self.label_Amp = Label(self.frame_root, text="Ventricle Amplitude:")
            self.label_Amp.place(x=283, y=220)
            self.label_Pulse_Width = Label(self.frame_root, text="Atrial Pulse Width:")
            self.label_Pulse_Width.place(x=292, y=270)
            self.label_Pulse_Width = Label(self.frame_root, text="Ventricle Pulse Width:")
            self.label_Pulse_Width.place(x=278, y=320)
            self.label_Recv_Time = Label(self.frame_root, text="Recovery Time:")
            self.label_Recv_Time.place(x=58, y=370)
            self.label_Resp_Fact = Label(self.frame_root, text="Response Factor:")
            self.label_Resp_Fact.place(x=50, y=420)
            self.label_Act_Thres = Label(self.frame_root, text="Acticity Threshold:")
            self.label_Act_Thres.place(x=295, y=372)
            self.label_React_Time = Label(self.frame_root, text="Reaction Time:")
            self.label_React_Time.place(x=315, y=422)

            self.entry_AV_Sensor_Rate = Entry(self.frame_root)
            self.entry_AV_Sensor_Rate.place(x=145, y=272)
            self.entry_AV_Delay = Entry(self.frame_root)
            self.entry_AV_Delay.place(x=145, y=322)

            self.entry_AV_Amp = Entry(self.frame_root)
            self.entry_AV_Amp.place(x=400, y=172)
            self.entry_AV_Amp = Entry(self.frame_root)
            self.entry_AV_Amp.place(x=400, y=222)
            self.entry_Pulse_Width = Entry(self.frame_root)
            self.entry_Pulse_Width.place(x=400, y=272)
            self.entry_Pulse_Width = Entry(self.frame_root)
            self.entry_Pulse_Width.place(x=400, y=322)

            self.entry_Act_Thres = Entry(self.frame_root)
            self.entry_Act_Thres.place(x=400, y=372)
            self.entry_React_Time = Entry(self.frame_root)
            self.entry_React_Time.place(x=400, y=422)

            self.entry_Recv_Time = Entry(self.frame_root)
            self.entry_Recv_Time.place(x=145, y=370)
            self.entry_Resp_Fact = Entry(self.frame_root)
            self.entry_Resp_Fact.place(x=145, y=420)



        elif self.mode == 10:
            self.background_image = tk.PhotoImage(file="backgroundpacing2.png")
            self.label = Label(self.frame_root, image=self.background_image)
            self.label.image = self.background_image
            self.label.pack()

            self.label_title2 = Label(self.frame_root, text="DDDR Pacing Mode")
            self.label_title2.config(font=("Courier", 15))
            self.label_title2.place(x=650, y=130)

            self.Back_image = tk.PhotoImage(file="Back.png")
            self.button_back = Button(self.frame_root, image=self.Back_image)
            self.button_back.config(command=self.from_Parameter_Window)
            self.button_back.place(x=1400, y=35)

            self.button_ok = Button(self.frame_root, text="     Ok     ")
            self.button_ok.config(command=self.Ok)
            self.button_apply = Button(self.frame_root, text="    Apply    ")
            self.button_apply.config(command=self.Apply)
            self.button_apply.place(x=1100, y=250)
            self.button_ok.place(x=1100, y=300)

            self.signout_image = tk.PhotoImage(file="signout.png")
            self.button_signout = Button(self.frame_root, image=self.signout_image)
            self.button_signout.config(command=self.To_login)
            self.button_signout.place(x=1400, y=75)

            self.entry_Recv_Time = Entry(self.frame_root)
            self.entry_Recv_Time.place(x=125, y=172)
            self.entry_Resp_Fact = Entry(self.frame_root)
            self.entry_Resp_Fact.place(x=125, y=222)
            self.entry_AV_Sensor_Rate = Entry(self.frame_root)
            self.entry_AV_Sensor_Rate.place(x=125, y=272)
            self.entry_AV_Delay = Entry(self.frame_root)
            self.entry_AV_Delay.place(x=125, y=322)
            self.entry_Dyn_AV_Delay = Entry(self.frame_root)
            self.entry_Dyn_AV_Delay.place(x=125, y=372)
            self.entry_AV_Delay_Off1 = Entry(self.frame_root)
            self.entry_AV_Delay_Off1.place(x=125, y=422)

            self.entry_AV_Amp = Entry(self.frame_root)
            self.entry_AV_Amp.place(x=400, y=172)
            self.entry_AV_Amp = Entry(self.frame_root)
            self.entry_AV_Amp.place(x=400, y=222)
            self.entry_Pulse_Width = Entry(self.frame_root)
            self.entry_Pulse_Width.place(x=400, y=272)
            self.entry_Pulse_Width = Entry(self.frame_root)
            self.entry_Pulse_Width.place(x=400, y=322)
            self.entry_AV_Sens = Entry(self.frame_root)
            self.entry_AV_Sens.place(x=400, y=372)
            self.entry_AV_Sens = Entry(self.frame_root)
            self.entry_AV_Sens.place(x=400, y=422)

            self.entry_VRP = Entry(self.frame_root)
            self.entry_VRP.place(x=650, y=172)
            self.entry_ARP = Entry(self.frame_root)
            self.entry_ARP.place(x=650, y=222)
            self.entry_PVARP = Entry(self.frame_root)
            self.entry_PVARP.place(x=650, y=272)
            self.entry_PVARP_Ext = Entry(self.frame_root)
            self.entry_PVARP_Ext.place(x=650, y=322)
            self.entry_Hyst = Entry(self.frame_root)
            self.entry_Hyst.place(x=650, y=372)
            self.entry_Rate_Smooth = Entry(self.frame_root)
            self.entry_Rate_Smooth.place(x=650, y=422)

            self.entry_ATR_Dur = Entry(self.frame_root)
            self.entry_ATR_Dur.place(x=920, y=172)
            self.entry_ATR_Fallback_Mode = Entry(self.frame_root)
            self.entry_ATR_Fallback_Mode.place(x=920, y=222)
            self.entry_ATR_Fallback_time = Entry(self.frame_root)
            self.entry_ATR_Fallback_time.place(x=920, y=272)
            self.entry_Act_Thres = Entry(self.frame_root)
            self.entry_Act_Thres.place(x=920, y=322)
            self.entry_React_Time = Entry(self.frame_root)
            self.entry_React_Time.place(x=920, y=372)

            self.label_Recv_Time = Label(self.frame_root, text="Recovery Time:")
            self.label_Recv_Time.place(x=30, y=170)
            self.label_Resp_Fact = Label(self.frame_root, text="Response Factor:")
            self.label_Resp_Fact.place(x=30, y=220)
            self.label_Sensor_Rate = Label(self.frame_root, text="Max Sensor Rate:")
            self.label_Sensor_Rate.place(x=30, y=270)
            self.label_AV_Delay = Label(self.frame_root, text="Fixed AV Delay:")
            self.label_AV_Delay.place(x=30, y=320)
            self.label_Dyn_AV_Delay = Label(self.frame_root, text="Dynamic Av Delay:")
            self.label_Dyn_AV_Delay.config(font=("Times", 8))
            self.label_Dyn_AV_Delay.place(x=25, y=370)
            self.label_Sen_AV_Delay_Off1 = Label(self.frame_root, text="Sensed AV:")
            self.label_Sen_AV_Delay_Off2 = Label(self.frame_root, text="Delay Offset")
            self.label_Sen_AV_Delay_Off1.place(x=55, y=420)
            self.label_Sen_AV_Delay_Off2.place(x=50, y=440)

            self.label_Amp = Label(self.frame_root, text="Atrial Amplitude:")
            self.label_Amp.place(x=300, y=170)
            self.label_Amp = Label(self.frame_root, text="Ventricle Amplitude:")
            self.label_Amp.place(x=283, y=220)
            self.label_Pulse_Width = Label(self.frame_root, text="Atrial Pulse Width:")
            self.label_Pulse_Width.place(x=292, y=270)
            self.label_Pulse_Width = Label(self.frame_root, text="Ventricle Pulse Width:")
            self.label_Pulse_Width.place(x=276, y=320)
            self.label_Sens = Label(self.frame_root, text="Ventricle Sensitivity:")
            self.label_Sens.place(x=288, y=370)
            self.label_Sens = Label(self.frame_root, text="Atrial Sensitivity:")
            self.label_Sens.place(x=303, y=420)

            self.label_VRP = Label(self.frame_root, text="VRP:")
            self.label_VRP.place(x=610, y=170)
            self.label_ARP = Label(self.frame_root, text="ARP:")
            self.label_ARP.place(x=610, y=220)
            self.label_PVARP = Label(self.frame_root, text="PVARP:")
            self.label_PVARP.place(x=600, y=270)
            self.label_PVARP_Ext = Label(self.frame_root, text="PVARP Extension:")
            self.label_PVARP_Ext.place(x=550, y=320)
            self.label_Hyst = Label(self.frame_root, text="Hysteresis:")
            self.label_Hyst.place(x=585, y=370)
            self.label_Rate_Smooth = Label(self.frame_root, text="Rate Smoothing:")
            self.label_Rate_Smooth.place(x=552, y=420)

            self.label_ATR_Dur = Label(self.frame_root, text="ATR Duration:")
            self.label_ATR_Dur.place(x=833, y=170)
            self.label_ATR_Fallback_Mode = Label(self.frame_root, text="ATR Fallback Mode:")
            self.label_ATR_Fallback_Mode.place(x=805, y=220)
            self.label_ATR_Fallback_time = Label(self.frame_root, text="ATR Fallback Time:")
            self.label_ATR_Fallback_time.place(x=810, y=270)
            self.label_Act_Thres = Label(self.frame_root, text="Activity Threshold:")
            self.label_Act_Thres.place(x=810, y=320)
            self.label_React_Time = Label(self.frame_root, text="Reaction Time:")
            self.label_React_Time.place(x=830, y=370)

        elif self.mode == 8:
            self.background_image = tk.PhotoImage(file="backgroundpacing3.png")
            self.label = Label(self.frame_root, image=self.background_image)
            self.label.image = self.background_image
            self.label.pack()

            self.label_title2 = Label(self.frame_root, text="AAIR Pacing Mode")
            self.label_title2.config(font=("Courier", 15))
            self.label_title2.place(x=320, y=120)

            self.common(145, 172, 145, 222, 50, 172, 50, 222, 750, 30, 330, 460, 400, 460, 750, 70)

            self.entry_AV_Sensor_Rate = Entry(self.frame_root)
            self.entry_AV_Sensor_Rate.place(x=145, y=272)
            self.entry_AV_Amp = Entry(self.frame_root)
            self.entry_AV_Amp.place(x=145, y=322)
            self.entry_Pulse_Width = Entry(self.frame_root)
            self.entry_Pulse_Width.place(x=145, y=372)
            self.entry_AV_Sens = Entry(self.frame_root)
            self.entry_AV_Sens.place(x=145, y=422)

            self.label_Sensor_Rate = Label(self.frame_root, text="Max Sensor Rate:")
            self.label_Sensor_Rate.place(x=50, y=272)
            self.label_Amp = Label(self.frame_root, text="Atrial Amplitude:")
            self.label_Amp.place(x=50, y=322)
            self.label_Pulse_Width = Label(self.frame_root, text="Atrial Pulse Width:")
            self.label_Pulse_Width.place(x=45, y=372)
            self.label_Sens = Label(self.frame_root, text="Atrial Sensitivity:")
            self.label_Sens.place(x=50, y=422)

            self.entry_ARP = Entry(self.frame_root)
            self.entry_ARP.place(x=450, y=172)
            self.entry_PVARP = Entry(self.frame_root)
            self.entry_PVARP.place(x=450, y=222)
            self.entry_Hyst = Entry(self.frame_root)
            self.entry_Hyst.place(x=450, y=272)
            self.entry_Rate_Smooth = Entry(self.frame_root)
            self.entry_Rate_Smooth.place(x=450, y=322)
            self.entry_Act_Thres = Entry(self.frame_root)
            self.entry_Act_Thres.place(x=450, y=372)
            self.entry_React_Time = Entry(self.frame_root)
            self.entry_React_Time.place(x=450, y=422)

            self.label_ARP = Label(self.frame_root, text="ARP:")
            self.label_ARP.place(x=413, y=172)
            self.label_PVARP = Label(self.frame_root, text="PVARP:")
            self.label_PVARP.place(x=400, y=222)
            self.label_Hyst = Label(self.frame_root, text="Hysteresis:")
            self.label_Hyst.place(x=385, y=272)
            self.label_Rate_Smooth = Label(self.frame_root, text="Rate Smoothing:")
            self.label_Rate_Smooth.place(x=355, y=322)
            self.label_Act_Thres = Label(self.frame_root, text="Activity Threshold:")
            self.label_Act_Thres.place(x=347, y=372)
            self.label_React_Time = Label(self.frame_root, text="Reaction Time:")
            self.label_React_Time.place(x=365, y=422)

            self.entry_Recv_Time = Entry(self.frame_root)
            self.entry_Recv_Time.place(x=710, y=172)
            self.entry_Resp_Fact = Entry(self.frame_root)
            self.entry_Resp_Fact.place(x=710,y=222)

            self.label_Recv_Time = Label(self.frame_root, text="Recovery Time:")
            self.label_Recv_Time.place(x=621, y=172)
            self.label_Resp_Fact = Label(self.frame_root, text="Response Factor:")
            self.label_Resp_Fact.place(x=615, y=222)

        elif self.mode == 9:
            self.background_image = tk.PhotoImage(file="backgroundpacing1.png")
            self.label = Label(self.frame_root, image=self.background_image)
            self.label.image = self.background_image
            self.label.pack()

            self.label_title2 = Label(self.frame_root, text="AOOR Pacing Mode")
            self.label_title2.config(font=("Courier", 15))
            self.label_title2.place(x=160, y=145)

            self.common(125, 172, 125, 222, 30, 170, 30, 220, 400, 50, 350, 370, 350, 320, 400, 90)

            self.entry_AV_Sensor_Rate = Entry(self.frame_root)
            self.entry_AV_Sensor_Rate.place(x=125, y=272)
            self.entry_Pulse_Width = Entry(self.frame_root)
            self.entry_Pulse_Width.place(x=125, y=322)
            self.entry_AV_Amp = Entry(self.frame_root)
            self.entry_AV_Amp.place(x=125, y=372)
            self.entry_Act_Thres = Entry(self.frame_root)
            self.entry_Act_Thres.place(x=125, y=422)

            self.label_Sensor_Rate = Label(self.frame_root, text="Max Sensor Rate:")
            self.label_Sensor_Rate.place(x=25, y=272)
            self.label_Amp = Label(self.frame_root, text="Atrial Amplitude:")
            self.label_Amp.place(x=25, y=322)
            self.label_Pulse_Width = Label(self.frame_root, text="Atrial Pulse Width:")
            self.label_Pulse_Width.place(x=20, y=372)
            self.label_Act_Thres = Label(self.frame_root, text="Activity Threshold:")
            self.label_Act_Thres.place(x=20, y=422)

            self.entry_Recv_Time = Entry(self.frame_root)
            self.entry_Recv_Time.place(x=360, y=172)
            self.entry_Resp_Fact = Entry(self.frame_root)
            self.entry_Resp_Fact.place(x=360, y=222)
            self.entry_React_Time = Entry(self.frame_root)
            self.entry_React_Time.place(x=360, y=272)


            self.label_React_Time = Label(self.frame_root, text="Reaction Time:")
            self.label_React_Time.place(x=270, y=272)
            self.label_Recv_Time = Label(self.frame_root, text="Recovery Time:")
            self.label_Recv_Time.place(x=270, y=172)
            self.label_Resp_Fact = Label(self.frame_root, text="Response Factor:")
            self.label_Resp_Fact.place(x=265, y=222)

        elif self.mode == 8:
            self.background_image = tk.PhotoImage(file="backgroundpacing3.png")
            self.label = Label(self.frame_root, image=self.background_image)
            self.label.image = self.background_image
            self.label.pack()

            self.label_title2 = Label(self.frame_root, text="VVIR Pacing Mode")
            self.label_title2.config(font=("Courier", 15))
            self.label_title2.place(x=160, y=145)

            self.common(125, 172, 125, 222, 30, 170, 30, 220, 400, 50, 350, 370, 350, 320, 400, 90)

            self.entry_AV_Sensor_Rate = Entry(self.frame_root)
            self.entry_AV_Sensor_Rate.place(x=125, y=272)

            self.label_Sensor_Rate = Label(self.frame_root, text="Max Sensor Rate:")
            self.label_Sensor_Rate.place(x=25, y=272)


    # All widgets are created in common() are common between all 4 pacing mode. Because the layout for the window of
    # each mode is different we will just pass the x and y coord as parameters when the method is called
    def common(self, upperlimx, upperlimy, lowerlimx, lowerlimy, upperlimx2, upperlimy2, lowerlimx2, lowerlimy2, backx,
               backy, okx, oky, applyx, applyy, signoutx, signouty):#, bpmx, bpmy, bpmx2, bpmy2):

        self.entry_Upperlim = Entry(self.frame_root)
        self.entry_Upperlim.place(x=upperlimx, y=upperlimy)
        self.entry_Lowerlim = Entry(self.frame_root)
        self.entry_Lowerlim.place(x=lowerlimx, y=lowerlimy)
        #self.entry_BPM = Enrty(self.frame_root)
        #self.entry_BPM.place(x = bpmx, y = bpmy)

        self.label_lowlim = Label(self.frame_root, text="Lower Rate limit:")
        self.label_lowlim.place(x=lowerlimx2, y=lowerlimy2)
        self.label_uplim = Label(self.frame_root, text="Upper Rate limit:")
        self.label_uplim.place(x=upperlimx2, y=upperlimy2)
        #self.label_BPM = Label(self.frame_root, text = "BPM")
        #self.label_BPM.place(x = bpmx2, bpmy2)

        self.Back_image = tk.PhotoImage(file="Back.png")
        self.button_back = Button(self.frame_root, image=self.Back_image)
        self.button_back.config(command=self.from_Parameter_Window)
        self.button_back.place(x=backx, y=backy)

        self.button_ok = Button(self.frame_root, text="     Ok     ")
        self.button_ok.config(command=self.Ok)
        self.button_apply = Button(self.frame_root, text="    Apply    ")
        self.button_apply.config(command=self.Apply)
        self.button_apply.place(x=applyx, y=applyy)
        self.button_ok.place(x=okx, y=oky)

        self.signout_image = tk.PhotoImage(file="signout.png")
        self.button_signout = Button(self.frame_root, image=self.signout_image)
        self.button_signout.config(command=self.To_login)
        self.button_signout.place(x=signoutx, y=signouty)

    def from_Parameter_Window(self):  # Returns to the pacing screen
        self.frame_root.pack_forget()
        self.PacingWindow = Pacing_Screen.Pacing_Window(self.master, self.user, self.df)

    def To_login(self):
        self.frame_root.pack_forget()
        self.login = Login_Screen.Login_Window(self.master, self.df)


    def Apply(self):  # Apply will save the #parameters in the entry fields and return to the pacing screen
        if self.mode == 1:
            self.save_AOO()
        elif self.mode == 2:
            self.save_VOO()
        elif self.mode == 3:
            self.save_AAI()
        elif self.mode == 4:
            self.save_VVI()
        elif self.mode == 5:
            self.save_DOO()
        elif self.mode == 6:
            self.save_DOOR()
        elif self.mode == 7:
            self.save_DDDR()
        elif self.mode == 8:
            self.save_AOOR()
        elif self.mode == 9:
            self.save_VVIR()
        elif self.mode == 10:
            self.save_AAIR()
        elif self.mode == 11:
            self.save_VOOR()

        self.frame_root.pack_forget()
        self.PacingWindow = Pacing_Screen.Pacing_Window(self.master, self.user, self.df)
        # Add code here to also save the parameters

    def Ok(self):  # Ok will only save the parameters in the entry fields
        if self.mode == 1:
            self.save_AOO()
        elif self.mode == 2:
            self.save_VOO()
        elif self.mode == 3:
            self.save_AAI()
        elif self.mode == 4:
            self.save_VVI()
        elif self.mode == 5:
            self.save_DOO()
        elif self.mode == 6:
            self.save_DOOR()
        elif self.mode == 7:
            self.save_DDDR()
        elif self.mode == 8:
            self.save_AOOR()
        elif self.mode == 9:
            self.save_VVIR()
        elif self.mode == 10:
            self.save_AAIR()
        elif self.mode == 11:
            self.save_VOOR()
        # Just random code so pycharm doesnt freak out that there is nothing in the function
        # add code here to save the parameters

    def save_VOO(self):
        try:
            success =  True
            for i in range(0, 20, 2):
                if self.user == self.df['Users'].iloc[i]:  ##find user
                    data[1] = self.mode
                    if int(self.entry_Lowerlim.get()) in range(45, 66):
                        self.df[self.df['Users'].iloc[i], 'VOO Lower Rate Limit'] = int(self.entry_Lowerlim.get())
                        self.data[2] = int(self.entry_Lowerlim.get())
                    else:
                        success = False
                    if int(self.entry_Upperlim.get()) in range(120, 151):
                        self.df[self.df['Users'].iloc[i], 'VOO Upper Rate Limit'] = int(self.entry_UpperLim.get())
                        self.data[3] = int(self.entry_UpperLim.get())
                    else:
                        success = False
                    if int(self.entry_Pulse_Width.get()) in range(1, 11):
                        self.df[self.df['Users'].iloc[i], 'VOO Pulse Width'] = int(self.entry_Pulse_Width.get())
                        self.data[11] = int(self.entry_Pulse_Width.get())
                    else:
                        success = False
                    if int(self.entry_AV_Amp.get()) in range(50, 101):
                        self.df[self.df['Users'].iloc[i], 'VOO Ventrical Amplitude'] = int(self.entry_AV_Amp.get())
                        self.data[10] = int(self.entry_AV_Amp.get())/100
                    else:
                        success = False
                    #if int(self.entry_BPM.get()) >= int(self.entry_Lowerlim.get()) and int(self.entry_BPM.get()) <= int(self.entry_Upperlim.get()):
                     #   self.df[self.df['Users'].iloc[i], 'VOO BPM'] = int(self.entry_BPM.get())
                      #  self.data[4] = int(self.entry_BPM.get())
                    #else:
                       # success = False
                    if success == True:
                        self.writeParameters()
                        ex.saveDataFrame(self.df)
                    else:
                        Notifiy_Window.Notify_window(8)

            ##lower rate limit, upper rate limit, pulsewidth, ventrical amplitude
        except ValueError:
            Notifiy_Window.Notify_window(8)

    def save_AOO(self):
        try:
            success = True
            for i in range(0, 20, 2):
                if self.user == self.df['Users'].iloc[i]:  ##find user
                    self.data[1] = self.mode
                    if 45 <= int(self.entry_Lowerlim.get()) <= 65:# >= 45 and int(self.entry_Lowerlim.get()) <= 65:#in range(45, 66):
                        self.df[self.df['Users'].iloc[i], 'AOO Lower Rate Limit'] = int(self.entry_Lowerlim.get())
                        self.data[2] = int(self.entry_Lowerlim.get())
                        print('yes')
                    else:
                        success = False
                        print('no')
                    if 120 <= int(self.entry_Upperlim.get()) <= 150:#in range(120, 151):
                        self.df[self.df['Users'].iloc[i], 'AOO Upper Rate Limit'] = int(self.entry_Upperlim.get())
                        self.data[3] = int(self.entry_Upperlim.get())
                        print('yes')
                    else:
                        success = False
                        print('no')
                    if int(self.entry_Pulse_Width.get()) in range(1, 11):
                        self.df[self.df['Users'].iloc[i], 'AOO Pulse Width'] = int(self.entry_Pulse_Width.get())
                        self.data[11] = int(self.entry_Pulse_Width.get())
                        print('yes')
                    else:
                        success = False
                        print('no')
                    if int(self.entry_AV_Amp.get()) in range(50, 101):
                        self.df[self.df['Users'].iloc[i], 'AOO Atrial Amplitude'] = int(self.entry_AV_Amp.get())
                        self.data[9] = int(self.entry_AV_Amp.get())
                        print('yes')
                    else:
                        success = False
                        print('no')
                   # if int(self.entry_BPM.get()) >= int(self.entry_Lowerlim.get()) and int(self.entry_BPM.get()) <= int(self.entry_Upperlim.get()):
                    #    self.df[self.df['Users'].iloc[i], 'AOO BPM'] = int(self.entry_BPM.get())
                     #   self.data[4] = int(self.entry_BPM.get())
                   # else:
                    #    success = False

            if success == True:
                self.writeParameters()
                ex.saveDataFrame(self.df)
                print(self.data)
            else:
                Notifiy_Window.Notify_window(8)
                print(self.data)

            ##lower rate limit, upper rate limit, pulsewidth, ventrical amplitude
        except ValueError:
            Notifiy_Window.Notify_window(8)
        ##LowerRateLimit, upper rate limit, pulse width, atrial amplitude
        ##save parameter

    def save_VVI(self):
        try:
            for i in range(0, 20, 2):
                if self.user == self.df['Users'].iloc[i]:  ##find user
                    self.data[1] = self.mode
                    if int(self.entry_Lowerlim.get()) in range(45, 66):
                        self.df[self.df['Users'].iloc[i], 'VVI Lower Rate Limit'] = int(self.entry_Lowerlim.get())
                        self.data[2] = int(self.entry_Lowerlim.get())
                    else:
                        success = False
                    if int(self.entry_Upperlim.get()) in range(120, 151):
                        self.df[self.df['Users'].iloc[i], 'VVI Upper Rate Limit'] = int(self.entry_Upperlim.get())
                        self.data[3] = int(self.entry_Upperlim.get())
                    else:
                        success = False
                    if int(self.entry_Pulse_Width.get()) in range(1, 11):
                        self.df[self.df['Users'].iloc[i], 'VVI Pulse Width'] = int(self.entry_Pulse_Width.get())
                        self.data[11] = int(self.entry_Pulse_Width.get())
                    else:
                        success = False
                    if int(self.entry_AV_Amp.get()) in range(50, 101):
                        self.df[self.df['Users'].iloc[i], 'VVI Ventrical Amplitude'] = int(self.entry_AV_Amp.get())
                        self.data[10] = int(self.entry_AV_Amp.get())
                    else:
                        success = False
                    if int(self.entry_AV_Sens.get()) >= 65 and int(self.entry_AV_Sens.get()) <= 70:
                        self.df[self.df['Users'].iloc[i], 'VVI Ventrical Sensitivity'] = int(self.entry_AV_Sens.get())
                        self.data[13] = int(self.entry_AV_Sens.get())
                    else:
                        success = False
                    if int(self.entry_VRP.get()) >= 150 and int(self.entry_VRP.get()) <= 300:
                        self.df[self.df['Users'].iloc[i], 'VVI VRP'] = int(self.entry_VRP.get())
                        self.data[15] = int(self.entry_VRP.get())
                    else:
                        success = False
                    if int(self.entry_Rate_Smooth.get()) >= 0 and int(self.entry_Rate_Smooth.get()) <= 100:
                        self.df[self.df['Users'].iloc[i], 'VVI Rate Smoothing'] = int(self.entry_Rate_Smooth.get())
                        self.data[16] = int(self.entry_Rate_Smooth.get())
                    else:
                        success = False
                   # if int(self.entry_BPM.get()) >= int(self.entry_Lowerlim.get()) and int(self.entry_BPM.get()) <= int(self.entry_Upperlim.get()):
                    #    self.df[self.df['Users'].iloc[i], 'VVI BPM'] = int(self.entry_BPM.get())
                      #  self.data[4] = int(self.entry_BPM.get())
                   # else:
                    #    success = False
                    if success == True:
                        self.writeParameters()
                        ex.saveDataFrame(self.df)
                    else:
                        Notifiy_Window.Notify_window(8)

            ##lower rate limit, upper rate limit, pulsewidth, ventrical amplitude
        except ValueError:
            Notifiy_Window.Notify_window(8)

    def save_AAI(self):
        try:
            for i in range(0, 20, 2):
                if self.user == self.df['Users'].iloc[i]:  ##find user
                    self.data[1] = self.mode
                    if int(self.entry_Lowerlim.get()) in range(45, 66):
                        self.df[self.df['Users'].iloc[i], 'AAI Lower Rate Limit'] = int(self.entry_Lowerlim.get())
                        self.data[2] = int(self.entry_Lowerlim.get())
                    else:
                        success = False
                    if int(self.entry_Upperlim.get()) in range(120, 151):
                        self.df[self.df['Users'].iloc[i], 'AAI Upper Rate Limit'] = int(self.entry_Upperlim.get())
                        self.data[3] = int(self.entry_Upperlim.get())
                    else:
                        success = False
                    if int(self.entry_Pulse_Width.get()) in range(1, 11):
                        self.df[self.df['Users'].iloc[i], 'AAI Pulse Width'] = int(self.entry_Pulse_Width.get())
                        self.data[11] = int(self.entry_Pulse_Width.get())
                    else:
                        success = False
                    if int(self.entry_AV_Amp.get()) in range(50, 101):
                        self.df[self.df['Users'].iloc[i], 'AAI Atrial Amplitude'] = int(self.entry_AV_Amp.get())
                        self.data[10] = int(self.entry_AV_Amp.get())
                    else:
                        success = False
                    if int(self.entry_AV_Sens.get()) >= 65 and int(self.entry_AV_Sens.get()) <= 70:
                        self.df[self.df['Users'].iloc[i], 'AAI Atrial Sensitivity'] = int(self.entry_AV_Sens.get())
                        self.data[12] = int(self.entry_AV_Sens.get())
                    else:
                        success = False
                    if int(self.entry_ARP.get()) >= 150 and int(self.entry_ARP.get()) <= 300:
                        self.df[self.df['Users'].iloc[i], 'AAI VRP'] = int(self.entry_ARP.get())
                        self.data[14] = int(self.entry_ARP.get())
                    else:
                        success = False
                    if int(self.entry_Rate_Smooth.get()) >= 0 and int(self.entry_Rate_Smooth.get()) <= 100:
                        self.df[self.df['Users'].iloc[i], 'AAI Rate Smoothing'] = int(self.entry_Rate_Smooth.get())
                        self.data[16] = int(self.entry_Rate_Smooth.get())
                    else:
                        success = False
                    #if int(self.entry_BPM.get()) >= int(self.entry_Lowerlim.get()) and int(self.entry_BPM.get()) <= int(self.entry_Upperlim.get()):
                     #   self.df[self.df['Users'].iloc[i], 'AAI BPM'] = int(self.entry_BPM.get())
                       # self.data[4] = int(self.entry_BPM.get())
                    #else:
                     #   success = False
                    if success == True:
                        self.writeParameters()
                        ex.saveDataFrame(self.df)
                    else:
                        Notifiy_Window.Notify_window(8)
            ##lower rate limit, upper rate limit, pulsewidth, ventrical amplitude
        except ValueError:
            Notifiy_Window.Notify_window(8)

    def save_DOO(self):
        try:
            for i in range(0, 20, 2):
                if self.user == self.df['Users'].iloc[i]:  ##find user
                    self.data[1] = self.mode
                    if int(self.entry_Lowerlim.get()) in range(45, 66):
                        self.df[self.df['Users'].iloc[i], 'DOO Lower Rate Limit'] = int(self.entry_Lowerlim.get())
                        self.data[2] = int(self.entry_Lowerlim.get())
                    else:
                        success = False
                    if int(self.entry_Upperlim.get()) in range(120, 151):
                        self.df[self.df['Users'].iloc[i], 'DOO Upper Rate Limit'] = int(self.entry_Upperlim.get())
                        self.data[3] = int(self.entry_Upperlim.get())
                    else:
                        success = False
                    if int(self.entry_Pulse_Width.get()) in range(1, 11):
                        self.df[self.df['Users'].iloc[i], 'DOO Ventrical Pulse Width'] = int(self.entry_Pulse_Width.get())
                        self.data[11] = int(self.entry_Pulse_Width.get())
                    else:
                        success = False
                    if int(self.entry_AV_Amp.get()) in range(50, 101):
                        self.df[self.df['Users'].iloc[i], 'DOO Ventrical Amplitude'] = int(self.entry_AV_Amp.get())
                        self.data[10] = int(self.entry_AV_Amp.get())
                        self.data[9] = int(self.entry_AV_Amp.get())
                    else:
                        success = False
                    #if int(self.entry_AV_Amp.get()) in range(50, 101):
                        #self.df[self.df['Users'].iloc[i], 'DOO Atrial Amplitude'] = int(self.entry_AV_Amp.get())
                    i#f int(self.entry_Pulse_Width.get()) in range(1, 11):
                        #self.df[self.df['Users'].iloc[i], 'DOO Atrial Pulse Width'] = int(self.entry_Pulse_Width.get())
                    if int(self.entry_AV_del.get()) >= 70 and int(self.entry_AV_del.get()) <= 300:
                        self.df[self.df['Users'].iloc[i], 'DOO Fixed AV Delay'] = int(self.entry_AV_del.get())
                        self.data[6] = int(self.entry_AV_del.get())
                    else:
                        success = False
                    #if int(self.entry_BPM.get()) >= int(self.entry_Lowerlim.get()) and int(self.entry_BPM.get()) <= int(self.entry_Upperlim.get()):
                     #   self.df[self.df['Users'].iloc[i], 'DOO BPM'] = int(self.entry_BPM.get())
                      #  self.data[4] = int(self.entry_BPM.get())
                    #else:
                     #   success = False
                    if success == True:
                        self.writeParameters()
                        ex.saveDataFrame(self.df)
                    else:
                        Notifiy_Window.Notify_window(8)
            ##lower rate limit, upper rate limit, pulsewidth, ventrical amplitude
        except ValueError:
            Notifiy_Window.Notify_window(8)
        # save parameters
    def save_AOOR(self):
        try:
            for i in range(0, 20, 2):
                if self.user == self.df['Users'].iloc[i]:  ##find user
                    self.data[1] = self.mode
                    if int(self.entry_Lowerlim.get()) in range(45, 66):
                        self.df[self.df['Users'].iloc[i], 'AOOR Lower Rate Limit'] = int(self.entry_Lowerlim.get())
                        self.data[2] = int(self.entry_Lowerlim.get())
                    else:
                        success = False
                    if int(self.entry_Upperlim.get()) in range(120, 151):
                        self.df[self.df['Users'].iloc[i], 'AOOR Upper Rate Limit'] = int(self.entry_Upperlim.get())
                        self.data[3] = int(self.entry_Upperlim.get())
                    else:
                        success = False
                    if int(self.entry_Pulse_Width.get()) in range(1, 11):
                        self.df[self.df['Users'].iloc[i], 'AOOR Pulse Width'] = int(self.entry_Pulse_Width.get())
                        self.data[11] = int(self.entry_Pulse_Width.get())
                    else:
                        success = False
                    if int(self.entry_AV_Amp.get()) in range(50, 101):
                        self.df[self.df['Users'].iloc[i], 'AOOR Atrial Amplitude'] = int(self.entry_AV_Amp.get())
                        self.data[9] = int(self.entry_AV_Amp.get())
                    else:
                        success = False
                    if int(self.entry_Act_Thres.get()) > 10:
                        self.df[self.df['Users'].iloc[i], 'AOOR Activity Threshold'] = int(self.entry_Act_Thres.get())
                        self.data[20] = int(self.entry_Act_Thres.get())
                    else:
                        success = False
                    if int(self.entry_React_Time.get()) >= 10 and int(self.entry_React_Time.get()) <= 15:
                        self.df[self.df['Users'].iloc[i], 'AOOR Reaction Time'] = int(self.entry_React_Time.get())
                        self.data[21] = int(self.entry_React_Time.get())
                    else:
                        success = False
                    if int(self.entry_Resp_Fact.get()) >= 1 and int(self.entry_Resp_Fact.get()) <= 16:
                        self.df[self.df['Users'].iloc[i], 'AOOR Response Factor'] = int(self.entry_Resp_Fact.get())
                        self.data[22] = int(self.entry_Resp_Fact.get())
                    else:
                        success = False
                    if int(self.entry_Recv_Time.get()) >= 2 and int(self.entry_Recv_Time.get()) <= 16:
                        self.df[self.df['Users'].iloc[i], 'AOOR Recovery Time'] = int(self.entry_Recv_Time.get())
                        self.data[23] = int(self.entry_Recv_Time.get())
                    else:
                        success = False
                    if int(self.entry_AV_Sensor_Rate.get()) in range(50, 176):
                        self.df[self.df['Users'].iloc[i], 'AOOR Sensor Rate'] = int(self.entry_AV_Sensor_Rate.get())
                        self.data[5] = int(self.entry_AV_Sensor_Rate.get())
                    else:
                        success = False
                    #if int(self.entry_BPM.get()) >= int(self.entry_Lowerlim.get()) and int(self.entry_BPM.get()) <= int(self.entry_Upperlim.get()):
                     #   self.df[self.df['Users'].iloc[i], 'AOOR BPM'] = int(self.entry_BPM.get())
                      #  self.data[4] = int(self.entry_BPM.get())
                    #else:
                     #   success = False
                    if success == True:
                        self.writeParameters()
                        ex.saveDataFrame(self.df)
                    else:
                        Notifiy_Window.Notify_window(8)

            ##lower rate limit, upper rate limit, pulsewidth, ventrical amplitude
        except ValueError:
            Notifiy_Window.Notify_window(8)
        ##save parameters

    def save_AAIR(self):
        try:
            for i in range(0, 20, 2):
                if self.user == self.df['Users'].iloc[i]:  ##find user
                    self.data[1] = self.mode
                    if int(self.entry_Lowerlim.get()) in range(45, 66):
                        self.df[self.df['Users'].iloc[i], 'AAIR Lower Rate Limit'] = int(self.entry_Lowerlim.get())
                        self.data[2] = int(self.entry_Lowerlim.get())
                    else:
                        success = False
                    if int(self.entry_Upperlim.get()) in range(120, 151):
                        self.df[self.df['Users'].iloc[i], 'AAIR Upper Rate Limit'] = int(self.entry_Upperlim.get())
                        self.data[3] = int(self.entry_Upperlim.get())
                    else:
                        success = False
                    if int(self.entry_Pulse_Width.get()) in range(1, 11):
                        self.df[self.df['Users'].iloc[i], 'AAIR Pulse Width'] = int(self.entry_Pulse_Width.get())
                        self.data[11] = int(self.entry_Pulse_Width.get())
                    else:
                        success = False
                    if int(self.entry_AV_Amp.get()) in range(50, 101):
                        self.df[self.df['Users'].iloc[i], 'AAIR Atrial Amplitude'] = int(self.entry_AV_Amp.get())
                        self.data[9] = int(self.entry_AV_Amp.get())
                    else:
                        success = False
                    if int(self.entry_AV_Sensor_Rate.get()) >= 65 and int(self.entry_AV_Sensor_Rate.get()) <= 70:
                        self.df[self.df['Users'].iloc[i], 'AAIR Sensor Rate'] = int(self.entry_AV_Sensor_Rate.get())
                        self.data[5] = int(self.entry_AV_Sensor_Rate.get())
                    else:
                        success = False
                    if int(self.entry_AV_Sens.get()) in range(1, 11):
                        self.df[self.df['Users'].iloc[i], 'AAIR Atrial Sensitivity'] = int(self.entry_AV_Sens.get())
                        self.data[12] = int(self.entry_AV_Sens.get())
                    else:
                        success = False
                    if int(self.entry_Rate_Smooth()) in range(0, 101):
                        self.df[self.df['Users'].iloc[i], 'AAIR Rate Smoothing'] = int(self.entry_Rate_Smooth.get())
                        self.data[16] = int(self.entry_Rate_Smooth.get())
                    else:
                        success = False
                    if int(self.entry_Act_Thres.get()) > 10:
                        self.df[self.df['Users'].iloc[i], 'AAIR Activity Threshold'] = int(self.entry_Act_Thres.get())
                        self.data[20] = int(self.entry_Act_Thres.get())
                    else:
                        success = False
                    if int(self.entry_React_Time.get()) >= 10 and int(self.entry_React_Time.get()) <= 15:
                        self.df[self.df['Users'].iloc[i], 'AAIR Reaction Time'] = int(self.entry_React_Time.get())
                        self.data[21] = int(self.entry_React_Time.get())
                    else:
                        success = False
                    if int(self.entry_Resp_Fact.get()) >= 1 and int(self.entry_Resp_Fact.get()) <= 16:
                        self.df[self.df['Users'].iloc[i], 'AAIR Response Factor'] = int(self.entry_Resp_Fact.get())
                        self.data[22] = int(self.entry_Resp_Fact.get())
                    else:
                        success = False
                    if int(self.entry_Recv_Time.get()) >= 2 and int(self.entry_Recv_Time.get()) <= 16:
                        self.df[self.df['Users'].iloc[i], 'AAIR Recovery Time'] = int(self.entry_Recv_Time.get())
                        self.data[23] = int(self.entry_Recv_Time.get())
                    else:
                        success = False
                    if int(self.entry_ARP.get()) >= 150 and int(self.entry_ARP.get()) <= 300:
                        self.df[self.df['Users'].iloc[i], 'AAIR ARP'] = int(self.entry_ARP.get())
                        self.data[14] = int(self.entry_ARP.get())
                    else:
                        success = False
                  #  if int(self.entry_BPM.get()) >= int(self.entry_Lowerlim.get()) and int(self.entry_BPM.get()) <= int(self.entry_Upperlim.get()):
                   #     self.df[self.df['Users'].iloc[i], 'AAIR BPM'] = int(self.entry_BPM.get())
                    #    self.data[4] = int(self.entry_BPM.get())
                    #:
                     #   success = False
                    if success == True:
                        self.writeParameters()
                        ex.saveDataFrame(self.df)
                    else:
                        Notifiy_Window.Notify_window(8)
            ##lower rate limit, upper rate limit, pulsewidth, ventrical amplitude
        except ValueError:
            Notifiy_Window.Notify_window(8)
        ##save parameters
    def save_VOOR(self):
        try:
            for i in range(0, 20, 2):
                if self.user == self.df['Users'].iloc[i]:  ##find user
                    self.data[1] = self.mode
                    if int(self.entry_Lowerlim.get()) in range(45, 66):
                        self.df[self.df['Users'].iloc[i], 'VOOR Lower Rate Limit'] = int(self.entry_Lowerlim.get())
                        self.data[2] = int(self.entry_Lowerlim.get())
                    else:
                        success = False
                    if int(self.entry_Upperlim.get()) in range(120, 151):
                        self.df[self.df['Users'].iloc[i], 'VOOR Upper Rate Limit'] = int(self.entry_Upperlim.get())
                        self.data[3] = int(self.entry_Upperlim.get())
                    else:
                        success = False
                    if int(self.entry_Pulse_Width.get()) in range(1, 11):
                        self.df[self.df['Users'].iloc[i], 'VOOR Pulse Width'] = int(self.entry_Pulse_Width.get())
                        self.data[11] = int(self.entry_Pulse_Width.get())
                    else:
                        success = False
                    if int(self.entry_AV_Amp.get()) in range(50, 101):
                        self.df[self.df['Users'].iloc[i], 'VOOR Ventrical Amplitude'] = int(self.entry_AV_Amp.get())
                        self.data[9] = int(self.entry_AV_Amp.get())
                    else:
                        success = False
                    if int(self.entry_Act_Thres.get()) > 10:
                        self.df[self.df['Users'].iloc[i], 'VOOR Activity Threshold'] = int(self.entry_Act_Thres.get())
                        self.data[20] = int(self.entry_Act_Thres.get())
                    else:
                        success = False
                    if int(self.entry_React_Time.get()) >= 10 and int(self.entry_React_Time.get()) <= 15:
                        self.df[self.df['Users'].iloc[i], 'VOOR Reaction Time'] = int(self.entry_React_Time.get())
                        self.data[21] = int(self.entry_React_Time.get())
                    else:
                        success = False
                    if int(self.entry_Resp_Fact.get()) >= 1 and int(self.entry_Resp_Fact.get()) <= 16:
                        self.df[self.df['Users'].iloc[i], 'VOOR Response Factor'] = int(self.entry_Resp_Fact.get())
                        self.data[22] = int(self.entry_Resp_Fact.get())
                    else:
                        success = False
                    if int(self.entry_Recv_Time.get()) >= 2 and int(self.entry_Recv_Time.get()) <= 16:
                        self.df[self.df['Users'].iloc[i], 'VOOR Recovery Time'] = int(self.entry_Recv_Time.get())
                        self.data[23] = int(self.entry_Recv_Time.get())
                    else:
                        success = False
                    if int(self.entry_AV_Sensor_Rate.get()) in range(50, 176):
                        self.df[self.df['Users'].iloc[i], 'VOOR Sensor Rate'] = int(self.entry_AV_Sensor_Rate.get())
                        self.data[5] = int(self.entry_AV_Sensor_Rate.get())
                    else:
                        success = False
                   # if int(self.entry_BPM.get()) >= int(self.entry_Lowerlim.get()) and int(self.entry_BPM.get()) <= int(self.entry_Upperlim.get()):
                    #    self.df[self.df['Users'].iloc[i], 'VOOR BPM'] = int(self.entry_BPM.get())
                     #   self.data[4] = int(self.entry_BPM.get())
                    #else:
                     #   success = False
                    if success == True:
                        self.writeParameters()
                        ex.saveDataFrame(self.df)
                    else:
                        Notifiy_Window.Notify_window(8)

            ##lower rate limit, upper rate limit, pulsewidth, ventrical amplitude
        except ValueError:
            Notifiy_Window.Notify_window(8)
        ##save parameters
    def save_VVIR(self):
        try:
            for i in range(0, 20, 2):
                if self.user == self.df['Users'].iloc[i]:  ##find user
                    self.data[1] = self.mode
                    if int(self.entry_Lowerlim.get()) in range(45, 66):
                        self.df[self.df['Users'].iloc[i], 'VVIR Lower Rate Limit'] = int(self.entry_Lowerlim.get())
                        self.data[2] = int(self.entry_Lowerlim.get())
                    else:
                        success = False
                    if int(self.entry_Upperlim.get()) in range(120, 151):
                        self.df[self.df['Users'].iloc[i], 'VVIR Upper Rate Limit'] = int(self.entry_Upperlim.get())
                        self.data[3] = int(self.entry_Upperlim.get())
                    else:
                        success = False
                    if int(self.entry_Pulse_Width.get()) in range(1, 11):
                        self.df[self.df['Users'].iloc[i], 'VVIR Pulse Width'] = int(self.entry_Pulse_Width.get())
                        self.data[11] = int(self.entry_Pulse_Width.get())
                    else:
                        success = False
                    if int(self.entry_AV_Amp.get()) in range(50, 101):
                        self.df[self.df['Users'].iloc[i], 'VVIR Ventrical Amplitude'] = int(self.entry_AV_Amp.get())
                        self.data[10] = int(self.entry_AV_Amp.get())
                    else:
                        success = False
                    if int(self.entry_AV_Sensor_Rate.get()) >= 65 and int(self.entry_AV_Sensor_Rate.get()) <= 70:
                        self.df[self.df['Users'].iloc[i], 'VVIR Sensor Rate'] = int(self.entry_AV_Sensor_Rate.get())
                        self.data[5] = int(self.entry_AV_Sensor_Rate.get())
                    else:
                        success = False
                    if int(self.entry_AV_Sens.get()) in range(1, 11):
                        self.df[self.df['Users'].iloc[i], 'VVIR Ventrical Sensitivity'] = int(self.entry_AV_Sens.get())
                        self.data[13] = int(self.entry_AV_Sens.get())
                    else:
                        success = False
                    if int(self.entry_Rate_Smooth()) in range(0, 101):
                        self.df[self.df['Users'].iloc[i], 'VVIR Rate Smoothing'] = int(self.entry_Rate_Smooth.get())
                        self.data[16] = int(self.entry_Rate_Smooth.get())
                    else:
                        success = False
                    if int(self.entry_Act_Thres.get()) > 10:
                        self.df[self.df['Users'].iloc[i], 'VVIR Activity Threshold'] = int(self.entry_Act_Thres.get())
                        self.data[20] = int(self.entry_Act_Thres.get())
                    else:
                        success = False
                    if int(self.entry_React_Time.get()) >= 10 and int(self.entry_React_Time.get()) <= 15:
                        self.df[self.df['Users'].iloc[i], 'VVIR Reaction Time'] = int(self.entry_React_Time.get())
                        self.data[21] = int(self.entry_React_Time.get())
                    else:
                        success = False
                    if int(self.entry_Resp_Fact.get()) >= 1 and int(self.entry_Resp_Fact.get()) <= 16:
                        self.df[self.df['Users'].iloc[i], 'VVIR Response Factor'] = int(self.entry_Resp_Fact.get())
                        self.data[22] = int(self.entry_Resp_Fact.get())
                    else:
                        success = False
                    if int(self.entry_Recv_Time.get()) >= 2 and int(self.entry_Recv_Time.get()) <= 16:
                        self.df[self.df['Users'].iloc[i], 'VVIR Recovery Time'] = int(self.entry_Recv_Time.get())
                        self.data[23] = int(self.entry_Recv_Time.get())
                    else:
                        success = False
                    if int(self.entry_VRP.get()) >= 150 and int(self.entry_VRP.get()) <= 300:
                        self.df[self.df['Users'].iloc[i], 'VVIR VRP'] = int(self.entry_VRP.get())
                        self.data[15] = int(self.entry_VRP.get())
                    else:
                        success = False
                    #if int(self.entry_BPM.get()) >= int(self.entry_Lowerlim.get()) and int(self.entry_BPM.get()) <= int(self.entry_Upperlim.get()):
                     #   self.df[self.df['Users'].iloc[i], 'VVIR BPM'] = int(self.entry_BPM.get())
                      #  self.data[4] = int(self.entry_BPM.get())
                    #else:
                     #   success = False
                    if success == True:
                        self.writeParameters()
                        ex.saveDataFrame(self.df)
                    else:
                        Notifiy_Window.Notify_window(8)
            ##lower rate limit, upper rate limit, pulsewidth, ventrical amplitude
        except ValueError:
            Notifiy_Window.Notify_window(8)
        ##save parameters
    def save_DOOR(self):
        try:
            for i in range(0, 20, 2):
                if self.user == self.df['Users'].iloc[i]:  ##find user
                    self.data[1] = self.mode
                    if int(self.entry_Lowerlim.get()) in range(45, 66):
                        self.df[self.df['Users'].iloc[i], 'DOOR Lower Rate Limit'] = int(self.entry_Lowerlim.get())
                        self.data[2] = int(self.entry_Lowerlim.get())
                    else:
                        success = False
                    if int(self.entry_Upperlim.get()) in range(120, 151):
                        self.df[self.df['Users'].iloc[i], 'DOOR Upper Rate Limit'] = int(self.entry_Upperlim.get())
                        self.data[3] = int(self.entry_Upperlim.get())
                    else:
                        success = False
                    if int(self.entry_Pulse_Width.get()) in range(1, 11):
                        self.df[self.df['Users'].iloc[i], 'DOOR Ventrical Pulse Width'] = int(self.entry_Pulse_Width.get())
                        self.data[11] = int(self.entry_Pulse_Width.get())
                    else:
                        success = False
                    if int(self.entry_AV_Amp.get()) in range(50, 101):
                        self.df[self.df['Users'].iloc[i], 'DOOR Ventrical Amplitude'] = int(self.entry_AV_Amp.get())
                        self.data[10] = int(self.entry_AV_Amp.get())
                    else:
                        success = False
                    #if int(self.entry_AV_Amp.get()) >= 65 and int(self.entry_AV_Amp.get()) <= 70:
                        #self.df[self.df['Users'].iloc[i], 'DOOR Atrial Amplitude'] = int(self.entry_AV_Amp.get())
                    #if int(self.entry_Pulse_Width.get()) in range(1, 11):
                        #self.df[self.df['Users'].iloc[i], 'DOOR Atrial Pulse Width'] = int(self.entry_Pulse_Width.get())
                    if int(self.entry_AV_del.get()) >= 70 and int(self.entry_AV_del.get()) <= 300:
                        self.df[self.df['Users'].iloc[i], 'DOOR Fixed AV Delay'] = int(self.entry_AV_del.get())
                        self.data[6] = int(self.entry_AV_del.get())
                    else:
                        success = False
                    if int(self.entry_Rate_Smooth()) in range(0, 101):
                        self.df[self.df['Users'].iloc[i], 'DOOR Rate Smoothing'] = int(self.entry_Rate_Smooth.get())
                        self.data[16] = int(self.entry_Rate_Smooth.get())
                    else:
                        success = False
                    if int(self.entry_Act_Thres.get()) > 10:
                        self.df[self.df['Users'].iloc[i], 'DOOR Activity Threshold'] = int(self.entry_Act_Thres.get())
                        self.data[20] = int(self.entry_Act_Thres.get())
                    else:
                        success = False
                    if int(self.entry_React_Time.get()) >= 10 and int(self.entry_React_Time.get()) <= 15:
                        self.df[self.df['Users'].iloc[i], 'DOOR Reaction Time'] = int(self.entry_React_Time.get())
                        self.data[21] = int(self.entry_React_Time.get())
                    else:
                        success = False
                    if int(self.entry_Resp_Fact.get()) >= 1 and int(self.entry_Resp_Fact.get()) <= 16:
                        self.df[self.df['Users'].iloc[i], 'DOOR Response Factor'] = int(self.entry_Resp_Fact.get())
                        self.data[22] = int(self.entry_Resp_Fact.get())
                    else:
                        success = False
                    if int(self.entry_Recv_Time.get()) >= 2 and int(self.entry_Recv_Time.get()) <= 16:
                        self.df[self.df['Users'].iloc[i], 'DOOR Recovery Time'] = int(self.entry_Recv_Time.get())
                        self.data[23] = int(self.entry_Recv_Time.get())
                    else:
                        success = False
                   # if int(self.entry_BPM.get()) >= int(self.entry_Lowerlim.get()) and int(self.entry_BPM.get()) <= int(self.entry_Upperlim.get()):
                    #    self.df[self.df['Users'].iloc[i], 'DOOR BPM'] = int(self.entry_BPM.get())
                     #   self.data[4] = int(self.entry_BPM.get())
                    #else:
                     #   success = False
                    if success == True:
                        self.writeParameters()
                        ex.saveDataFrame(self.df)
                    else:
                        Notifiy_Window.Notify_window(8)

            ##lower rate limit, upper rate limit, pulsewidth, ventrical amplitude
        except ValueError:
            Notifiy_WindowNotify_window(8)
        ##save parameters
    def save_DDDR(self):
        try:
            for i in range(0, 20, 2):
                if self.user == self.df['Users'].iloc[i]:  ##find user
                    self.data[1] = self.mode
                    if int(self.entry_Lowerlim.get()) in range(45, 66):
                        self.df[self.df['Users'].iloc[i], 'DDDR Lower Rate Limit'] = int(self.entry_Lowerlim.get())
                        self.data[2] = int(self.entry_Lowerlim.get())
                    else:
                        success = False
                    if int(self.entry_Upperlim.get()) in range(120, 151):
                        self.df[self.df['Users'].iloc[i], 'DDDR Upper Rate Limit'] = int(self.entry_Upperlim.get())
                        self.data[3] = int(self.entry_Upperlim.get())
                    else:
                        success = False
                    if int(self.entry_Pulse_Width.get()) in range(1, 11):
                        self.df[self.df['Users'].iloc[i], 'DDDR Ventrical Pulse Width'] = int(self.entry_Pulse_Width.get())
                        self.data[11] = int(self.entry_Pulse_Width.get())
                    else:
                        success = False
                    if int(self.entry_AV_Amp.get()) in range(50, 101):
                        self.df[self.df['Users'].iloc[i], 'DDDR Ventrical Amplitude'] = int(self.entry_AV_Amp.get())
                        self.data[10] = int(self.entry_AV_Amp.get())
                        self.data[9] = int(self.entry_AV_Amp.get())
                    else:
                        success = False
                    #if int(self.entry_AV_Amp.get()) >= 65 and int(self.entry_AV_Amp.get()) <= 70:
                     #   self.df[self.df['Users'].iloc[i], 'DOOR Atrial Amplitude'] = int(self.entry_AV_Amp.get())
                   # if int(self.entry_Pulse_Width.get()) in range(1, 11):
                    #    self.df[self.df['Users'].iloc[i], 'DOOR Atrial Pulse Width'] = int(self.entry_Pulse_Width.get())
                    if int(self.entry_AV_del.get()) >= 70 and int(self.entry_AV_del.get()) <= 300:
                        self.df[self.df['Users'].iloc[i], 'DDDR Fixed AV Delay'] = int(self.entry_AV_del.get())
                        self.data[6] = int(self.entry_AV_del.get())
                    else:
                        success = False
                    if int(self.entry_Rate_Smooth()) in range(0, 101):
                        self.df[self.df['Users'].iloc[i], 'DDDR Rate Smoothing'] = int(self.entry_Rate_Smooth.get())
                        self.data[16] = int(self.entry_Rate_Smooth.get())
                    else:
                        success = False
                    if int(self.entry_Act_Thres.get()) > 10:
                        self.df[self.df['Users'].iloc[i], 'DDDR Activity Threshold'] = int(self.entry_Act_Thres.get())
                        self.data[20] = int(self.entry_Act_Thres.get())
                    else:
                        success = False
                    if int(self.entry_React_Time.get()) >= 10 and int(self.entry_React_Time.get()) <= 15:
                        self.df[self.df['Users'].iloc[i], 'DDDR Reaction Time'] = int(self.entry_React_Time.get())
                        self.data[21] = int(self.entry_React_Time.get())
                    else:
                        success = False
                    if int(self.entry_Resp_Fact.get()) >= 1 and int(self.entry_Resp_Fact.get()) <= 16:
                        self.df[self.df['Users'].iloc[i], 'DDDR Response Factor'] = int(self.entry_Resp_Fact.get())
                        self.data[22] = int(self.entry_Resp_Fact.get())
                    else:
                        success = False
                    if int(self.entry_Recv_Time.get()) >= 2 and int(self.entry_Recv_Time.get()) <= 16:
                        self.df[self.df['Users'].iloc[i], 'DDDR Recovery Time'] = int(self.entry_Recv_Time.get())
                        self.data[23] = int(self.entry_Recv_Time.get())
                    else:
                        success = False
                    if int(self.entry_VRP.get()) >= 150 and int(self.entry_VRP.get()) <= 300:
                        self.df[self.df['Users'].iloc[i], 'DDDR VRP'] = int(self.entry_VRP.get())
                        self.data[15] = int(self.entry_VRP.get())
                        self.data[14] = int(self.entry_VRP.get())
                    else:
                        success = False
                    #if int(self.entry_ARP.get()) in range(150, 301):
                    #    self.df[self.df['Users'].iloc[i], 'DDDR ARP'] = int(self.entry_ARP.get())
                    if int(self.entry_AV_Sensor_Rate.get()) in range(50, 176):
                        self.df[self.df['Users'].iloc[i], 'DDDR Sensor Rate'] = int(self.entry_AV_Sensor_Rate.get())
                        self.data[5] = int(self.entry_AV_Sensor_Rate.get())
                    else:
                        success = False
                    if int(self.entry_Dyn_AV_Delay.get()) in range(0, 2):
                        self.df[self.df['Users'].iloc[i], 'DDDR Dynamic AV Delay'] = int(self.entry_Dyn_AV_Delay.get())
                        self.data[7] = int(self.entry_Dyn_AV_Delay.get())
                    else:
                        success = False
                    if int(self.entry_AV_Delay_Off1.get()) in range(10, 101) or int(self.entry_AV_Delay_Off1.get()) == 0:
                        self.df[self.df['Users'].iloc[i], 'DDDR Sensed AV Delay Offset'] = int(self.entry_AV_Delay_Off1.get())
                        self.data[8] = int(self.entry_AV_Delay_Off1.get())
                    else:
                        success = False
                    if int(self.entry_AV_Sens.get()) in range(1, 11):
                        self.df[self.df['Users'].iloc[i], 'DDDR Ventrical Sensitivity'] = int(self.entry_AV_Sens.get())
                        self.data[12] = int(self.entry_AV_Sens.get())
                        self.data[13] = int(self.entry_AV_Sens.get())
                    else:
                        success = False
                    #if int(self.entry_AV_Sens.get()) in range(1, 11):
                        #self.df[self.df['Users'].iloc[i], 'DDDRR Atrial Sensitivity'] = int(self.entry_AV_Sens.get())
                    if int(self.entry_ATR_Fallback_Mode.get()) in range(0, 2):
                        self.df[self.df['Users'].iloc[i], 'DDDR ATR Fallback Mode'] = int(self.entry_ATR_Fallback_Mode.get())
                        self.df[18] = int(self.entry_ATR_Fallback_Mode.get())
                    else:
                        success = False
                    if int(self.entry_ATR_Fallback_time.get()) in range(1, 6):
                        self.df[self.df['Users'].iloc[i], 'DDDR ATR Fallback Time'] = int(self.entry_ATR_Fallback_time.get())
                        self.data[19] = int(self.entry_ATR_Fallback_time.get())
                    else:
                        success = False
                   # if int(self.entry_BPM.get()) >= int(self.entry_Lowerlim.get()) and int(self.entry_BPM.get()) <= int(self.entry_Upperlim.get()):
                    #    self.df[self.df['Users'].iloc[i], 'DDDR BPM'] = int(self.entry_BPM.get())
                     #   self.data[4] = int(self.entry_BPM.get())
                    #else:
                     #   success = False
                    if success == True:
                        self.writeParameters()
                        ex.saveDataFrame(self.df)
                    else:
                        Notifiy_Window.Notify_window(8)
        except ValueError:
            Notifiy_Window.Notify_window(8)
    ##save parameters

    def writeParameters(self):
        tosend = struct.pack('<BBBBBBHHBBBBHBBBHBdBBB', self.data[0], self.data[1], self.data[2], self.data[3], self.data[4],self.data[5],self.data[6],self.data[7],self.data[8],
                             self.data[9],self.data[10], self.data[11], self.data[12], self.data[13], self.data[14], self.data[15], self.data[16], self.data[17], self.data[18], self.data[19],
                             self.data[20], self.data[21])
        transList = [0]*len(tosend)
        i = 0
        while i < len(tosend):
            transList[i] = tosend[i]
            i += 1
        self.board.write(transList)

    def showVOO(self):
        #show old parameters
        for i in range(0, 20, 2):
            if self,df['Users'].iloc[i] == self.user:
                self.entry_Lowerlim.insert(self.df[self.df['Users'].iloc[i], 'VOO Lower Rate Limit'])
                self.entry_UpperLim.insert(self.df[self.df['Users'].iloc[i], 'VOO Upper Rate Limit'])
                self.entry_Pulse_Width.insert(self.df[self.df['Users'].iloc[i], 'VOO Pulse Width'])
                self.entry_AV_Amp.insert(self.df[self.df['Users'].iloc[i], 'VOO Ventrical Amplitude'])
                self.entry_BPM.insert(self.df[self.df['Users'].iloc[i], 'VOO BPM'])

    def showAOO(self):
        #show old parameters
        for i in range(0, 20, 2):
            if self, df['Users'].iloc[i] == self.user:
                self.entry_Lowerlim.insert(self.df[self.df['Users'].iloc[i], 'AOO Lower Rate Limit'])
                self.entry_UpperLim.insert(self.df[self.df['Users'].iloc[i], 'AOO Upper Rate Limit'])
                self.entry_Pulse_Width.insert(self.df[self.df['Users'].iloc[i], 'AOO Pulse Width'])
                self.entry_AV_Amp.insert(self.df[self.df['Users'].iloc[i], 'AOO Atrial Amplitude'])
                self.entry_BPM.insert(self.df[self.df['Users'].iloc[i], 'AOO BPM'])

    def showVVI(self):
        # show old parameters
        for i in range(0, 20, 2):
            if self, df['Users'].iloc[i] == self.user:
                self.entry_Lowerlim.insert(self.df[self.df['Users'].iloc[i], 'VVI Lower Rate Limit'])
                self.entry_UpperLimself.df.insert([self.df['Users'].iloc[i], 'VVI Upper Rate Limit'])
                self.entry_Pulse_Width.insert(self.df[self.df['Users'].iloc[i], 'VVI Pulse Width'])
                self.entry_AV_Amp.insert(self.df[self.df['Users'].iloc[i], 'VVI Ventrical Amplitude'])
                self.entry_AV_Sens.insert(self.df[self.df['Users'].iloc[i], 'VVI Ventrical Sensitivity'])
                self.entry_VRP.insert(self.df[self.df['Users'].iloc[i], 'VVI VRP'])
                self.entry_Rate_Smooth.insert(self.df[self.df['Users'].iloc[i], 'VVI Rate Smoothing'])
                self.entry_BPM.insert(self.df[self.df['Users'].iloc[i], 'VVI BPM'])

    def showAAI(self):
        # show old parameters
        for i in range(0, 20, 2):
            if self, df['Users'].iloc[i] == self.user:
                self.entry_Lowerlim.insert(self.df[self.df['Users'].iloc[i], 'AAI Lower Rate Limit'])
                self.entry_UpperLim.insert(self.df[self.df['Users'].iloc[i], 'AAI Upper Rate Limit'])
                self.entry_Pulse_Width.insert(self.df[self.df['Users'].iloc[i], 'AAI Pulse Width'])
                self.entry_AV_Amp.insert(self.df[self.df['Users'].iloc[i], 'AAI Atrial Amplitude'])
                self.entry_AV_Sens.insert(self.df[self.df['Users'].iloc[i], 'AAI Atrial Sensitivity'])
                self.entry_ARP.insert(self.df[self.df['Users'].iloc[i], 'AAI VRP'])
                self.entry_Rate_Smooth.insert(self.df[self.df['Users'].iloc[i], 'AAI Rate Smoothing'])
                self.entry_BPM.insert(self.df[self.df['Users'].iloc[i], 'AAI BPM'])

    def showDOO(self):
        # show old parameters
        for i in range(0, 20, 2):
            if self, df['Users'].iloc[i] == self.user:
                self.entry_Lowerlim.insert(self.df[self.df['Users'].iloc[i], 'DOO Lower Rate Limit'])
                self.entry_UpperLim.insert(self.df[self.df['Users'].iloc[i], 'DOO Upper Rate Limit'])
                self.entry_Pulse_Width.insert(self.df[self.df['Users'].iloc[i], 'DOO Ventrical Pulse Width'])
                self.entry_AV_Amp.insert(self.df[self.df['Users'].iloc[i], 'DOO Ventrical Amplitude'])
                self.entry_AV_del.insert(self.df[self.df['Users'].iloc[i], 'DOO Fixed AV Delay'])
                self.entry_BPM.insert(self.df[self.df['Users'].iloc[i], 'DOO BPM'])

    def showAOOR(self):
        # show old parameters
        for i in range(0, 20, 2):
            if self, df['Users'].iloc[i] == self.user:
                self.entry_Lowerlim.insert(self.df[self.df['Users'].iloc[i], 'AOOR Lower Rate Limit'])
                self.entry_UpperLim.insert(self.df[self.df['Users'].iloc[i], 'AOOR Upper Rate Limit'])
                self.entry_Pulse_Width.insert(self.df[self.df['Users'].iloc[i], 'AOOR Pulse Width'])
                self.entry_AV_Amp.insert(self.df[self.df['Users'].iloc[i], 'AOOR Atrial Amplitude'])
                self.entry_Rate_Smooth.insert(self.df[self.df['Users'].iloc[i], 'AOOR Rate Smoothing'])
                self.entry_Act_Thres.insert(self.df[self.df['Users'].iloc[i], 'AOOR Activity Threshold'])
                self.entry_React_Time.insert(self.df[self.df['Users'].iloc[i], 'AOOR Reaction Time'])
                self.entry_Resp_Fact.insert(self.df[self.df['Users'].iloc[i], 'AOOR Response Factor'])
                self.entry_Recv_Time.insert(self.df[self.df['Users'].iloc[i], 'AOOR Recovery Time'])
                self.entry_BPM.insert(self.df[self.df['Users'].iloc[i], 'AOOR BPM'])

    def showAAIR(self):
        #old
        for i in range(0, 20, 2):
            if self, df['Users'].iloc[i] == self.user:
                self.df[self.df['Users'].iloc[i], 'AAIR Lower Rate Limit'] = int(self.entry_Lowerlim.get())
                self.df[self.df['Users'].iloc[i], 'AAIR Upper Rate Limit'] = int(self.entry_UpperLim.get())
                self.df[self.df['Users'].iloc[i], 'AAIR Pulse Width'] = int(self.entry_Pulse_Width.get())
                self.df[self.df['Users'].iloc[i], 'AAIR Atrial Amplitude'] = int(self.entry_AV_Amp.get())
                self.df[self.df['Users'].iloc[i], 'AAIR Sensor Rate'] = int(self.entry_AV_Sensor_Rate.get())
                self.df[self.df['Users'].iloc[i], 'AAIR Atrial Sensitivity'] = int(self.entry_AV_Sens.get())
                self.df[self.df['Users'].iloc[i], 'AAIR Rate Smoothing'] = int(self.entry_Rate_Smooth.get())
                self.df[self.df['Users'].iloc[i], 'AAIR Activity Threshold'] = int(self.entry_Act_Thres.get())
                self.df[self.df['Users'].iloc[i], 'AAIR Reaction Time'] = int(self.entry_React_Time.get())
                self.df[self.df['Users'].iloc[i], 'AAIR Response Factor'] = int(self.entry_Resp_Fact.get())
                self.df[self.df['Users'].iloc[i], 'AAIR Recovery Time'] = int(self.entry_Recv_Time.get())
                self.df[self.df['Users'].iloc[i], 'AAIR ARP'] = int(self.entry_ARP.get())
                self.entry_BPM.insert(self.df[self.df['Users'].iloc[i], 'AAIR BPM'])

    def showVOOR(self):
        # show old parameters
        for i in range(0, 20, 2):
            if self, df['Users'].iloc[i] == self.user:
                self.entry_Lowerlim.insert(self.df[self.df['Users'].iloc[i], 'VOOR Lower Rate Limit'])
                self.entry_UpperLim.insert(self.df[self.df['Users'].iloc[i], 'VOOR Upper Rate Limit'])
                self.entry_Pulse_Width.insert(self.df[self.df['Users'].iloc[i], 'VOOR Pulse Width'])
                self.entry_AV_Amp.insert(self.df[self.df['Users'].iloc[i], 'VOOR Ventrical Amplitude'])
                self.entry_Act_Thres.insert(self.df[self.df['Users'].iloc[i], 'VOOR Activity Threshold'])
                self.entry_React_Time.insert(self.df[self.df['Users'].iloc[i], 'VOOR Reaction Time'])
                self.entry_Resp_Fact.insert(self.df[self.df['Users'].iloc[i], 'VOOR Response Factor'])
                self.entry_Recv_Time.insert(self.df[self.df['Users'].iloc[i], 'VOOR Recovery Time'])
                self.entry_AV_Sensor_Rate.insert(self.df[self.df['Users'].iloc[i], 'VOOR Sensor Rate'])
                self.entry_BPM.insert(self.df[self.df['Users'].iloc[i], 'VOOR BPM'])

    def showVVIR(self):
        #show old
        for i in range(0, 20, 2):
            if self, df['Users'].iloc[i] == self.user:
                self.entry_Lowerlim.insert(self.df[self.df['Users'].iloc[i], 'VVIR Lower Rate Limit'])
                self.entry_UpperLim.insert(self.df[self.df['Users'].iloc[i], 'VVIR Upper Rate Limit'])
                self.entry_Pulse_Width.insert(self.df[self.df['Users'].iloc[i], 'VVIR Pulse Width'])
                self.entry_AV_Amp.insert(self.df[self.df['Users'].iloc[i], 'VVIR Ventrical Amplitude'])
                self.entry_AV_Sensor_Rate.insert(self.df[self.df['Users'].iloc[i], 'VVIR Sensor Rate'])
                self.entry_AV_Sens.insert(self.df[self.df['Users'].iloc[i], 'VVIR Ventrical Sensitivity'])
                self.entry_Rate_Smooth.insert(self.df[self.df['Users'].iloc[i], 'VVIR Rate Smoothing'])
                self.entry_Act_Thres.insert(self.df[self.df['Users'].iloc[i], 'VVIR Activity Threshold'])
                self.entry_React_Time.insert(self.df[self.df['Users'].iloc[i], 'VVIR Reaction Time'])
                self.entry_Resp_Fact.insert(self.df[self.df['Users'].iloc[i], 'VVIR Response Factor'])
                self.entry_Recv_Time.insert(self.df[self.df['Users'].iloc[i], 'VVIR Recovery Time'])
                self.entry_VRP.insert(self.df[self.df['Users'].iloc[i], 'VVIR VRP'])
                self.entry_BPM.insert(self.df[self.df['Users'].iloc[i], 'VVIR BPM'])

    def showDOOR(self):
        #show old
        for i in range(0, 20, 2):
            if self, df['Users'].iloc[i] == self.user:
                self.entry_Lowerlim.insert(self.df[self.df['Users'].iloc[i], 'DOOR Lower Rate Limit'])
                self.entry_UpperLim.insert(self.df[self.df['Users'].iloc[i], 'DOOR Upper Rate Limit'])
                self.entry_Pulse_Width.insert(self.df[self.df['Users'].iloc[i], 'DOOR Ventrical Pulse Width'])
                self.entry_AV_Amp.insert(self.df[self.df['Users'].iloc[i], 'DOOR Ventrical Amplitude'])
                self.entry_AV_del.insert(self.df[self.df['Users'].iloc[i], 'DOOR Fixed AV Delay'])
                self.entry_Rate_Smooth.insert(self.df[self.df['Users'].iloc[i], 'DOOR Rate Smoothing'])
                self.entry_Act_Thres.insert(self.df[self.df['Users'].iloc[i], 'DOOR Activity Threshold'])
                self.entry_React_Time.insert(self.df[self.df['Users'].iloc[i], 'DOOR Reaction Time'])
                self.entry_Resp_Fact.insert(self.df[self.df['Users'].iloc[i], 'DOOR Response Factor'])
                self.entry_Recv_Time.insert(self.df[self.df['Users'].iloc[i], 'DOOR Recovery Time'])
                self.entry_BPM.insert(self.df[self.df['Users'].iloc[i], 'DOOR BPM'])

    def showDDDR(self):
        for i in range(0, 20, 2):
            if self, df['Users'].iloc[i] == self.user:
                self.entry_Lowerlim.insert(self.df[self.df['Users'].iloc[i], 'DDDR Lower Rate Limit'])
                self.entry_UpperLim.insert(self.df[self.df['Users'].iloc[i], 'DDDR Upper Rate Limit'])
                self.entry_Pulse_Width.insert(self.df[self.df['Users'].iloc[i], 'DDDR Ventrical Pulse Width'])
                self.entry_AV_Amp.insert(self.df[self.df['Users'].iloc[i], 'DDDR Ventrical Amplitude'])
                self.entry_AV_del.insert(self.df[self.df['Users'].iloc[i], 'DDDR Fixed AV Delay'])
                self.entry_Rate_Smooth.insert(self.df[self.df['Users'].iloc[i], 'DDDR Rate Smoothing'])
                self.entry_Act_Thres.insert(self.df[self.df['Users'].iloc[i], 'DDDR Activity Threshold'])
                self.entry_React_Time.insert(self.df[self.df['Users'].iloc[i], 'DDDR Reaction Time'])
                self.entry_Resp_Fact.insert(self.df[self.df['Users'].iloc[i], 'DDDR Response Factor'])
                self.entry_Recv_Time.insert(self.df[self.df['Users'].iloc[i], 'DDDR Recovery Time'])
                self.entry_VRP.insert(self.df[self.df['Users'].iloc[i], 'DDDR VRP'])
                self.entry_AV_Sensor_Rate.insert(self.df[self.df['Users'].iloc[i], 'DDDR Sensor Rate'])
                self.entry_Dyn_AV_Delay.insert(self.df[self.df['Users'].iloc[i], 'DDDR Dynamic AV Delay'])
                self.entry_AV_Delay_Off1.insert(self.df[self.df['Users'].iloc[i], 'DDDR Sensed AV Delay Offset'])
                self.entry_AV_Sens.insert(self.df[self.df['Users'].iloc[i], 'DDDR Ventrical Sensitivity'])
                self.entry_ATR_Fallback_Mode.insert(self.df[self.df['Users'].iloc[i], 'DDDR ATR Fallback Mode'])
                self.entry_ATR_Fallback_time.insert(self.df[self.df['Users'].iloc[i], 'DDDR ATR Fallback Time'])
                self.entry_BPM.insert(self.df[self.df['Users'].iloc[i], 'DDDR BPM'])

def openSerial():
    s = Serial()
    s.port = 'COM6'
    s.baudrate = 115200
    s.timeout = 0.5
    s.dtr = 0
    s.open()
    state = s.isOpen()
    return s


