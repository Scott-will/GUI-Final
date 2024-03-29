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
# import Serial_com            #
# import time                   #
#import panda as pd             #
#import Excel_Handling as ex    #
#################################
from tkinter import *
import tkinter as tk
import Pacing_Screen
import Notifiy_Window
import Excel_Handling as ex
import pandas as pd
import struct
from serial import Serial
import Serial_com as sc
import Lists
import numpy




class Parameter_Window:
    def __init__(self, master, mode, user, df):
        self.frame_root = Frame(master, width=1500, height=500)
        self.frame_root.pack()
        self.mode = mode
        self.user = user
        self.master = master
        self.df = df
        self.data = [22, 9, 60, 150, 250, 75, 10, 70, 250, 1.5, 20, 2, 8]
        self.board = sc.s
        print(sc.s)
        #self.boardID = 22
        #self.data[0] = 22

        if self.mode == 1:
            self.background_image = tk.PhotoImage(file="backgroundpacing1.png")
            self.label = Label(self.frame_root, image=self.background_image)
            self.label.image = self.background_image
            self.label.pack()
            # command's parameters are the x and y coordinates for the various widgets it creates
            self.common(125, 172, 125, 222, 30, 170, 30, 220, 300, 50, 300, 350, 300, 300, 300, 90, 340, 222, 270, 222, 300, 10)

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
            self.label_PVARP.place(x=290, y=172)

            self.entry_AV_Amp = Entry(self.frame_root)  # self.entry_AV_Amp, self.entry_Pulse_Width,
            self.entry_AV_Amp.place(x=125, y=270)
            self.entry_Pulse_Width = Entry(self.frame_root)
            self.entry_Pulse_Width.place(x=125, y=320)
            self.entry_AV_Sens = Entry(self.frame_root)
            self.entry_AV_Sens.place(x=125, y=370)
            self.entry_ARP = Entry(self.frame_root)
            self.entry_ARP.place(x=125, y=420)
            self.entry_PVARP = Entry(self.frame_root)
            self.entry_PVARP.place(x=340, y=172)
            self.showAOO()



        elif self.mode == 0:
            self.background_image = tk.PhotoImage(file="backgroundpacingAOOVOO.png")
            self.label = Label(self.frame_root, image=self.background_image)
            self.label.image = self.background_image
            self.label.pack()

            self.common(155, 192, 155, 242, 60, 190, 60, 240, 300, 50, 300, 310, 300, 260, 300, 90, 155, 392, 80, 392, 300, 10)

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
            self.showVOO()



        elif self.mode == 3:
            self.background_image = tk.PhotoImage(file="backgroundpacingVIIAAI.png")
            self.label = Label(self.frame_root, image=self.background_image)
            self.label.image = self.background_image
            self.label.pack()

            self.common(155, 192, 155, 242, 60, 190, 60, 240, 430, 60, 400, 420, 400, 370, 430, 100, 410, 342, 338, 342, 430, 20)

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
            self.showAAI()



        elif self.mode == 2:
            self.background_image = tk.PhotoImage(file="backgroundpacingVIIAAI.png")
            self.label = Label(self.frame_root, image=self.background_image)
            self.label.image = self.background_image
            self.label.pack()

            self.common(180, 182, 180, 232, 85, 182, 85, 232, 430, 60, 400, 350, 400, 300, 430, 100, 410, 272, 338, 272,  430, 20)

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
            self.showVVI()


        elif self.mode == 4:
            self.background_image = tk.PhotoImage(file="backgroundpacing1.png")
            self.label = Label(self.frame_root, image=self.background_image)
            self.label.image = self.background_image
            self.label.pack()

            self.label_title2 = Label(self.frame_root, text="DOO Pacing Mode")
            self.label_title2.config(font=("Courier", 13))
            self.label_title2.place(x=120, y=145)

            self.common(140, 172, 140, 222, 46, 170, 46, 220, 300, 50, 300, 350, 300, 300, 300, 90, 360, 222, 290, 222,  300, 10)

            self.label.AV_del = Label(self.frame_root, text="Fixed Av Delay:")
            self.label.AV_del.place(x=57, y=272)
            self.label_Amp = Label(self.frame_root, text="Atrial Amplitude:")
            self.label_Amp.place(x=45, y=322)
            self.label_Amp = Label(self.frame_root, text="Ventricle Amplitude:")
            self.label_Amp.place(x=27, y=372)
            self.label_Pulse_Width = Label(self.frame_root, text="Atrial Pulse Width:")
            self.label_Pulse_Width.place(x=40, y=422)
            self.label_Pulse_Width = Label(self.frame_root, text="Vent Pulse Width:")
            self.label_Pulse_Width.place(x=260, y=172)

            self.entry_AV_del = Entry(self.frame_root)
            self.entry_AV_del.place(x=140, y=272)
            self.entry_AV_Amp = Entry(self.frame_root)
            self.entry_AV_Amp.place(x=140, y=322)
            self.entry_AV_Amp = Entry(self.frame_root)
            self.entry_AV_Amp.place(x=140, y=372)
            self.entry_Pulse_Width = Entry(self.frame_root)
            self.entry_Pulse_Width.place(x=140, y=422)
            self.entry_Pulse_Width = Entry(self.frame_root)
            self.entry_Pulse_Width.place(x=360, y=172)
            self.showDOO()

        elif self.mode == 9:
            self.background_image = tk.PhotoImage(file="backgroundpacingVIIAAI.png")
            self.label = Label(self.frame_root, image=self.background_image)
            self.label.image = self.background_image
            self.label.pack()

            self.label_title2 = Label(self.frame_root, text="DOOR Pacing Mode")
            self.label_title2.config(font=("Courier", 15))
            self.label_title2.place(x=180, y=145)

            self.common(145, 172, 145, 222, 50, 172, 50, 222, 430, 60, 160, 450, 230, 450, 430, 100, 400, 462, 315, 462, 430, 20)

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
            self.label_Act_Thres = Label(self.frame_root, text="Activity Threshold:")
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
            self.showDOOR()



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

            self.button_list = Button(self.frame_root,text="Parameter List")
            self.button_list.config(command=self.Parameter_List)
            self.button_list.place(x=1400, y=5)

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
            self.entry_BPM = Entry(self.frame_root)
            self.entry_BPM.place(x=920, y=422)

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
            self.label_BPM = Label(self.frame_root, text="Target BPM:")
            self.label_BPM.place(x=840, y=420)
            self.showDDDR()

        elif self.mode == 6:
            self.background_image = tk.PhotoImage(file="backgroundpacing3.png")
            self.label = Label(self.frame_root, image=self.background_image)
            self.label.image = self.background_image
            self.label.pack()

            self.label_title2 = Label(self.frame_root, text="AAIR Pacing Mode")
            self.label_title2.config(font=("Courier", 15))
            self.label_title2.place(x=320, y=120)

            self.common(145, 172, 145, 222, 50, 172, 50, 222, 750, 30, 330, 460, 400, 460, 750, 70, 710, 272, 640, 272, 750, 0)

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
            self.label_Pulse_Width.place(x=41, y=372)
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
            self.label_Act_Thres.place(x=344, y=372)
            self.label_React_Time = Label(self.frame_root, text="Reaction Time:")
            self.label_React_Time.place(x=365, y=422)

            self.entry_Recv_Time = Entry(self.frame_root)
            self.entry_Recv_Time.place(x=710, y=172)
            self.entry_Resp_Fact = Entry(self.frame_root)
            self.entry_Resp_Fact.place(x=710, y=222)

            self.label_Recv_Time = Label(self.frame_root, text="Recovery Time:")
            self.label_Recv_Time.place(x=621, y=172)
            self.label_Resp_Fact = Label(self.frame_root, text="Response Factor:")
            self.label_Resp_Fact.place(x=615, y=222)
            self.showAAIR()

        elif self.mode == 5:
            self.background_image = tk.PhotoImage(file="backgroundpacing1.png")
            self.label = Label(self.frame_root, image=self.background_image)
            self.label.image = self.background_image
            self.label.pack()

            self.label_title2 = Label(self.frame_root, text="AOOR Pacing Mode")
            self.label_title2.config(font=("Courier", 15))
            self.label_title2.place(x=160, y=145)

            self.common(125, 172, 125, 222, 30, 170, 30, 220, 400, 50, 350, 420, 350, 370, 400, 90, 360, 322, 288, 322, 400, 10)

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
            self.label_Amp.place(x=25, y=372)
            self.label_Pulse_Width = Label(self.frame_root, text="Atrial Pulse Width:")
            self.label_Pulse_Width.place(x=20, y=322)
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
            self.showAOOR()


        elif self.mode == 8:

            self.background_image = tk.PhotoImage(file="backgroundpacing3.png")
            self.label = Label(self.frame_root, image=self.background_image)
            self.label.image = self.background_image
            self.label.pack()
            self.label_title2 = Label(self.frame_root, text="VVIR Pacing Mode")
            self.label_title2.config(font=("Courier", 15))
            self.label_title2.place(x=300, y=120)

            self.common(150, 172, 150, 222, 55, 170, 55, 220, 700, 30, 700, 370, 700, 320, 700, 70, 700, 222, 628, 222, 700, 0)

            self.entry_Sensor_Rate = Entry(self.frame_root)
            self.entry_Sensor_Rate.place(x=150, y=272)
            self.entry_Vent_Amp = Entry(self.frame_root)
            self.entry_Vent_Amp.place(x=150, y=322)
            self.entry_Vent_Pulse = Entry(self.frame_root)
            self.entry_Vent_Pulse.place(x=150, y=372)
            self.entry_Vent_Sens = Entry(self.frame_root)
            self.entry_Vent_Sens.place(x=150, y=422)

            self.label_Sensor_Rate = Label(self.frame_root, text="Max Sensor Rate:")
            self.label_Sensor_Rate.place(x=55, y=272)
            self.label_Vent_Amp = Label(self.frame_root, text="Ventricle Amplitude:")
            self.label_Vent_Amp.place(x=35, y=323)
            self.label_Vent_Pulse = Label(self.frame_root, text="Ventricle Pulse Width:")
            self.label_Vent_Pulse.place(x=27, y=372)
            self.label_Vent_Sens = Label(self.frame_root, text="Ventricle Sensitivity:")
            self.label_Vent_Sens.place(x=38, y=422)

            self.entry_VRP = Entry(self.frame_root)
            self.entry_VRP.place(x=390, y=172)
            self.entry_Hyst = Entry(self.frame_root)
            self.entry_Hyst.place(x=390, y=220)
            self.entry_Rate_Smooth = Entry(self.frame_root)
            self.entry_Rate_Smooth.place(x=390, y=272)
            self.entry_Act_Thres = Entry(self.frame_root)
            self.entry_Act_Thres.place(x=390, y=322)
            self.entry_React_Time = Entry(self.frame_root)
            self.entry_React_Time.place(x=390, y=372)
            self.entry_Resp_Fact = Entry(self.frame_root)
            self.entry_Resp_Fact.place(x=390, y=422)
            self.entry_Recv_Time = Entry(self.frame_root)
            self.entry_Recv_Time.place(x=700, y=172)

            self.label_VRP = Label(self.frame_root, text="VRP:")
            self.label_VRP.place(x=360, y=172)
            self.label_Hyst = Label(self.frame_root, text="Hysteresis:")
            self.label_Hyst.place(x=327, y=222)
            self.label_Rate_Smooth = Label(self.frame_root, text="Rate Smoothing:")
            self.label_Rate_Smooth.place(x=295, y=272)
            self.label_Act_Thres = Label(self.frame_root, text="Activity Threshold:")
            self.label_Act_Thres.place(x=285, y=322)
            self.label_React_Time = Label(self.frame_root, text="Reaction Time:")
            self.label_React_Time.place(x=305, y=372)
            self.label_Resp_Fact = Label(self.frame_root, text="Response Factor:")
            self.label_Resp_Fact.place(x=295, y=422)
            self.label_Recv_Time = Label(self.frame_root, text="Recovery Time:")
            self.label_Recv_Time.place(x=610, y=172)
            self.showVVIR()


        elif self.mode == 7:

            self.background_image = tk.PhotoImage(file="backgroundpacing1.png")
            self.label = Label(self.frame_root, image=self.background_image)
            self.label.image = self.background_image
            self.label.pack()
            self.label_title2 = Label(self.frame_root, text="VOOR Pacing Mode")
            self.label_title2.config(font=("Courier", 15))
            self.label_title2.place(x=160, y=145)

            self.common(125, 172, 125, 222, 30, 170, 30, 220, 400, 50, 350, 420, 350, 370, 400, 90, 350, 322, 278, 322, 400, 10)

            self.label_Sensor_Rate = Label(self.frame_root, text="Max Sensor Rate:")
            self.label_Sensor_Rate.place(x=30, y=272)
            self.label_Vent_Amp = Label(self.frame_root, text="Vent Amplitude:")
            self.label_Vent_Amp.place(x=30, y=323)
            self.label_Vent_Pulse = Label(self.frame_root, text="Vent Pulse Width:")
            self.label_Vent_Pulse.place(x=27, y=372)
            self.label_Act_Thres = Label(self.frame_root, text="Activity Threshold:")
            self.label_Act_Thres.place(x=20, y=422)
            self.entry_Sensor_Rate = Entry(self.frame_root)
            self.entry_Sensor_Rate.place(x=125, y=272)
            self.entry_Vent_Amp = Entry(self.frame_root)
            self.entry_Vent_Amp.place(x=125, y=322)
            self.entry_Vent_Pulse = Entry(self.frame_root)
            self.entry_Vent_Pulse.place(x=125, y=372)
            self.entry_Act_Thres = Entry(self.frame_root)
            self.entry_Act_Thres.place(x=125, y=422)

            self.label_React_Time = Label(self.frame_root, text="Reaction Time:")
            self.label_React_Time.place(x=260, y=172)
            self.label_Resp_Fact = Label(self.frame_root, text="Response Factor:")
            self.label_Resp_Fact.place(x=257, y=222)
            self.label_Recv_Time = Label(self.frame_root, text="Recovery Time:")
            self.label_Recv_Time.place(x=260, y=272)

            self.entry_React_Time = Entry(self.frame_root)
            self.entry_React_Time.place(x=350, y=172)
            self.entry_Resp_Fact = Entry(self.frame_root)
            self.entry_Resp_Fact.place(x=350, y=222)
            self.entry_Recv_Time = Entry(self.frame_root)
            self.entry_Recv_Time.place(x=350, y=272)
            self.showVOOR()

    # All widgets are created in common() are common between all 4 pacing mode. Because the layout for the window of
    # each mode is different we will just pass the x and y coord as parameters when the method is called
    def common(self, upperlimx, upperlimy, lowerlimx, lowerlimy, upperlimx2, upperlimy2, lowerlimx2, lowerlimy2, backx,
               backy, okx, oky, applyx, applyy, signoutx, signouty, BPMX, BPMY, BPMX2, BPMY2, listx, listy):
        self.entry_Upperlim = Entry(self.frame_root)
        self.entry_Upperlim.place(x=upperlimx, y=upperlimy)
        self.entry_Lowerlim = Entry(self.frame_root)
        self.entry_Lowerlim.place(x=lowerlimx, y=lowerlimy)

        self.label_lowlim = Label(self.frame_root, text="Lower Rate limit:")
        self.label_lowlim.place(x=lowerlimx2, y=lowerlimy2)
        self.label_uplim = Label(self.frame_root, text="Upper Rate limit:")
        self.label_uplim.place(x=upperlimx2, y=upperlimy2)

        self.entry_BPM = Entry(self.frame_root)
        self.entry_BPM.place(x=BPMX, y=BPMY)

        self.label_BPM = Label(self.frame_root, text="Target BPM:")
        self.label_BPM.place(x=BPMX2, y=BPMY2)

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

        self.button_signout = Button(self.frame_root, text="Parameter Limits")
        self.button_signout.config(command=self.Parameter_List)
        self.button_signout.place(x=listx, y=listy)

    def from_Parameter_Window(self):  # Returns to the pacing screen
        Notifiy_Window.Notify_window(10, self.frame_root, self.master, self.df, 1, self.user)

    def To_login(self):
        Notifiy_Window.Notify_window(9, self.frame_root, self.master, self.df, 0, self.user)

    def Parameter_List(self):
        Lists.Parameter_List()

    def Apply(self):  # Apply will save the #parameters in the entry fields and return to the pacing screen
        if self.mode == 1:
            self.save_AOO()
        elif self.mode == 0:
            self.save_VOO()
        elif self.mode == 3:
            self.save_AAI()
        elif self.mode == 2:
            self.save_VVI()
        elif self.mode == 4:
            self.save_DOO()
        elif self.mode == 9:
            self.save_DOOR()
        elif self.mode == 10:
            self.save_DDDR()
        elif self.mode == 5:
            self.save_AOOR()
        elif self.mode == 8:
            self.save_VVIR()
        elif self.mode == 6:
            self.save_AAIR()
        elif self.mode == 7:
            self.save_VOOR()

        self.frame_root.pack_forget()
        self.PacingWindow = Pacing_Screen.Pacing_Window(self.master, self.user, self.df)
        # Add code here to also save the parameters

    def Ok(self):  # Ok will only save the parameters in the entry fields
        if self.mode == 1:
            self.save_AOO()
        elif self.mode == 0:
            self.save_VOO()
        elif self.mode == 3:
            self.save_AAI()
        elif self.mode == 2:
            self.save_VVI()
        elif self.mode == 4:
            self.save_DOO()
        elif self.mode == 9:
            self.save_DOOR()
        elif self.mode == 10:
            self.save_DDDR()
        elif self.mode == 5:
            self.save_AOOR()
        elif self.mode == 8:
            self.save_VVIR()
        elif self.mode == 6:
            self.save_AAIR()
        elif self.mode == 7:
            self.save_VOOR()
        # add code here to save the parameters

    def save_VOO(self):
        try:
            success =  True
            for j in range(0, 20, 2):
                if self.user == self.df.at[j, 'Users']:  #['Users'].iloc[i]:  ##find user
                    self.data[1] = self.mode
                    if int(self.entry_Lowerlim.get()) in range(45, 66):
                        self.df.at[j, 'VOO Lower Rate Limit'] = int(self.entry_Lowerlim.get())#df['Users'].iloc[i], 'VOO Lower Rate Limit'] = int(self.entry_Lowerlim.get())
                        #self.data[2] = int(self.entry_Lowerlim.get())
                    else:
                        success = False
                    if int(self.entry_Upperlim.get()) in range(120, 151):
                        self.df.at[j, 'VOO Upper Rate Limit'] = int(self.entry_Upperlim.get())
                        #self.data[3] = int(self.entry_Upperlim.get())
                    else:
                        success = False
                    if int(self.entry_Pulse_Width.get()) in range(1, 11):
                        self.df.at[j, 'VOO Pulse Width'] = int(self.entry_Pulse_Width.get())
                        self.data[6] = int(self.entry_Pulse_Width.get())
                    else:
                        success = False
                    if int(self.entry_AV_Amp.get()) in range(50, 101):
                        self.df.at[j, 'VOO Ventricular Amplitude'] = int(self.entry_AV_Amp.get())
                        self.data[5] = int(self.entry_AV_Amp.get())
                    else:
                        success = False
                    if int(self.entry_BPM.get()) >= int(self.entry_Lowerlim.get()) and int(self.entry_BPM.get()) <= int(self.entry_Upperlim.get()):
                        self.df.at[j, 'VOO Target BPM'] = int(self.entry_BPM.get())
                        self.data[2] = int(self.entry_BPM.get())
                    else:
                        success = False
                    if success == True:
                        self.writeParameters()
                        ex.saveDataFrame(self.df)
                    else:
                        Notifiy_Window.Notify_window(8,self.frame_root,self.master,self.df,2,self.user)

            ##lower rate limit, upper rate limit, pulsewidth, ventrical amplitude
        except ValueError:
            Notifiy_Window.Notify_window(8,self.frame_root,self.master,self.df,2,self.user)

    def save_AOO(self):
        try:
            success = True
            for j in range(0, 20, 2):
                if self.user == self.df.iat[j, 0]:  ##find user
                    self.data[1] = self.mode
                    if 45 <= int(self.entry_Lowerlim.get()) <= 65:# >= 45 and int(self.entry_Lowerlim.get()) <= 65:#in range(45, 66):
                        self.df.at[j, 'AOO Lower Rate Limit'] = int(self.entry_Lowerlim.get())
                        #self.data[2] = int(self.entry_Lowerlim.get())
                        print('yes')
                    else:
                        success = False
                        print('no')
                    if 120 <= int(self.entry_Upperlim.get()) <= 150:#in range(120, 151):
                        self.df.at[j, 'AOO Upper Rate Limit'] = int(self.entry_Upperlim.get())
                        #self.data[3] = int(self.entry_Upperlim.get())
                        print('yes')
                    else:
                        success = False
                        print('no')
                    if int(self.entry_Pulse_Width.get()) in range(1, 11):
                        self.df.at[j, 'AOO Pulse Width'] = int(self.entry_Pulse_Width.get())
                        self.data[6] = int(self.entry_Pulse_Width.get())
                        print('yes')
                    else:
                        success = False
                        print('no')
                    if int(self.entry_AV_Amp.get()) in range(50, 101):
                        self.df.at[j, 'AOO Atrial Amplitude'] = int(self.entry_AV_Amp.get())
                        self.data[5] = int(self.entry_AV_Amp.get())
                        print('yes')
                    else:
                        success = False
                        print('no')
                    if int(self.entry_BPM.get()) >= int(self.entry_Lowerlim.get()) and int(self.entry_BPM.get()) <= int(self.entry_Upperlim.get()):
                        self.df.at[j, 'AOO Target BPM'] = int(self.entry_BPM.get())
                        self.data[2] = int(self.entry_BPM.get())
                    else:
                        success = False

            if success == True:
                self.writeParameters()
                ex.saveDataFrame(self.df)
            else:
                Notifiy_Window.Notify_window(8,self.frame_root,self.master,self.df,2,self.user)
                print(self.data)

            ##lower rate limit, upper rate limit, pulsewidth, ventrical amplitude
        except ValueError:
            Notifiy_Window.Notify_window(8,self.frame_root,self.master,self.df,2,self.user)
        ##LowerRateLimit, upper rate limit, pulse width, atrial amplitude
        ##save parameter

    def save_VVI(self):
        try:
            for j in range(0, 20, 2):
                success = True
                if self.user == self.df.iat[j, 0]:  ##find user
                    self.data[1] = self.mode
                    if int(self.entry_Lowerlim.get()) in range(45, 66):
                        self.df.at[j, 'VVI Lower Rate Limit'] = int(self.entry_Lowerlim.get())
                        #self.data[2] = int(self.entry_Lowerlim.get())
                    else:
                        success = False
                    if int(self.entry_Upperlim.get()) in range(120, 151):
                        self.df.at[j, 'VVI Upper Rate Limit'] = int(self.entry_Upperlim.get())
                        #self.data[3] = int(self.entry_Upperlim.get())
                    else:
                        success = False
                    if int(self.entry_Pulse_Width.get()) in range(1, 11):
                        self.df.at[j, 'VVI Pulse Width'] = int(self.entry_Pulse_Width.get())
                        self.data[6] = int(self.entry_Pulse_Width.get())
                    else:
                        success = False
                    if int(self.entry_AV_Amp.get()) in range(50, 101):
                        self.df.at[j, 'VVI Ventricular Amplitude'] = int(self.entry_AV_Amp.get())
                        self.data[5] = int(self.entry_AV_Amp.get())
                    else:
                        success = False
                    if int(self.entry_AV_Sens.get()) >= 65 and int(self.entry_AV_Sens.get()) <= 70:
                        self.df.at[j, 'VVI Ventricular Sensitivity'] = int(self.entry_AV_Sens.get())
                        self.data[7] = int(self.entry_AV_Sens.get())
                    else:
                        success = False
                    if int(self.entry_VRP.get()) >= 150 and int(self.entry_VRP.get()) <= 300:
                        self.df.at[j, 'VVI VRP'] = int(self.entry_VRP.get())
                        self.data[8] = int(self.entry_VRP.get())
                    else:
                        success = False
                    if int(self.entry_Rate_Smooth.get()) >= 0 and int(self.entry_Rate_Smooth.get()) <= 100:
                        self.df.at[j, 'VVI Rate Smoothing'] = int(self.entry_Rate_Smooth.get())
                        #self.data[16] = int(self.entry_Rate_Smooth.get())
                    else:
                        success = False
                    if int(self.entry_BPM.get()) >= int(self.entry_Lowerlim.get()) and int(self.entry_BPM.get()) <= int(self.entry_Upperlim.get()):
                        self.df.at[j, 'VVI Target BPM'] = int(self.entry_BPM.get())
                        self.data[4] = int(self.entry_BPM.get())
                    else:
                       success = False
                    if success == True:
                        self.writeParameters()
                        ex.saveDataFrame(self.df)
                    else:
                        Notifiy_Window.Notify_window(8,self.frame_root,self.master,self.df,2,self.user)

            ##lower rate limit, upper rate limit, pulsewidth, Ventricular amplitude
        except ValueError:
            Notifiy_Window.Notify_window(8,self.frame_root,self.master,self.df,2,self.user)

    def save_AAI(self):
        try:
            for j in range(0, 20, 2):
                if self.user == self.df.iat[j, 0]:  ##find user
                    success = True
                    self.data[1] = self.mode
                    if int(self.entry_Lowerlim.get()) in range(45, 66):
                        self.df.at[j, 'AAI Lower Rate Limit'] = int(self.entry_Lowerlim.get())
                        #self.data[2] = int(self.entry_Lowerlim.get())
                    else:
                        success = False
                    if int(self.entry_Upperlim.get()) in range(120, 151):
                        self.df.at[j, 'AAI Upper Rate Limit'] = int(self.entry_Upperlim.get())
                        #self.data[3] = int(self.entry_Upperlim.get())
                    else:
                        success = False
                    if int(self.entry_Pulse_Width.get()) in range(1, 11):
                        self.df.at[j, 'AAI Pulse Width'] = int(self.entry_Pulse_Width.get())
                        self.data[6] = int(self.entry_Pulse_Width.get())
                    else:
                        success = False
                    if int(self.entry_AV_Amp.get()) in range(50, 101):
                        self.df.at[j, 'AAI Atrial Amplitude'] = int(self.entry_AV_Amp.get())
                        self.data[5] = int(self.entry_AV_Amp.get())
                    else:
                        success = False
                    if int(self.entry_AV_Sens.get()) >= 65 and int(self.entry_AV_Sens.get()) <= 70:
                        self.df.at[j, 'AAI Atrial Sensitivity'] = int(self.entry_AV_Sens.get())
                        self.data[6] = int(self.entry_AV_Sens.get())
                    else:
                        success = False
                    if int(self.entry_ARP.get()) >= 150 and int(self.entry_ARP.get()) <= 300:
                        self.df.at[j, 'AAI ARP'] = int(self.entry_ARP.get())
                        self.data[8] = int(self.entry_ARP.get())
                    else:
                        success = False
                    if int(self.entry_Rate_Smooth.get()) >= 0 and int(self.entry_Rate_Smooth.get()) <= 100:
                        self.df.at[j, 'AAI Rate Smoothing'] = int(self.entry_Rate_Smooth.get())
                        #self.data[16] = int(self.entry_Rate_Smooth.get())
                    else:
                        success = False
                    if int(self.entry_BPM.get()) >= int(self.entry_Lowerlim.get()) and int(self.entry_BPM.get()) <= int(self.entry_Upperlim.get()):
                        self.df.at[j, 'AAI Target BPM'] = int(self.entry_BPM.get())
                        self.data[4] = int(self.entry_BPM.get())
                    else:
                        success = False
                    if success == True:
                        self.writeParameters()
                        ex.saveDataFrame(self.df)
                    else:
                        Notifiy_Window.Notify_window(8, self.frame_root, self.master, self.df, 2, self.user)
            ##lower rate limit, upper rate limit, pulsewidth, Ventricular amplitude
        except ValueError:
            Notifiy_Window.Notify_window(8,self.frame_root,self.master,self.df,2,self.user)

    def save_DOO(self):
        try:
            success = True
            for j in range(0, 20, 2):
                if self.user == self.df.iat[j, 0]:  ##find user
                    self.data[1] = self.mode
                    if int(self.entry_Lowerlim.get()) in range(45, 66):
                        self.df.at[j, 'DOO Lower Rate Limit'] = int(self.entry_Lowerlim.get())
                        #self.data[2] = int(self.entry_Lowerlim.get())
                    else:
                        success = False
                    if int(self.entry_Upperlim.get()) in range(120, 151):
                        self.df.at[j, 'DOO Upper Rate Limit'] = int(self.entry_Upperlim.get())
                        #self.data[3] = int(self.entry_Upperlim.get())
                    else:
                        success = False
                    if int(self.entry_Pulse_Width.get()) in range(1, 11):
                        self.df.at[j, 'DOO Ventrical Pulse Width'] = int(self.entry_Pulse_Width.get())
                        self.data[6] = int(self.entry_Pulse_Width.get())
                    else:
                        success = False
                    if int(self.entry_AV_Amp.get()) in range(50, 101):
                        self.df.at[j, 'DOO Ventricular Amplitude'] = int(self.entry_AV_Amp.get())
                        self.data[5] = int(self.entry_AV_Amp.get())
                        #self.data[9] = int(self.entry_AV_Amp.get())
                    else:
                        success = False
                    #if int(self.entry_AV_Amp.get()) in range(50, 101):
                        #self.df[self.df['Users'].iloc[i], 'DOO Atrial Amplitude'] = int(self.entry_AV_Amp.get())
                    #f int(self.entry_Pulse_Width.get()) in range(1, 11):
                        #self.df[self.df['Users'].iloc[i], 'DOO Atrial Pulse Width'] = int(self.entry_Pulse_Width.get())
                    if int(self.entry_AV_del.get()) >= 70 and int(self.entry_AV_del.get()) <= 300:
                        self.df.at[j, 'DOO Fixed AV Delay'] = int(self.entry_AV_del.get())
                        self.data[4] = int(self.entry_AV_del.get())
                    else:
                        success = False
                    if int(self.entry_BPM.get()) >= int(self.entry_Lowerlim.get()) and int(self.entry_BPM.get()) <= int(self.entry_Upperlim.get()):
                        self.df.at[j, 'DOO Target BPM'] = int(self.entry_BPM.get())
                        self.data[4] = int(self.entry_BPM.get())
                    else:
                       success = False
                    if success == True:
                        self.writeParameters()
                        ex.saveDataFrame(self.df)
                    else:
                        Notifiy_Window.Notify_window(8,self.frame_root,self.master,self.df,2,self.user)
            ##lower rate limit, upper rate limit, pulsewidth, Ventricular amplitude
        except ValueError:
            Notifiy_Window.Notify_window(8, self.frame_root, self.master, self.df, 2, self.user)
        # save parameters
    def save_AOOR(self):
        try:
            success = True
            for j in range(0, 20, 2):
                if self.user == self.df.iat[j, 0]:  ##find user
                    self.data[1] = self.mode
                    if int(self.entry_Lowerlim.get()) in range(45, 66):
                        self.df.at[j, 'AOOR Lower Rate Limit'] = int(self.entry_Lowerlim.get())
                        #self.data[2] = int(self.entry_Lowerlim.get())
                        print('yes')
                    else:
                        success = False
                        print('no')
                    if int(self.entry_Upperlim.get()) in range(120, 151):
                        self.df.at[j, 'AOOR Upper Rate Limit'] = int(self.entry_Upperlim.get())
                        #self.data[3] = int(self.entry_Upperlim.get())
                        print('upyes')
                    else:
                        success = False
                    if int(self.entry_Pulse_Width.get()) in range(1, 11):
                        self.df.at[j, 'AOOR Pulse Width'] = int(self.entry_Pulse_Width.get())
                        self.data[6] = int(self.entry_Pulse_Width.get())
                        print('widyes')
                    else:
                        success = False
                    if int(self.entry_AV_Amp.get()) in range(50, 101):
                        self.df.at[j, 'AOOR Atrial Amplitude'] = int(self.entry_AV_Amp.get())
                        self.data[5] = int(self.entry_AV_Amp.get())
                        print('amp')
                    else:
                        success = False
                    if 1.3 < float(self.entry_Act_Thres.get()) and float(self.entry_Act_Thres.get()) < 1.7:
                        self.df.at[j, 'AOOR Activity Threshold'] = float(self.entry_Act_Thres.get())
                        self.data[9] = float(self.entry_Act_Thres.get())
                        print('act')
                    else:
                        success = False
                    if int(self.entry_React_Time.get()) >= 10 and int(self.entry_React_Time.get()) <= 50:
                        self.df.at[j, 'AOOR Reaction Time'] = int(self.entry_React_Time.get())
                        self.data[10] = int(self.entry_React_Time.get())
                        print('reach')
                    else:
                        success = False
                    if int(self.entry_Resp_Fact.get()) >= 1 and int(self.entry_Resp_Fact.get()) <= 16:
                        self.df.at[j, 'AOOR Response Factor'] = int(self.entry_Resp_Fact.get())
                        self.data[11] = int(self.entry_Resp_Fact.get())
                        print('rep')
                    else:
                        success = False
                    if int(self.entry_Recv_Time.get()) >= 2 and int(self.entry_Recv_Time.get()) <= 16:
                        self.df.at[j, 'AOOR Recovery Time'] = int(self.entry_Recv_Time.get())
                        self.data[12] = int(self.entry_Recv_Time.get())
                        print('recov')
                    else:
                        success = False
                    if int(self.entry_AV_Sensor_Rate.get()) in range(50, 151):
                        self.df.at[j, 'AOOR Sensor Rate'] = int(self.entry_AV_Sensor_Rate.get())
                        self.data[3] = int(self.entry_AV_Sensor_Rate.get())
                        print('sens')
                    else:
                        success = False
                    if int(self.entry_BPM.get()) >= int(self.entry_Lowerlim.get()) and int(self.entry_BPM.get()) <= int(self.entry_Upperlim.get()):
                        self.df.at[j, 'AOOR Target BPM'] = int(self.entry_BPM.get())
                        self.data[4] = int(self.entry_BPM.get())
                        print('bpm')
                    else:
                       success = False
                    if success == True:
                        self.writeParameters()
                        ex.saveDataFrame(self.df)
                    else:
                        Notifiy_Window.Notify_window(8, self.frame_root, self.master, self.df, 2, self.user)

            ##lower rate limit, upper rate limit, pulsewidth, Ventricular amplitude
        except ValueError:
            Notifiy_Window.Notify_window(8,self.frame_root,self.master,self.df,2,self.user)
        ##save parameters

    def save_AAIR(self):
        try:
            success = True
            for j in range(0, 20, 2):
                if self.user == self.df.iat[j, 0]:  ##find user
                    self.data[1] = self.mode
                    if int(self.entry_Lowerlim.get()) in range(45, 66):
                        self.df.at[j, 'AAIR Lower Rate Limit'] = int(self.entry_Lowerlim.get())
                        #self.data[2] = int(self.entry_Lowerlim.get())
                    else:
                        success = False
                    if int(self.entry_Upperlim.get()) in range(120, 151):
                        self.df.at[j, 'AAIR Upper Rate Limit'] = int(self.entry_Upperlim.get())
                        #self.data[3] = int(self.entry_Upperlim.get())
                    else:
                        success = False
                    if int(self.entry_Pulse_Width.get()) in range(1, 11):
                        self.df.at[j, 'AAIR Pulse Width'] = int(self.entry_Pulse_Width.get())
                        self.data[6] = int(self.entry_Pulse_Width.get())
                    else:
                        success = False
                    if int(self.entry_AV_Amp.get()) in range(50, 101):
                        self.df.at[j, 'AAIR Atrial Amplitude'] = int(self.entry_AV_Amp.get())
                        self.data[5] = int(self.entry_AV_Amp.get())
                    else:
                        success = False
                    if int(self.entry_AV_Sensor_Rate.get()) >= 50 and int(self.entry_AV_Sensor_Rate.get()) <= 150:
                        self.df.at[j, 'AAIR Sensor Rate'] = int(self.entry_AV_Sensor_Rate.get())
                        self.data[3] = int(self.entry_AV_Sensor_Rate.get())
                    else:
                        success = False
                    if int(self.entry_AV_Sens.get()) in range(65, 71):
                        self.df.at[j, 'AAIR Atrial Sensitivity'] = int(self.entry_AV_Sens.get())
                        self.data[7] = int(self.entry_AV_Sens.get())
                    else:
                        success = False
                    #if int(self.entry_Rate_Smooth()) in range(0, 101):
                     #   self.df.at[j, 'AAIR Rate Smoothing'] = int(self.entry_Rate_Smooth.get())
                        #self.data[16] = int(self.entry_Rate_Smooth.get())
                    #else:
                        #success = False
                    if 1.3 < float(self.entry_Act_Thres.get()) and float(self.entry_Act_Thres.get()) < 1.7:
                        self.df.at[j, 'AAIR Activity Threshold'] = float(self.entry_Act_Thres.get())
                        self.data[9] = float(self.entry_Act_Thres.get())
                    else:
                        success = False
                    if int(self.entry_React_Time.get()) >= 10 and int(self.entry_React_Time.get()) <= 50:
                        self.df.at[j, 'AAIR Reaction Time'] = int(self.entry_React_Time.get())
                        self.data[10] = int(self.entry_React_Time.get())
                    else:
                        success = False
                    if int(self.entry_Resp_Fact.get()) >= 1 and int(self.entry_Resp_Fact.get()) <= 16:
                        self.df.at[j, 'AAIR Response Factor'] = int(self.entry_Resp_Fact.get())
                        self.data[11] = int(self.entry_Resp_Fact.get())
                    else:
                        success = False
                    if int(self.entry_Recv_Time.get()) >= 2 and int(self.entry_Recv_Time.get()) <= 16:
                        self.df.at[j, 'AAIR Recovery Time'] = int(self.entry_Recv_Time.get())
                        self.data[12] = int(self.entry_Recv_Time.get())
                    else:
                        success = False
                    if int(self.entry_ARP.get()) >= 150 and int(self.entry_ARP.get()) <= 300:
                        self.df.at[j, 'AAIR ARP'] = int(self.entry_ARP.get())
                        self.data[8] = int(self.entry_ARP.get())
                    else:
                        success = False
                    if int(self.entry_BPM.get()) >= int(self.entry_Lowerlim.get()) and int(self.entry_BPM.get()) <= int(self.entry_Upperlim.get()):
                        self.df.at[j, 'AAIR Target BPM'] = int(self.entry_BPM.get())
                        self.data[4] = int(self.entry_BPM.get())
                    else:
                        success = False
                    if success == True:
                        self.writeParameters()
                        ex.saveDataFrame(self.df)
                    else:
                        Notifiy_Window.Notify_window(8,self.frame_root,self.master,self.df,2,self.user)
            ##lower rate limit, upper rate limit, pulsewidth, Ventricular amplitude
        except ValueError:
            Notifiy_Window.Notify_window(8,self.frame_root,self.master,self.df,2,self.user)
        ##save parameters
    def save_VOOR(self):
        try:
            success = True
            for j in range(0, 20, 2):
                if self.user == self.df.iat[j, 0]:  ##find user
                    self.data[1] = self.mode
                    if int(self.entry_Lowerlim.get()) in range(45, 66):
                        self.df.at[j, 'VOOR Lower Rate Limit'] = int(self.entry_Lowerlim.get())
                        #self.data[2] = int(self.entry_Lowerlim.get())
                    else:
                        success = False
                    if int(self.entry_Upperlim.get()) in range(120, 151):
                        self.df.at[j, 'VOOR Upper Rate Limit'] = int(self.entry_Upperlim.get())
                        #self.data[3] = int(self.entry_Upperlim.get())
                    else:
                        success = False
                    if int(self.entry_Vent_Pulse.get()) in range(1, 11):
                        self.df.at[j, 'VOOR Pulse Width'] = int(self.entry_Vent_Pulse.get())
                        self.data[6] = int(self.entry_Vent_Pulse.get())
                    else:
                        success = False
                    if int(self.entry_Vent_Amp.get()) in range(50, 101):
                        self.df.at[j, 'VOOR Ventricular Amplitude'] = int(self.entry_Vent_Amp.get())
                        self.data[5] = int(self.entry_Vent_Amp.get())
                    else:
                        success = False
                    if 1.3 < float(self.entry_Act_Thres.get()) and float(self.entry_Act_Thres.get()) < 1.7:
                        self.df.at[j, 'VOOR Activity Threshold'] = float(self.entry_Act_Thres.get())
                        self.data[9] = float(self.entry_Act_Thres.get())
                    else:
                        success = False
                    if int(self.entry_React_Time.get()) >= 10 and int(self.entry_React_Time.get()) <= 15:
                        self.df.at[j, 'VOOR Reaction Time'] = int(self.entry_React_Time.get())
                        self.data[10] = int(self.entry_React_Time.get())
                    else:
                        success = False
                    if int(self.entry_Resp_Fact.get()) >= 1 and int(self.entry_Resp_Fact.get()) <= 16:
                        self.df.at[j, 'VOOR Response Factor'] = int(self.entry_Resp_Fact.get())
                        self.data[11] = int(self.entry_Resp_Fact.get())
                    else:
                        success = False
                    if int(self.entry_Recv_Time.get()) >= 2 and int(self.entry_Recv_Time.get()) <= 16:
                        self.df.at[j, 'VOOR Recovery Time'] = int(self.entry_Recv_Time.get())
                        self.data[12] = int(self.entry_Recv_Time.get())
                    else:
                        success = False
                    if int(self.entry_Sensor_Rate.get()) in range(50, 176):
                        self.df.at[j, 'VOOR Sensor Rate'] = int(self.entry_Sensor_Rate.get())
                        self.data[3] = int(self.entry_Sensor_Rate.get())
                    else:
                        success = False
                    if int(self.entry_BPM.get()) >= int(self.entry_Lowerlim.get()) and int(self.entry_BPM.get()) <= int(self.entry_Upperlim.get()):
                        self.df.at[j, 'VOOR Target BPM'] = int(self.entry_BPM.get())
                        self.data[4] = int(self.entry_BPM.get())
                    else:
                        success = False
                    if success == True:
                        self.writeParameters()
                        ex.saveDataFrame(self.df)
                    else:
                        Notifiy_Window.Notify_window(8,self.frame_root,self.master,self.df,2,self.user)

            ##lower rate limit, upper rate limit, pulsewidth, Ventricular amplitude
        except ValueError:
            Notifiy_Window.Notify_window(8,self.frame_root,self.master,self.df,2,self.user)
        ##save parameters
    def save_VVIR(self):
        try:
            success = True
            for j in range(0, 20, 2):
                if self.user == self.df.iat[j, 0]:  ##find user
                    self.data[1] = self.mode
                    if int(self.entry_Lowerlim.get()) in range(45, 66):
                        self.df.at[j, 'VVIR Lower Rate Limit'] = int(self.entry_Lowerlim.get())
                        #self.data[2] = int(self.entry_Lowerlim.get())
                    else:
                        success = False
                    if int(self.entry_Upperlim.get()) in range(120, 151):
                        self.df.at[j, 'VVIR Upper Rate Limit'] = int(self.entry_Upperlim.get())
                        #self.data[3] = int(self.entry_Upperlim.get())
                    else:
                        success = False
                    if int(self.entry_Vent_Pulse.get()) in range(1, 11):
                        self.df.at[j, 'VVIR Pulse Width'] = int(self.entry_Vent_Pulse.get())
                        self.data[6] = int(self.entry_Vent_Pulse.get())
                    else:
                        success = False
                    if int(self.entry_Vent_Amp.get()) in range(50, 101):
                        self.df.at[j, 'VVIR Ventricular Amplitude'] = int(self.entry_Vent_Amp.get())
                        self.data[5] = int(self.entry_Vent_Amp.get())
                    else:
                        success = False
                    if int(self.entry_Sensor_Rate.get()) >= 50 and int(self.entry_Sensor_Rate.get()) <=150:
                        self.df.at[j, 'VVIR Sensor Rate'] = int(self.entry_Sensor_Rate.get())
                        self.data[3] = int(self.entry_Sensor_Rate.get())
                    else:
                        success = False
                    if int(self.entry_Vent_Sens.get()) in range(65, 71):
                        self.df.at[j, 'VVIR Ventricular Sensitivity'] = int(self.entry_Vent_Sens.get())
                        self.data[7] = int(self.entry_Vent_Sens.get())
                    else:
                        success = False
                    #if int(self.entry_Rate_Smooth()) in range(0, 101):
                     #   self.df.at[j, 'VVIR Rate Smoothing'] = int(self.entry_Rate_Smooth.get())
                        #self.data[16] = int(self.entry_Rate_Smooth.get())
                    #else:
                     #   success = False
                    if 1.3 < float(self.entry_Act_Thres.get()) and float(self.entry_Act_Thres.get()) < 1.7:
                        self.df.at[j, 'VVIR Activity Threshold'] = float(self.entry_Act_Thres.get())
                        self.data[9] = float(self.entry_Act_Thres.get())
                    else:
                        success = False
                    if int(self.entry_React_Time.get()) >= 10 and int(self.entry_React_Time.get()) <= 50:
                        self.df.at[j, 'VVIR Reaction Time'] = int(self.entry_React_Time.get())
                        self.data[10] = int(self.entry_React_Time.get())
                    else:
                        success = False
                    if int(self.entry_Resp_Fact.get()) >= 1 and int(self.entry_Resp_Fact.get()) <= 16:
                        self.df.at[j, 'VVIR Response Factor'] = int(self.entry_Resp_Fact.get())
                        self.data[11] = int(self.entry_Resp_Fact.get())
                    else:
                        success = False
                    if int(self.entry_Recv_Time.get()) >= 2 and int(self.entry_Recv_Time.get()) <= 16:
                        self.df.at[j, 'VVIR Recovery Time'] = int(self.entry_Recv_Time.get())
                        self.data[12] = int(self.entry_Recv_Time.get())
                    else:
                        success = False
                    if int(self.entry_VRP.get()) >= 150 and int(self.entry_VRP.get()) <= 300:
                        self.df.at[j, 'VVIR VRP'] = int(self.entry_VRP.get())
                        self.data[8] = int(self.entry_VRP.get())
                    else:
                        success = False
                    if int(self.entry_BPM.get()) >= int(self.entry_Lowerlim.get()) and int(self.entry_BPM.get()) <= int(self.entry_Upperlim.get()):
                        self.df.at[j, 'VVIR Target BPM'] = int(self.entry_BPM.get())
                        self.data[4] = int(self.entry_BPM.get())
                    else:
                        success = False
                    if success == True:
                        self.writeParameters()
                        ex.saveDataFrame(self.df)
                    else:
                        Notifiy_Window.Notify_window(8)
            ##lower rate limit, upper rate limit, pulsewidth, Ventricular amplitude
        except ValueError:
            Notifiy_Window.Notify_window(8,self.frame_root,self.master,self.df,2,self.user)
        ##save parameters
    def save_DOOR(self):
        try:
            success = True
            for j in range(0, 20, 2):
                if self.user == self.df.iat[j, 0]:  ##find user
                    self.data[1] = self.mode
                    if int(self.entry_Lowerlim.get()) in range(45, 66):
                        self.df.at[j, 'DOOR Lower Rate Limit'] = int(self.entry_Lowerlim.get())
                        print('yes')
                        #self.data[2] = int(self.entry_Lowerlim.get())
                    else:
                        success = False
                        print('no')
                    if int(self.entry_Upperlim.get()) in range(120, 151):
                        self.df.at[j, 'DOOR Upper Rate Limit'] = int(self.entry_Upperlim.get())
                        print('yes')
                        #self.data[3] = int(self.entry_Upperlim.get())
                    else:
                        success = False
                        print('no')
                    if int(self.entry_Pulse_Width.get()) in range(1, 11):
                        self.df.at[j, 'DOOR Ventrical Pulse Width'] = int(self.entry_Pulse_Width.get())
                        self.data[6] = int(self.entry_Pulse_Width.get())
                        print('yes')
                    else:
                        success = False
                        print('no')
                    if int(self.entry_AV_Amp.get()) in range(50, 101):
                        self.df.at[j, 'DOOR Ventricular Amplitude'] = int(self.entry_AV_Amp.get())
                        self.data[5] = int(self.entry_AV_Amp.get())
                        print('yes')
                    else:
                        success = False
                        print('no')
                    #if int(self.entry_AV_Amp.get()) >= 65 and int(self.entry_AV_Amp.get()) <= 70:
                        #self.df[self.df['Users'].iloc[i], 'DOOR Atrial Amplitude'] = int(self.entry_AV_Amp.get())
                    #if int(self.entry_Pulse_Width.get()) in range(1, 11):
                        #self.df[self.df['Users'].iloc[i], 'DOOR Atrial Pulse Width'] = int(self.entry_Pulse_Width.get())
                    if int(self.entry_AV_Delay.get()) >= 70 and int(self.entry_AV_Delay.get()) <= 300:
                        self.df.at[j, 'DOOR Fixed AV Delay'] = int(self.entry_AV_Delay.get())
                        self.data[4] = int(self.entry_AV_Delay.get())
                        print('yes')
                    else:
                        success = False
                        print('no')
                    #if int(self.entry_Rate_Smooth()) in range(0, 101):
                      #  self.df.at[j, 'DOOR Rate Smoothing'] = int(self.entry_Rate_Smooth.get())
                       # #self.data[16] = int(self.entry_Rate_Smooth.get())
                    #else:
                     #   success = False
                    if 1.3 < float(self.entry_Act_Thres.get()) and float(self.entry_Act_Thres.get()) < 1.7:
                        self.df.at[j, 'DOOR Activity Threshold'] = float(self.entry_Act_Thres.get())
                        self.data[9] = float(self.entry_Act_Thres.get())
                        print('yes')
                    else:
                        success = False
                        print('no')
                    if int(self.entry_React_Time.get()) >= 10 and int(self.entry_React_Time.get()) <= 50:
                        self.df.at[j, 'DOOR Reaction Time'] = int(self.entry_React_Time.get())
                        self.data[10] = int(self.entry_React_Time.get())
                        print('yes')
                    else:
                        success = False
                        print('no')
                    if int(self.entry_Resp_Fact.get()) >= 1 and int(self.entry_Resp_Fact.get()) <= 16:
                        self.df.at[j, 'DOOR Response Factor'] = int(self.entry_Resp_Fact.get())
                        self.data[11] = int(self.entry_Resp_Fact.get())
                        print('yes')
                    else:
                        success = False
                        print('no')
                    if int(self.entry_Recv_Time.get()) >= 2 and int(self.entry_Recv_Time.get()) <= 16:
                        self.df.at[j, 'DOOR Recovery Time'] = int(self.entry_Recv_Time.get())
                        self.data[12] = int(self.entry_Recv_Time.get())
                        print('yes')
                    else:
                        success = False
                        print('no')
                    if int(self.entry_BPM.get()) >= int(self.entry_Lowerlim.get()) and int(self.entry_BPM.get()) <= int(self.entry_Upperlim.get()):
                        self.df.at[j, 'DOOR Target BPM'] = int(self.entry_BPM.get())
                        self.data[2] = int(self.entry_BPM.get())
                        print('yes')
                    else:
                        success = False
                        print('no')
                    if int(self.entry_AV_Sensor_Rate.get()) in range(50, 151):
                        self.df.at[j, 'DOOR Sensor Rate'] = int(self.entry_AV_Sensor_Rate.get())
                        self.data[3] = int(self.entry_AV_Sensor_Rate.get())
                        print('yes')
                    else:
                        success = False
                        print('no')
                    if success == True:
                        self.writeParameters()
                        ex.saveDataFrame(self.df)
                    else:
                        Notifiy_Window.Notify_window(8,self.frame_root,self.master,self.df,2,self.user)

            ##lower rate limit, upper rate limit, pulsewidth, Ventricular amplitude
        except ValueError:
            Notifiy_Window.Notify_window(8,self.frame_root,self.master,self.df,2,self.user)
        ##save parameters
    def save_DDDR(self):
        try:
            success = True
            for j in range(0, 20, 2):
                if self.user == self.df.iat[j, 0]:  ##find user
                    self.data[1] = self.mode
                    if int(self.entry_Lowerlim.get()) in range(45, 66):
                        self.df.at[j, 'DDDR Lower Rate Limit'] = int(self.entry_Lowerlim.get())
                        #self.data[2] = int(self.entry_Lowerlim.get())
                    else:
                        success = False
                    if int(self.entry_Upperlim.get()) in range(120, 151):
                        self.df.at[j, 'DDDR Upper Rate Limit'] = int(self.entry_Upperlim.get())
                        #self.data[3] = int(self.entry_Upperlim.get())
                    else:
                        success = False
                    if int(self.entry_Pulse_Width.get()) in range(1, 11):
                        self.df.at[j, 'DDDR Ventricular Pulse Width'] = int(self.entry_Pulse_Width.get())
                        self.data[6] = int(self.entry_Pulse_Width.get())
                    else:
                        success = False
                    if int(self.entry_AV_Amp.get()) in range(50, 101):
                        self.df.at[j, 'DDDR Ventricular Amplitude'] = int(self.entry_AV_Amp.get())
                        self.data[5] = int(self.entry_AV_Amp.get())
                        self.data[5] = int(self.entry_AV_Amp.get())
                    else:
                        success = False
                    #if int(self.entry_AV_Amp.get()) >= 65 and int(self.entry_AV_Amp.get()) <= 70:
                     #   self.df[self.df['Users'].iloc[i], 'DOOR Atrial Amplitude'] = int(self.entry_AV_Amp.get())
                   # if int(self.entry_Pulse_Width.get()) in range(1, 11):
                    #    self.df[self.df['Users'].iloc[i], 'DOOR Atrial Pulse Width'] = int(self.entry_Pulse_Width.get())
                    if int(self.entry_AV_del.get()) >= 70 and int(self.entry_AV_del.get()) <= 300:
                        self.df.at[j, 'DDDR Fixed AV Delay'] = int(self.entry_AV_del.get())
                        self.data[4] = int(self.entry_AV_del.get())
                    else:
                        success = False
                    if int(self.entry_Rate_Smooth()) in range(0, 101):
                        self.df.at[j, 'DDDR Rate Smoothing'] = int(self.entry_Rate_Smooth.get())
                        #self.data[16] = int(self.entry_Rate_Smooth.get())
                    else:
                        success = False
                    if int(self.entry_Act_Thres.get()) > 10:
                        self.df.at[j, 'DDDR Activity Threshold'] = int(self.entry_Act_Thres.get())
                        self.data[9] = int(self.entry_Act_Thres.get())
                    else:
                        success = False
                    if int(self.entry_React_Time.get()) >= 10 and int(self.entry_React_Time.get()) <= 15:
                        self.df.at[j, 'DDDR Reaction Time'] = int(self.entry_React_Time.get())
                        self.data[10] = int(self.entry_React_Time.get())
                    else:
                        success = False
                    if int(self.entry_Resp_Fact.get()) >= 1 and int(self.entry_Resp_Fact.get()) <= 16:
                        self.df.at[j, 'DDDR Response Factor'] = int(self.entry_Resp_Fact.get())
                        self.data[11] = int(self.entry_Resp_Fact.get())
                    else:
                        success = False
                    if int(self.entry_Recv_Time.get()) >= 2 and int(self.entry_Recv_Time.get()) <= 16:
                        self.df.at[j, 'DDDR Recovery Time'] = int(self.entry_Recv_Time.get())
                        self.data[12] = int(self.entry_Recv_Time.get())
                    else:
                        success = False
                    if int(self.entry_VRP.get()) >= 150 and int(self.entry_VRP.get()) <= 300:
                        self.df.at[j, 'DDDR VRP'] = int(self.entry_VRP.get())
                        self.data[8] = int(self.entry_VRP.get())
                        #self.data[14] = int(self.entry_VRP.get())
                    else:
                        success = False
                    #if int(self.entry_ARP.get()) in range(150, 301):
                    #    self.df[self.df['Users'].iloc[i], 'DDDR ARP'] = int(self.entry_ARP.get())
                    if int(self.entry_AV_Sensor_Rate.get()) in range(50, 176):
                        self.df.at[j, 'DDDR Sensor Rate'] = int(self.entry_AV_Sensor_Rate.get())
                        self.data[5] = int(self.entry_AV_Sensor_Rate.get())
                    else:
                        success = False
                    if int(self.entry_Dyn_AV_Delay.get()) in range(0, 2):
                        self.df.at[j, 'DDDR Dynamic AV Delay'] = int(self.entry_Dyn_AV_Delay.get())
                        self.data[7] = int(self.entry_Dyn_AV_Delay.get())
                    else:
                        success = False
                    if int(self.entry_AV_Delay_Off1.get()) in range(10, 101) or int(self.entry_AV_Delay_Off1.get()) == 0:
                        self.df.at[j, 'DDDR Sensed AV Delay Offset'] = int(self.entry_AV_Delay_Off1.get())
                        self.data[8] = int(self.entry_AV_Delay_Off1.get())
                    else:
                        success = False
                    if int(self.entry_AV_Sens.get()) in range(1, 11):
                        self.df.at[j, 'DDDR Ventricular Sensitivity'] = int(self.entry_AV_Sens.get())
                        self.data[12] = int(self.entry_AV_Sens.get())
                        self.data[13] = int(self.entry_AV_Sens.get())
                    else:
                        success = False
                    #if int(self.entry_AV_Sens.get()) in range(1, 11):
                        #self.df[self.df['Users'].iloc[i], 'DDDRR Atrial Sensitivity'] = int(self.entry_AV_Sens.get())
                    if int(self.entry_ATR_Fallback_Mode.get()) in range(0, 2):
                        self.df.at[j, 'DDDR ATR Fallback Mode'] = int(self.entry_ATR_Fallback_Mode.get())
                        self.df[18] = int(self.entry_ATR_Fallback_Mode.get())
                    else:
                        success = False
                    if int(self.entry_ATR_Fallback_time.get()) in range(1, 6):
                        self.df.at[j, 'DDDR ATR Fallback Time'] = int(self.entry_ATR_Fallback_time.get())
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
                        Notifiy_Window.Notify_window(8,self.frame_root,self.master,self.df,2,self.user)
        except ValueError:
            Notifiy_Window.Notify_window(8)
    ##save parameters

    def writeParameters(self):
        try:
            tosend = struct.pack('<BBBBHBBBHdBBB', self.data[0], self.data[1],self.data[2], self.data[3], self.data[4], self.data[5], self.data[6], self.data[7], self.data[8]
        , self.data[9], self.data[10], self.data[11], self.data[12])
        #BBBBBBHHBBBBHBBBHBdB
            self.transList = [0]*len(tosend)
            i = 0
            while i < len(tosend):
                self.transList[i] = tosend[i]
                i += 1
            for i in range(500):
                self.board.write(self.transList)
                print('f')
            Notifiy_Window.Notify_window(2, self.frame_root, self.master, self.df, 2, self.user)

        except:
            Notifiy_Window.Notify_window(9, 0,0,0,2,0)

    def showVOO(self):
        #show old parameters
        for j in range(0, 20, 2):
            if self.df.at[j, 'Users']  == self.user:
                if pd.isnull(self.df.at[j, 'VOO Lower Rate Limit']):
                    pass
                else:
                    self.entry_Lowerlim.insert(0, str(int(self.df.at[j, 'VOO Lower Rate Limit'])))
                if pd.isnull(self.df.at[j, 'VOO Upper Rate Limit']):
                    pass
                else:
                    self.entry_Upperlim.insert(0, str(int(self.df.at[j, 'VOO Upper Rate Limit'])))
                if pd.isnull(self.df.at[j, 'VOO Upper Rate Limit']):
                    pass
                else:
                    self.entry_Pulse_Width.insert(0, str(int(self.df.at[j, 'VOO Pulse Width'])))
                if pd.isnull(self.df.at[j, 'VOO Ventricular Amplitude']):
                    pass
                else:
                    self.entry_AV_Amp.insert(0, str(int(self.df.at[j, 'VOO Ventricular Amplitude'])))
                if pd.isnull(self.df.at[j, 'VOO Target BPM']):
                    pass
                else:
                    self.entry_BPM.insert(0, str(int(self.df.at[j, 'VOO Target BPM'])))

    def showAOO(self):
        #show old parameters
        for j in range(0, 20, 2):
            if self.df.iat[j, 0] == self.user:
                if pd.isnull(self.df.at[j, 'AOO Lower Rate Limit']):
                    pass
                else:
                    self.entry_Lowerlim.insert(0, str(int(self.df.at[j,'AOO Lower Rate Limit'])))#])']#[self.df['Users'].iloc[i], 'AOO Lower Rate Limit'])
                if pd.isnull(self.df.at[j, 'AOO Upper Rate Limit']):
                    pass
                else:
                    self.entry_Upperlim.insert(0, str(int(self.df.at[j, 'AOO Upper Rate Limit'])))
                if pd.isnull(self.df.at[j, 'AOO Pulse Width']):
                    pass
                else:
                    self.entry_Pulse_Width.insert(0, str(int(self.df.at[j, 'AOO Pulse Width'])))
                if pd.isnull(self.df.at[j, 'AOO Atrial Amplitude']):
                    pass
                else:
                    self.entry_AV_Amp.insert(0, str(int(self.df.at[j, 'AOO Atrial Amplitude'])))
                if pd.isnull(self.df.at[j, 'AOO Target BPM']):
                    pass
                else:
                    self.entry_BPM.insert(0, str(int(self.df.at[j, 'AOO Target BPM'])))

    def showVVI(self):
        # show old parameters
        for j in range(0, 20, 2):
            if self.df.iat[j, 0] == self.user:
                if pd.isnull(self.df.at[j, 'VVI Lower Rate Limit']):
                    pass
                else:
                    self.entry_Lowerlim.insert(0, str(int(self.df.at[j, 'VVI Lower Rate Limit'])))
                if pd.isnull(self.df.at[j, 'VVI Upper Rate Limit']):
                    pass
                else:
                    self.entry_Upperlim.insert(0, str(int(self.df.at[j, 'VVI Upper Rate Limit'])))
                if pd.isnull(self.df.at[j, 'VVI Pulse Width']):
                    pass
                else:
                    self.entry_Pulse_Width.insert(0, str(int(self.df.at[j, 'VVI Pulse Width'])))
                if pd.isnull(self.df.at[j, 'VVI Ventricular Amplitude']):
                    pass
                else:
                    self.entry_AV_Amp.insert(0, str(int(self.df.at[j, 'VVI Ventricular Amplitude'])))
                if pd.isnull(self.df.at[j, 'VVI Ventricular Sensitivity']):
                    pass
                else:
                    self.entry_AV_Sens.insert(0, str(int(self.df.at[j, 'VVI Ventricular Sensitivity'])))
                if pd.isnull(self.df.at[j, 'VVI VRP']):
                    pass
                else:
                    self.entry_VRP.insert(0, str(int(self.df.at[j, 'VVI VRP'])))
                if pd.isnull(self.df.at[j, 'VVI Rate Smoothing']):
                    pass
                else:
                    self.entry_Rate_Smooth.insert(0, str(int(self.df.at[j, 'VVI Rate Smoothing'])))
                if pd.isnull(self.df.at[j, 'VVI Target BPM']):
                    pass
                else:
                    self.entry_BPM.insert(0, str(int(self.df.at[j, 'VVI Target BPM'])))

    def showAAI(self):
        # show old parameters
        for j in range(0, 20, 2):
            if self.df.iat[j, 0] == self.user:
                if pd.isnull(self.df.at[j, 'AAI Lower Rate Limit']):
                    pass
                else:
                    self.entry_Lowerlim.insert(0, str(int(self.df.at[j, 'AAI Lower Rate Limit'])))
                if pd.isnull(self.df.at[j, 'AAI Upper Rate Limit']):
                    pass
                else:
                    self.entry_Upperlim.insert(0, str(int(self.df.at[j, 'AAI Upper Rate Limit'])))
                if pd.isnull(self.df.at[j, 'AAI Pulse Width']):
                    pass
                else:
                    self.entry_Pulse_Width.insert(0, str(int(self.df.at[j, 'AAI Pulse Width'])))
                if pd.isnull(self.df.at[j, 'AAI Atrial Amplitude']):
                    pass
                else:
                    self.entry_AV_Amp.insert(0, str(int(self.df.at[j, 'AAI Atrial Amplitude'])))
                if pd.isnull(self.df.at[j, 'AAI Atrial Sensitivity']):
                    pass
                else:
                    self.entry_AV_Sens.insert(0, str(int(self.df.at[j, 'AAI Atrial Sensitivity'])))
                if pd.isnull(self.df.at[j, 'AAI ARP']):
                    pass
                else:
                    self.entry_ARP.insert(0, str(int(self.df.at[j, 'AAI ARP'])))
                if pd.isnull(self.df.at[j, 'AAI Rate Smoothing']):
                    pass
                else:
                    self.entry_Rate_Smooth.insert(0, str(int(self.df.at[j, 'AAI Rate Smoothing'])))
                if pd.isnull(self.df.at[j, 'AAI Target BPM']):
                    pass
                else:
                    self.entry_BPM.insert(0, str(int(self.df.at[j, 'AAI Target BPM'])))

    def showDOO(self):
        # show old parameters
        for j in range(0, 20, 2):
            if self.df.iat[j, 0] == self.user:
                if pd.isnull(self.df.at[j, 'DOO Lower Rate Limit']):
                    pass
                else:
                    self.entry_Lowerlim.insert(0, str(int(self.df.at[j, 'DOO Lower Rate Limit'])))
                if pd.isnull(self.df.at[j, 'DOO Upper Rate Limit']):
                    pass
                else:
                    self.entry_Upperlim.insert(0, str(int(self.df.at[j, 'DOO Upper Rate Limit'])))
                if pd.isnull(self.df.at[j, 'DOO Ventrical Pulse Width']):
                    pass
                else:
                    self.entry_Pulse_Width.insert(0, str(int(self.df.at[j, 'DOO Ventricular Pulse Width'])))
                if pd.isnull(self.df.at[j, 'DOO Ventricular Amplitude']):
                    pass
                else:
                    self.entry_AV_Amp.insert(0, str(int(self.df.at[j, 'DOO Ventricular Amplitude'])))
                if pd.isnull(self.df.at[j, 'DOO Fixed AV Delay']):
                    pass
                else:
                    self.entry_AV_Delay.insert(0, str(int(self.df.at[j, 'DOO Fixed AV Delay'])))
                if pd.isnull(self.df.at[j, 'DOO Target BPM']):
                    pass
                else:
                    self.entry_BPM.insert(0, str(int(self.df.at[j, 'DOO Target BPM'])))

    def showAOOR(self):
        # show old parameters
        for j in range(0, 20, 2):
            if self.df.iat[j, 0] == self.user:
                if pd.isnull(self.df.at[j, 'AOOR Lower Rate Limit']):
                    pass
                else:
                    self.entry_Lowerlim.insert(0, str(int(self.df.at[j, 'AOOR Lower Rate Limit'])))
                if pd.isnull(self.df.at[j, 'AOOR Upper Rate Limit']):
                    pass
                else:
                    self.entry_Upperlim.insert(0, str(int(self.df.at[j, 'AOOR Upper Rate Limit'])))
                if pd.isnull(self.df.at[j, 'AOOR Pulse Width']):
                    pass
                else:
                    self.entry_Pulse_Width.insert(0, str(int(self.df.at[j, 'AOOR Pulse Width'])))
                if pd.isnull(self.df.at[j, 'AOOR Atrial Amplitude']):
                    pass
                else:
                    self.entry_AV_Amp.insert(0, str(int(self.df.at[j, 'AOOR Atrial Amplitude'])))

                if pd.isnull(self.df.at[j, 'AOOR Activity Threshold']):
                    pass
                else:
                    self.entry_Act_Thres.insert(0, str(float(self.df.at[j, 'AOOR Activity Threshold'])))
                if pd.isnull(self.df.at[j, 'AOOR Reaction Time']):
                    pass
                else:
                    self.entry_React_Time.insert(0, str(int(self.df.at[j, 'AOOR Reaction Time'])))
                if pd.isnull(self.df.at[j, 'AOOR Response Factor']):
                    pass
                else:
                    self.entry_Resp_Fact.insert(0, str(int(self.df.at[j, 'AOOR Response Factor'])))
                if pd.isnull(self.df.at[j, 'AOOR Recovery Time']):
                    pass
                else:
                    self.entry_Recv_Time.insert(0, str(int(self.df.at[j, 'AOOR Recovery Time'])))
                if pd.isnull(self.df.at[j, 'AOOR Target BPM']):
                    pass
                else:
                    self.entry_BPM.insert(0, str(int(self.df.at[j, 'AOOR Target BPM'])))
                if pd.isnull(self.df.at[j, 'AOOR Sensor Rate']):
                    pass
                else:
                    self.entry_AV_Sensor_Rate.insert(0, str(int(self.df.at[j, 'AOOR Sensor Rate'])))

    def showAAIR(self):
        #old
        for j in range(0, 20, 2):
            if self.df.iat[j, 0] == self.user:
                if pd.isnull(self.df.at[j, 'AAIR Lower Rate Limit']):
                    pass
                else:
                    self.entry_Lowerlim.insert(0, str(int(self.df.at[j, 'AAIR Lower Rate Limit'])))
                if pd.isnull(self.df.at[j, 'AAIR Upper Rate Limit']):
                    pass
                else:
                    self.entry_Upperlim.insert(0, str(int(self.df.at[j, 'AAIR Upper Rate Limit'])))
                if pd.isnull(self.df.at[j, 'AAIR Pulse Width']):
                    pass
                else:
                    self.entry_Pulse_Width.insert(0, str(int(self.df.at[j, 'AAIR Pulse Width'])))
                if pd.isnull(self.df.at[j, 'AAIR Atrial Amplitude']):
                    pass
                else:
                    self.entry_AV_Amp.insert(0, str(int(self.df.at[j, 'AAIR Atrial Amplitude'])))
                if pd.isnull(self.df.at[j, 'AAIR Sensor Rate']):
                    pass
                else:
                    self.entry_AV_Sensor_Rate.insert(0, str(int(self.df.at[j, 'AAIR Sensor Rate'])))
                if pd.isnull(self.df.at[j, 'AAIR Atrial Sensitivity']):
                    pass
                else:
                    self.entry_AV_Sens.insert(0, str(int(self.df.at[j, 'AAIR Atrial Sensitivity'])))
                if pd.isnull(self.df.at[j, 'AAIR Rate Smoothing']):
                    pass
                else:
                    self.entry_Rate_Smooth.insert(0, str(int(self.df.at[j, 'AAIR Rate Smoothing'])))
                if pd.isnull(self.df.at[j, 'AAIR Activity Threshold']):
                    pass
                else:
                    self.entry_Act_Thres.insert(0, str(float(self.df.at[j, 'AAIR Activity Threshold'])))
                if pd.isnull(self.df.at[j, 'AAIR Reaction Time']):
                    pass
                else:
                    self.entry_React_Time.insert(0, str(int(self.df.at[j, 'AAIR Reaction Time'])))
                if pd.isnull(self.df.at[j, 'AAIR Response Factor']):
                    pass
                else:
                    self.entry_Resp_Fact.insert(0, str(int(self.df.at[j, 'AAIR Response Factor'])))
                if pd.isnull(self.df.at[j, 'AAIR Recovery Time']):
                    pass
                else:
                    self.entry_Recv_Time.insert(0, str(int(self.df.at[j, 'AAIR Recovery Time'])))
                if pd.isnull(self.df.at[j, 'AAIR ARP']):
                    pass
                else:
                    self.entry_ARP.insert(0, str(int(self.df.at[j, 'AAIR ARP'])))
                if pd.isnull(self.df.at[j, 'AAIR Target BPM']):
                    pass
                else:
                    self.entry_BPM.insert(0, str(int(self.df.at[j, 'AAIR Target BPM'])))

    def showVOOR(self):
        # show old parameters
        for j in range(0, 20, 2):
            if self.df.iat[j, 0] == self.user:
                if pd.isnull(self.df.at[j, 'VOOR Lower Rate Limit']):
                    pass
                else:
                    self.entry_Lowerlim.insert(0, str(int(self.df.at[j, 'VOOR Lower Rate Limit'])))
                if pd.isnull(self.df.at[j, 'VOOR Upper Rate Limit']):
                    pass
                else:
                    self.entry_Upperlim.insert(0, str(int(self.df.at[j, 'VOOR Upper Rate Limit'])))
                if pd.isnull(self.df.at[j, 'VOOR Pulse Width']):
                    pass
                else:
                    self.entry_Pulse_Width.insert(0, str(int(self.df.at[j, 'VOOR Pulse Width'])))
                if pd.isnull(self.df.at[j, 'VOOR Ventricular Amplitude']):
                    pass
                else:
                    self.entry_AV_Amp.insert(0, str(int(self.df.at[j, 'VOOR Ventricular Amplitude'])))
                if pd.isnull(self.df.at[j, 'VOOR Activity Threshold']):
                    pass
                else:
                    self.entry_Act_Thres.insert(0, str(float(self.df.at[j, 'VOOR Activity Threshold'])))
                if pd.isnull(self.df.at[j, 'VOOR Reaction Time']):
                    pass
                else:
                    self.entry_React_Time.insert(0, str(int(self.df.at[j, 'VOOR Reaction Time'])))
                if pd.isnull(self.df.at[j, 'VOOR Response Factor']):
                    pass
                else:
                    self.entry_Resp_Fact.insert(0, str(int(self.df.at[j, 'VOOR Response Factor'])))
                if pd.isnull(self.df.at[j, 'VOOR Recovery Time']):
                    pass
                else:
                    self.entry_Recv_Time.insert(0, str(int(self.df.at[j, 'VOOR Recovery Time'])))
                if pd.isnull(self.df.at[j, 'VOOR Sensor Rate']):
                    pass
                else:
                    self.entry_AV_Sensor_Rate.insert(0, str(int(self.df.at[j, 'VOOR Sensor Rate'])))
                if pd.isnull(self.df.at[j, 'VOOR Target BPM']):
                    pass
                else:
                    self.entry_BPM.insert(0, str(int(self.df.at[j, 'VOOR Target BPM'])))

    def showVVIR(self):
        #show old
        for j in range(0, 20, 2):
            if self.df.iat[j, 0] == self.user:
                if pd.isnull(self.df.at[j, 'VVIR Lower Rate Limit']):
                    pass
                else:
                    self.entry_Lowerlim.insert(0, str(int(self.df.at[j, 'VVIR Lower Rate Limit'])))
                if pd.isnull(self.df.at[j, 'VVIR Upper Rate Limit']):
                    pass
                else:
                    self.entry_Upperlim.insert(0, str(int(self.df.at[j, 'VVIR Upper Rate Limit'])))
                if pd.isnull(self.df.at[j, 'VVIR Pulse Width']):
                    pass
                else:
                    self.entry_Pulse_Width.insert(0, str(int(self.df.at[j, 'VVIR Pulse Width'])))
                if pd.isnull(self.df.at[j, 'VVIR Ventricular Amplitude']):
                    pass
                else:
                    self.entry_AV_Amp.insert(0, str(int(self.df.at[j, 'VVIR Ventricular Amplitude'])))
                if pd.isnull(self.df.at[j, 'VVIR Sensor Rate']):
                    pass
                else:
                    self.entry_AV_Sensor_Rate.insert(0, str(int(self.df.at[j, 'VVIR Sensor Rate'])))
                if pd.isnull(self.df.at[j, 'VVIR Ventricular Sensitivity']):
                    pass
                else:
                    self.entry_AV_Sens.insert(0, str(int(self.df.at[j, 'VVIR Ventricular Sensitivity'])))
                if pd.isnull(self.df.at[j, 'VVIR Rate Smoothing']):
                    pass
                else:
                    self.entry_Rate_Smooth.insert(0, str(int(self.df.at[j, 'VVIR Rate Smoothing'])))
                if pd.isnull(self.df.at[j, 'VVIR Activity Threshold']):
                    pass
                else:
                    self.entry_Act_Thres.insert(0, str(float(self.df.at[j, 'VVIR Activity Threshold'])))
                if pd.isnull(self.df.at[j, 'VVIR Reaction Time']):
                    pass
                else:
                    self.entry_React_Time.insert(0, str(int(self.df.at[j, 'VVIR Reaction Time'])))
                if pd.isnull(self.df.at[j, 'VVIR Response Factor']):
                    pass
                else:
                    self.entry_Resp_Fact.insert(0, str(int(self.df.at[j, 'VVIR Response Factor'])))
                if pd.isnull(self.df.at[j, 'VVIR Recovery Time']):
                    pass
                else:
                    self.entry_Recv_Time.insert(0, str(int(self.df.at[j, 'VVIR Recovery Time'])))
                if pd.isnull(self.df.at[j, 'VVIR VRP']):
                    pass
                else:
                    self.entry_VRP.insert(0, str(int(self.df.at[j, 'VVIR VRP'])))
                if pd.isnull(self.df.at[j, 'VVIR Target BPM']):
                    pass
                else:
                    self.entry_BPM.insert(0, str(int(self.df.at[j, 'VVIR Target BPM'])))

    def showDOOR(self):
        #show old
        for j in range(0, 20, 2):
            if self.df.iat[j, 0] == self.user:
                if pd.isnull(self.df.at[j, 'DOOR Lower Rate Limit']):
                    pass
                else:
                    self.entry_Lowerlim.insert(0, str(int(self.df.at[j, 'DOOR Lower Rate Limit'])))
                if pd.isnull(self.df.at[j, 'DOOR Upper Rate Limit']):
                    pass
                else:
                    self.entry_Upperlim.insert(0, str(int(self.df.at[j, 'DOOR Upper Rate Limit'])))
                if pd.isnull(self.df.at[j, 'DOOR Ventrical Pulse Width']):
                    pass
                else:
                    self.entry_Pulse_Width.insert(0, str(int(self.df.at[j, 'DOOR Ventrical Pulse Width'])))
                if pd.isnull(self.df.at[j, 'DOOR Ventricular Amplitude']):
                    pass
                else:
                    self.entry_AV_Amp.insert(0, str(int(self.df.at[j, 'DOOR Ventricular Amplitude'])))
                if pd.isnull(self.df.at[j, 'DOOR Fixed AV Delay']):
                    pass
                else:
                    self.entry_AV_Delay.insert(0, str(int(self.df.at[j, 'DOOR Fixed AV Delay'])))
                #if pd.isnull(self.df.at[j, 'DOOR Rate Smoothing']):
                 #   pass
                #else:
                 #   self.entry_Rate_Smooth.insert(0, str(int(self.df.at[j, 'DOOR Rate Smoothing'])))
                if pd.isnull(self.df.at[j, 'DOOR Activity Threshold']):
                    pass
                else:
                    self.entry_Act_Thres.insert(0, str(float(self.df.at[j, 'DOOR Activity Threshold'])))
                if pd.isnull(self.df.at[j, 'DOOR Reaction Time']):
                    pass
                else:
                    self.entry_React_Time.insert(0, str(int(self.df.at[j, 'DOOR Reaction Time'])))
                if pd.isnull(self.df.at[j, 'DOOR Response Factor']):
                    pass
                else:
                    self.entry_Resp_Fact.insert(0, str(int(self.df.at[j, 'DOOR Response Factor'])))
                if pd.isnull(self.df.at[j, 'DOOR Recovery Time']):
                    pass
                else:
                    self.entry_Recv_Time.insert(0, str(int(self.df.at[j, 'DOOR Recovery Time'])))
                if pd.isnull(self.df.at[j, 'DOOR Target BPM']):
                    pass
                else:
                    self.entry_BPM.insert(0, str(int(self.df.at[j, 'DOOR Target BPM'])))
                if pd.isnull(self.df.at[j, 'DOOR Sensor Rate']):
                    pass
                else:
                    self.entry_AV_Sensor_Rate.insert(0, str(int(self.df.at[j, 'DOOR Sensor Rate'])))

    def showDDDR(self):
        for j in range(0, 20, 2):
            if self.df.iat[j, 0] == self.user:
                if pd.isnull(self.df.at[j, 'DDDR Lower Rate Limit']):
                    pass
                else:
                    self.entry_Lowerlim.insert(0, str(int(self.df.at[j, 'DDDR Lower Rate Limit'])))
                if pd.isnull(self.df.at[j, 'DDDR Upper Rate Limit']):
                    pass
                else:
                    self.entry_Upperlim.insert(0, str(int(self.df.at[j, 'DDDR Upper Rate Limit'])))
                if pd.isnull(self.df.at[j, 'DDDR Ventrical Pulse Width']):
                    pass
                else:
                    self.entry_Pulse_Width.insert(0, str(int(self.df.at[j, 'DDDR Ventrical Pulse Width'])))
                if pd.isnull(self.df.at[j, 'DDDR Ventricular Amplitude']):
                    pass
                else:
                    self.entry_AV_Amp.insert(0, str(int(self.df.at[j, 'DDDR Ventricular Amplitude'])))
                if pd.isnull(self.df.at[j, 'DDDR Fixed AV Delay']):
                    pass
                else:
                    self.entry_AV_Delay.insert(0, str(int(self.df.at[j, 'DDDR Fixed AV Delay'])))
                if pd.isnull(self.df.at[j, 'DDDR Rate Smoothing']):
                    pass
                else:
                    self.entry_Rate_Smooth.insert(0, str(int(self.df.at[j, 'DDDR Rate Smoothing'])))
                if pd.isnull(self.df.at[j, 'DDDR Activity Threshold']):
                    pass
                else:
                    self.entry_Act_Thres.insert(0, str(float(self.df.at[j, 'DDDR Activity Threshold'])))
                if pd.isnull(self.df.at[j, 'DDDR Reaction Time']):
                    pass
                else:
                    self.entry_React_Time.insert(0, str(int(self.df.at[j, 'DDDR Reaction Time'])))
                if pd.isnull(self.df.at[j, 'DDDR Response Factor']):
                    pass
                else:
                    self.entry_Resp_Fact.insert(0, str(int(self.df.at[j, 'DDDR Response Factor'])))
                if pd.isnull(self.df.at[j, 'DDDR Recovery Time']):
                    pass
                else:
                    self.entry_Recv_Time.insert(0, str(int(self.df.at[j, 'DDDR Recovery Time'])))
                if pd.isnull(self.df.at[j, 'DDDR VRP']):
                    pass
                else:
                    self.entry_VRP.insert(0, str(int(self.df.at[j, 'DDDR VRP'])))
                if pd.isnull(self.df.at[j, 'DDDR Sensor Rate']):
                    pass
                else:
                    self.entry_AV_Sensor_Rate.insert(0, str(int(self.df.at[j, 'DDDR Sensor Rate'])))
                if pd.isnull(self.df.at[j, 'DDDR Dynamic AV Delay']):
                    pass
                else:
                    self.entry_Dyn_AV_Delay.insert(0, str(int(self.df.at[j, 'DDDR Dynamic AV Delay'])))
                if pd.isnull(self.df.at[j, 'DDDR Sensed AV Delay Offset']):
                    pass
                else:
                    self.entry_AV_Delay_Off1.insert(0, str(int(self.df.at[j, 'DDDR Sensed AV Delay Offset'])))
                if pd.isnull(self.df.at[j, 'DDDR Ventricular Sensitivity']):
                    pass
                else:
                    self.entry_AV_Sens.insert(0, str(int(self.df.at[j, 'DDDR Ventricular Sensitivity'])))
                if pd.isnull(self.df.at[j, 'DDDR ATR Fallback Mode']):
                    pass
                else:
                    self.entry_ATR_Fallback_Mode.insert(0, str(int(self.df.at[j, 'DDDR ATR Fallback Mode'])))
                if pd.isnull(self.df.at[j, 'DDDR ATR Fallback Time']):
                    pass
                else:
                    self.entry_ATR_Fallback_time.insert(0, str(int(self.df.at[j, 'DDDR ATR Fallback Time'])))
                if pd.isnull(self.df.at[j, 'DDDR Target BPM']):
                    pass
                else:
                    self.entry_BPM.insert(0, str(int(self.df.at[j, 'DDDR Target BPM'])))

def openSerial():
    s = Serial()
    s.port = 'COM6'
    s.baudrate = 115200
    s.timeout = 0.5
    s.dtr = 0
    s.open()
    state = s.isOpen()
    return s


