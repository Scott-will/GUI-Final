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
#################################
import winsound
from tkinter import *
import tkinter as tk
import pickle


def save_users(list_of_users):  ##writing users to file
    f = open("Users.txt", 'wb')  # opens file then dumps users into file
    pickle.dump(list_of_users, f)
    f.close()
    list_of_users = read_users()
    print(list_of_users)
    print("su")
    return list_of_users


def read_users():  # reading saved users from txt file
    list_of_users = []
    try:
        f = open("Users.txt", 'rb')  # opens file
        while True:
            try:
                list_of_users = pickle.load(f)  ##reading data from file if not end of file
            except EOFError:
                break
        f.close()
    except IOError:
        f = open("Users.txt", 'w+')
        f.close()
    return list_of_users


def read_last_login():  ##reading last user saved if remember me is checked
    last_login = []
    try:
        f2 = open("Remembered.txt", 'rb')  ##opens file
        while True:
            try:
                last_login = pickle.load(f2)  ##reads file while not end of file
            except EOFError:
                break
        f2.close()
    except IOError:
        f2 = open("Remembered.txt", 'w+')
        f2.close()

    return last_login


def add_user(list_of_users, username, password):  ##adding a user
    try:
        if len(list_of_users) < 20:  ##check if not max number of users
            not_found = True
            for i in range(0, len(list_of_users) - 1, 2):
                if username == list_of_users[i]:
                    not_found = False
                    Notify_window(1)
                    break
            if not_found == True:  ##ERRROR IS SOMEWHERE HERE
                list_of_users.append(username)
                list_of_users.append(password)  # append login info
        else:
            Notify_window(7)  ##error window
    except TypeError:
        list_of_users = []
        list_of_users.append(username)
        list_of_users.append(password)
        print(list_of_users)
        print("au")
    return list_of_users


class Login_Window:  # Class for the create of the main login window
    def __init__(self, master):  ##initializes the class, root is the master

        # We will be using the same root window and placing and removing frames different frames, every class will
        # have its own frame
        self.frame_root = Frame(master, width=500, height=500)
        self.frame_root.pack()
        self.master = master

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
        self.checkbutton_remember.config(command=self.remember_me)
        self.checkbutton_remember.place(x=165, y=400)
        self.get_old_users()  ##gets old user login info if remember me is checked,

        # Block for the creation of the buttons for the login frame
        self.button_login = Button(self.frame_root, text="Login",
                                   command=self.pacing_screen)  # command = self.check_user(self.entry_user.get(), self.entry_pass.get()))
        self.button_login.place(x=170, y=425)
        # self.button_login.config(command=self.check_user(self.entry_user.get(), self.entry_pass.get()))
        self.button_create = Button(self.frame_root, text="New User", command=self.new_user_window)
        self.button_create.place(x=235, y=425)

    def remember_me(self):  ##function called when remember me box ix checked, saves user to a file
        if self.check_state_var.get() == 1:  ##checks if remember me is checked adds info to dump to file
            to_dump = [self.entry_user.get(), self.entry_pass.get(), self.check_state_var.get()]
            f = open("Remembered.txt", 'wb')
            pickle.dump(to_dump, f)  ##dumps info
            f.close()
        if self.check_state_var.get() == 0:
            to_dump = []
            f = open("Remembered.txt", 'wb')
            pickle.dump(to_dump, f)  ##dumps info
            f.close()

    def pacing_screen(self):  ##calls pacing screen
        password = self.entry_pass.get()
        username = self.entry_user.get()
        list_of_users = read_users()
        success = 0  ##variable to check if need to call error window
        try:
            for i in range(0, len(list_of_users) - 1, 2):  # checks if user exists and password is correct
                if list_of_users[i] == username:
                    if password == list_of_users[i + 1]:
                        self.frame_root.pack_forget()
                        self.PacingScreen = Pacing_Window(self.master, username)
                        success = 1
        except TypeError:
            pass
        if success == 0:
            Error = Notify_window(6)  ##user does not exist

    def new_user_window(self):  # calls new user screen
        self.frame_root.pack_forget()
        self.NewUserWindow = New_User_Window(self.master, list_of_users)

    def get_old_users(self):
        try:
            old_user = []
            f2 = open("Remembered.txt", "rb")
            while True:
                try:
                    old_user = (pickle.load(f2))  # reads old user login info while not end of file
                except EOFError:
                    break
            f2.close()
            try:
                if old_user[2] == 1:  ##checks if remembered me is checked
                    self.entry_user.insert(10, old_user[0])  # inserts into user and password entry spot
                    self.entry_pass.insert(10, old_user[1])
                    self.check_state_var.set(1)
            except IndexError:
                pass
            except TypeError:
                old_user = []  ##does nothing
        except IOError:
            f2 = open("Remembered.txt", 'w+')
            old_user = []
            f2.close()


# This calls is for the window where new users register. This class has the same structure as the login Window class
class New_User_Window:
    def __init__(self, master, list_of_users):
        ##frame definition
        self.frame_root = Frame(master, width=500, height=500)
        self.frame_root.pack()
        self.list_of_users = list_of_users
        self.master = master

        # buttons and text defintiions
        self.background_image = tk.PhotoImage(file="backgroundpacing.png")
        self.label = Label(self.frame_root, image=self.background_image)
        self.label.image = self.background_image
        self.label.pack()

        self.entry_username = Entry(self.frame_root)
        self.entry_username.place(x=200, y=300)
        self.label_username = Label(self.frame_root, text="UserID:")
        self.label_username.place(x=155, y=300)

        self.entry_password = Entry(self.frame_root)
        self.entry_password.config(show="*")
        self.entry_password.place(x=200, y=330)
        self.label_password = Label(self.frame_root, text="Password:")
        self.label_password.place(x=140, y=330)

        self.entry_password_confirmation = Entry(self.frame_root)
        self.entry_password_confirmation.place(x=200, y=360)
        self.entry_password_confirmation.config(show="*")
        self.label_password_confirmation = Label(self.frame_root, text="Confirm Password:")
        self.label_password_confirmation.place(x=95, y=360)

        self.button_username = Button(self.frame_root, text="Create")
        self.button_username.place(x=200, y=390)
        self.button_username.config(command=self.create_user)
        self.button_cancel = Button(self.frame_root, text="Cancel")
        self.button_cancel.config(command=self.from_new_user)
        self.button_cancel.place(x=250, y=390)

    def from_new_user(self):  # Transition function from new user window to the login screen
        self.frame_root.pack_forget()
        self.LoginScreen = Login_Window(self.master)

    def create_user(self):  # We take the collected username and password and save them
        username = self.entry_username.get()
        password = self.entry_password.get()
        password_confirm = self.entry_password_confirmation.get()
        if password == password_confirm:
            self.list_of_users = add_user(self.list_of_users, username, password)
            list_of_users = save_users(self.list_of_users)
            print(list_of_users)
            self.from_new_user()  ##goes back to login screen
        else:
            error = Notify_window(4)


class Notify_window():  # Class to warn users of errors various errors or to notify them of a conformation
    # If you want to add more errors or conformations, start a new block of if and elif cases
    # Use this class for any notifications that require a separate window
    def __init__(self, error):
        winsound.PlaySound("sound.wav", winsound.SND_ASYNC)  # Basic windows error sound to notify users
        box = Tk()  # Creating a separate tk window for the errors
        box.geometry('300x100')
        box.resizable(0, 0)
        # Button for closing the error window
        Ok_button = Button(box, text="        OK        ", command=box.destroy)
        Ok_button.place(x=110, y=50)

        # Add more statements if you have more errors to throw, please label the errors
        ## need a window to: show file writing was success && paramaters saved
        if error == 1:  # For no username entered in register
            error1_label = Label(box, text="Username already exists")
            error1_label.place(x=80, y=20)

        elif error == 2:  # For no password entered in register
            error2_label = Label(box, text="Please enter a password")
            error2_label.place(x=80, y=20)

        elif error == 3:  # For no confirm password in register
            error3_label = Label(box, text="Please confirm your password")
            error3_label.place(x=80, y=20)

        elif error == 4:  # For non matching passwords entered in register
            error4_label = Label(box, text="Passwords do not match")
            error4_label.place(x=80, y=20)

        elif error == 5:  # For successful creation of new user
            created_label = Label(box, text="Registration confrimed!")
            created_label.place(x=80, y=20)

        elif error == 6:  # Either password or username is incorrect
            error6_label = Label(box, text="Username or Password is incorrect")
            error6_label.place(x=80, y=20)

        elif error == 7:  # Already have 10 users registered
            error7_label = Label(box, text="There are already 10 users")
            error7_label.place(x=80, y=20)

        elif error == 8:  #
            error8_label = Lable(box, text="Invalid input")


# Class for the pacing window screen, again this follows the basic structure as the other classes for frame creation
class Pacing_Window:
    def __init__(self, master, user):
        self.frame_root = Frame(master, width=500, height=500)
        self.frame_root.pack()
        self.background_image = tk.PhotoImage(file="backgroundpacing1.png")
        self.label = Label(self.frame_root, image=self.background_image)
        self.label.image = self.background_image
        self.label.pack()
        self.text = Label(self.frame_root, text="Please select a Pacing mode")
        self.text.config(font=("Courier", 15))
        self.text.place(x=95, y=150)
        self.user = user
        self.master = master

        self.signout_image = tk.PhotoImage(file="signout.png")
        self.button_signout = Button(self.frame_root, image=self.signout_image)
        self.button_signout.config(command=self.from_Pacing_Window)
        self.button_signout.place(x=400, y=50)

        self.AOO_image = tk.PhotoImage(file="AOO.png")
        self.AOO_button = Button(self.frame_root, image=self.AOO_image)
        self.AOO_button.config(command=self.To_Parameters1)
        self.AOO_button.place(x=100, y=200)

        self.VOO_image = tk.PhotoImage(file="VOO.png")
        self.VOO_button = Button(self.frame_root, image=self.VOO_image)
        self.VOO_button.config(command=self.To_Parameters2)
        self.VOO_button.place(x=100, y=300)

        self.AAI_image = tk.PhotoImage(file="AAI.png")
        self.AAI_button = Button(self.frame_root, image=self.AAI_image)
        self.AAI_button.config(command=self.To_Parameters3)
        self.AAI_button.place(x=300, y=200)

        self.VVI_image = tk.PhotoImage(file="VVI.png")
        self.VVI_button = Button(self.frame_root, image=self.VVI_image)
        self.VVI_button.config(command=self.To_Parameters4)
        self.VVI_button.place(x=300, y=300)

    def from_Pacing_Window(self):  # Transition function from new user window to the login screen
        self.frame_root.pack_forget()
        self.LoginScreen = Login_Window(self.master)

    # These 4 methods will display the appropriate texts depending on which mode was pressed on the pacing screen
    def To_Parameters1(self):
        self.frame_root.pack_forget()
        self.ParameterWindow = Parameter_Window(self.master, 1, self.user)

    def To_Parameters2(self):
        self.frame_root.pack_forget()
        self.ParameterWindow = Parameter_Window(self.master, 2, self.user)

    def To_Parameters3(self):
        self.frame_root.pack_forget()
        self.ParameterWindow = Parameter_Window(self.master, 3, self.user)

    def To_Parameters4(self):
        self.frame_root.pack_forget()
        self.ParameterWindow = Parameter_Window(self.master, 4, self.user)


# Class for the frame where the parameters are edited
class Parameter_Window:
    def __init__(self, master, mode, user):
        self.frame_root = Frame(master, width=1500, height=500)
        self.frame_root.pack()
        self.mode = mode
        self.user = user
        self.master = master
        self.parameters = self.old_parameters()

        # The following 4 modes will display the correct set of titles depending on which pacing mode the user wants to
        # edit
        if self.mode == 1:
            self.background_image = tk.PhotoImage(file="backgroundpacingAOOVOO.png")
            self.label = Label(self.frame_root, image=self.background_image)
            self.label.image = self.background_image
            self.label.pack()
            # comman's parameters are the x and y coordinates for the various widgets it creates
            self.common(125, 172, 125, 222, 30, 220, 30, 170, 300, 50, 300, 350, 300, 300)

            self.label_title1 = Label(self.frame_root, text="AOO Pacing Mode")
            self.label_title1.config(font=("Courier", 11))
            self.label_title1.place(x=130, y=145)
            self.label_Atr_Amp = Label(self.frame_root, text="Atrial Amplitude:")
            self.label_Atr_Amp.place(x=30, y=270)
            self.label_Atr_Pulse = Label(self.frame_root, text="Atrial Pulse Width:")
            self.label_Atr_Pulse.place(x=24, y=320)
            self.label_Atr_Sens = Label(self.frame_root, text="Atrial Sensitivity:")
            self.label_Atr_Sens.place(x=30, y=370)
            self.label_ARP = Label(self.frame_root, text="ARP:")
            self.label_ARP.place(x=93, y=420)
            self.label_PVARP = Label(self.frame_root, text="PVARP:")
            self.label_PVARP.place(x=80, y=470)

            self.entry_Atr_Amp = Entry(self.frame_root)
            self.entry_Atr_Amp.place(x=125, y=270)
            self.entry_Atr_Pulse = Entry(self.frame_root)
            self.entry_Atr_Pulse.place(x=125, y=320)
            self.entry_Atr_Sens = Entry(self.frame_root)
            self.entry_Atr_Sens.place(x=125, y=370)
            self.entry_ARP = Entry(self.frame_root)
            self.entry_ARP.place(x=125, y=420)
            self.entry_PVARP = Entry(self.frame_root)
            self.entry_PVARP.place(x=125, y=470)

            self.write_parameters()


        elif self.mode == 2:
            self.background_image = tk.PhotoImage(file="backgroundpacingAOOVOO.png")
            self.label = Label(self.frame_root, image=self.background_image)
            self.label.image = self.background_image
            self.label.pack()

            self.common(155,192,155,242,60,240,60,190,300,50,300,310,300,260)

            self.label_title2 = Label(self.frame_root, text="VOO Pacing Mode")
            self.label_title2.config(font=("Courier", 15))
            self.label_title2.place(x=100, y=150)
            self.label_Vent_Amp = Label(self.frame_root, text="Ventricle Amplitude:")
            self.label_Vent_Amp.place(x=40, y=292)
            self.label_Vent_Pulse = Label(self.frame_root, text="Ventricle Pulse Width:")
            self.label_Vent_Pulse.place(x=33, y=342)

            self.entry_Vent_Amp = Entry(self.frame_root)
            self.entry_Vent_Amp.place(x=155, y=292)
            self.entry_Vent_Pulse = Entry(self.frame_root)
            self.entry_Vent_Pulse.place(x=155, y=342)
            self.write_parameters()


        elif self.mode == 3:

            self.background_image = tk.PhotoImage(file="backgroundpacingVIIAAI.png")
            self.label = Label(self.frame_root, image=self.background_image)
            self.label.image = self.background_image
            self.label.pack()

            self.common(155, 192, 155, 242, 60, 240, 60, 190, 430, 100, 400, 420, 400, 370)

            self.label_title3 = Label(self.frame_root, text="AAI Pacing Mode")
            self.label_title3.config(font=("Courier", 15))
            self.label_title3.place(x=200, y=150)
            self.label_Atr_Amp = Label(self.frame_root, text="Atrial Amplitude:")
            self.label_Atr_Amp.place(x=57, y=342)
            self.label_Atr_Pulse = Label(self.frame_root, text="Atrial Pulse Width:")
            self.label_Atr_Pulse.place(x=50, y=292)
            self.label_Atr_Sens = Label(self.frame_root, text="Atrial Sensitivity:")
            self.label_Atr_Sens.place(x=62, y=392)
            self.label_ARP = Label(self.frame_root, text="ARP:")
            self.label_ARP.place(x=125, y=442)
            self.label_PVARP = Label(self.frame_root, text="PVARP:")
            self.label_PVARP.place(x=365, y=192)
            self.label_Hyst = Label(self.frame_root, text="Hysteresis:")
            self.label_Hyst.place(x=345, y=242)
            self.label_Rate_Smooth = Label(self.frame_root, text="Rate Smoothing:")
            self.label_Rate_Smooth.place(x=315, y=292)

            self.entry_Atr_Pulse = Entry(self.frame_root)
            self.entry_Atr_Pulse.place(x=155, y=292)
            self.entry_Atr_Amp = Entry(self.frame_root)
            self.entry_Atr_Amp.place(x=155, y=342)
            self.entry_Atr_Sens = Entry(self.frame_root)
            self.entry_Atr_Sens.place(x=155, y=392)
            self.entry_ARP = Entry(self.frame_root)
            self.entry_ARP.place(x=155, y=442)

            self.entry_PVARP = Entry(self.frame_root)
            self.entry_PVARP.place(x=410, y=192)
            self.entry_Hyst = Entry(self.frame_root)
            self.entry_Hyst.place(x=410, y=242)
            self.entry_Rate_Smooth = Entry(self.frame_root)
            self.entry_Rate_Smooth.place(x=410, y=292)

            self.write_parameters()


        elif self.mode == 4:
            self.background_image = tk.PhotoImage(file="backgroundpacingVIIAAI.png")
            self.label = Label(self.frame_root, image=self.background_image)
            self.label.image = self.background_image
            self.label.pack()

            self.common(180, 182, 180, 232, 85, 182, 85, 232, 430, 100, 400, 350, 400, 300)

            self.label_title4 = Label(self.frame_root, text="VII Pacing Mode")
            self.label_title4.config(font=("Courier", 12))
            self.label_title4.place(x=210, y=150)
            self.label_Vent_Amp = Label(self.frame_root, text="Ventricle Amplitude:")
            self.label_Vent_Amp.place(x=66, y=272)
            self.label_Vent_Pulse = Label(self.frame_root, text="Ventricle Pulse Width:")
            self.label_Vent_Pulse.place(x=60, y=322)
            self.label_Vent_Sens = Label(self.frame_root, text="Ventricle Sensitivity:")
            self.label_Vent_Sens.place(x=70, y=372)
            self.label_VRP = Label(self.frame_root, text="VRP:")
            self.label_VRP.place(x=150, y=422)
            self.label_Hyst = Label(self.frame_root, text="Hysteresis:")
            self.label_Hyst.place(x=335, y=172)
            self.label_Rate_Smooth = Label(self.frame_root, text="Rate Smoothing:")
            self.label_Rate_Smooth.place(x=317, y=222)

            self.entry_Vent_Amp = Entry(self.frame_root)
            self.entry_Vent_Amp.place(x=180, y=272)
            self.entry_Vent_Pulse = Entry(self.frame_root)
            self.entry_Vent_Pulse.place(x=180, y=322)
            self.entry_Vent_Sens = Entry(self.frame_root)
            self.entry_Vent_Sens.place(x=180, y=372)
            self.entry_VRP = Entry(self.frame_root)
            self.entry_VRP.place(x=180, y=422)
            self.entry_Hyst = Entry(self.frame_root)
            self.entry_Hyst.place(x=410, y=182)
            self.entry_Rate_Smooth = Entry(self.frame_root)
            self.entry_Rate_Smooth.place(x=410, y=232)
            self.write_parameters()

    # All widgets are created in common() are common between all 4 pacing mode. Because the layout for the window of
    # each mode is different we will just pass the x and y coord as parameters when the method is called
    def common(self, upperlimx, upperlimy, lowerlimx, lowerlimy, upperlimx2, upperlimy2, lowerlimx2, lowerlimy2, backx,
               backy, okx, oky, applyx, applyy):
        self.entry_Upperlim = Entry(self.frame_root)
        self.entry_Upperlim.place(x=upperlimx, y=upperlimy)
        self.entry_Lowerlim = Entry(self.frame_root)
        self.entry_Lowerlim.place(x=lowerlimx, y=lowerlimy)

        self.label_lowlim = Label(self.frame_root, text="Lower Rate limit:")
        self.label_lowlim.place(x=lowerlimx2, y=lowerlimy2)
        self.label_uplim = Label(self.frame_root, text="Upper Rate limit:")
        self.label_uplim.place(x=upperlimx2, y=upperlimy2)

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

    def from_Parameter_Window(self):  # Returns to the pacing screen
        self.frame_root.pack_forget()
        self.PacingWindow = Pacing_Window(self.master, self.user)

    def Apply(self):  # Apply will save the #parameters in the entry fields and return to the pacing screen
        self.frame_root.pack_forget()
        self.PacingWindow = Pacing_Window(self.master, self.user)
        # Add code here to also save the parameters

        self.save_parameters()

    def Ok(self):  # Ok will only save the parameters in the entry fields
        self.save_parameters()  # Just random code so pycharm doesnt freak out that there is nothing in the function
        # add code here to save the parameters

    def save_parameters(self):  ##saves parameters
        f = open("Parameters.txt", 'wb')
        ##check if file is empty,
        ##order is user, ul, ll, d, w, mode
        ##so search file to see if user exists (icrement by 6 6)
        ##if yes change data
        ##if no add user and data
        i = 0
        while True:
            try:
                if self.user == self.parameters[i]:  ##if user already has parameters, change them
                    self.parameters[i + 1] = self.entry_Upperlim.get()
                    self.parameters[i + 2] = self.entry_Lowerlim.get()
                    self.parameters[i + 3] = self.entry_Sensor_Rate.get()
                    self.parameters[i + 4] = self.entry_AV_Delay.get()
                    self.parameters[i + 5] = self.entry_Dyn_AV_Delay.get()
                    self.parameters[i + 6] = self.entry_AV_Delay_Off1.get()
                    self.parameters[i + 7] = self.entry_Atr_Amp.get()
                    self.parameters[i + 8] = self.entry_Vent_Amp.get()
                    self.parameters[i + 9] = self.entry_Atr_Pulse.get()
                    self.parameters[i + 10] = self.entry_Vent_Pulse.get()
                    self.parameters[i + 11] = self.entry_Vent_Sens.get()
                    self.parameters[i + 12] = self.entry_Atr_Sens.get()
                    self.parameters[i + 13] = self.entry_VRP.get()
                    self.parameters[i + 14] = self.entry_ARP.get()
                    self.parameters[i + 15] = self.entry_PVARP.get()
                    self.parameters[i + 16] = self.entry_PVARP_Ext.get()
                    self.parameters[i + 17] = self.entry_Hyst.get()
                    self.parameters[i + 18] = self.entry_Rate_Smooth.get()
                    self.parameters[i + 19] = self.entry_ATR_Dur.get()
                    self.parameters[i + 20] = self.entry_ATR_Fallback_Mode.get()
                    self.parameters[i + 21] = self.entry_Act_Thres.get()
                    self.parameters[i + 22] = self.entry_React_Time.get()
                    self.parameters[i + 23] = self.entry_Resp_Fact.get()
                    self.parameters[i + 24] = self.entry_Recv_Time.get()
                    self.parameters[i + 25] = self.mode
                    break
                else:
                    i = i + 26
            except EOFError:  ##if user not found add them and their data
                self.parameters.append(self.user)
                self.parameters.append(self.entry_Upperlim.get())
                self.parameters.append(self.entry_Lowerlim.get())
                self.parameters.append(self.entry_Sensor_Rate.get())
                self.parameters.append(self.entry_AV_Delay.get())
                self.parameters.append(self.entry_Dyn_AV_Delay.get())
                self.parameters.append(self.entry_AV_Delay_Off1.get())
                self.parameters.append(self.entry_Atr_Amp.get())
                self.parameters.append(self.entry_Vent_Amp.get())
                self.parameters.append(self.entry_Atr_Pulse.get())
                self.parameters.append(self.entry_Vent_Pulse.get())
                self.parameters.append(self.entry_Vent_Sens.get())
                self.parameters.append(self.entry_Atr_Sens.get())
                self.parameters.append(self.entry_VRP.get())
                self.parameters.append(self.entry_ARP.get())
                self.parameters.append(self.entry_PVARP.get())
                self.parameters.append(self.entry_PVARP_Ext.get())
                self.parameters.append(self.entry_Hyst.get())
                self.parameters.append(self.entry_Rate_Smooth.get())
                self.parameters.append(self.entry_ATR_Dur.get())
                self.parameters.append(self.entry_ATR_Fallback_Mode.get())
                self.parameters.append(self.entry_Act_Thres.get())
                self.parameters.append(self.entry_React_Time.get())
                self.parameters.append(self.entry_Resp_Fact.get())
                self.parameters.append(self.entry_Recv_Time.get())
                self.parameters.append(self.mode)
                break
            except IndexError:
                self.parameters.append(self.user)
                self.parameters.append(self.entry_Upperlim.get())
                self.parameters.append(self.entry_Lowerlim.get())
                self.parameters.append(self.entry_Sensor_Rate.get())
                self.parameters.append(self.entry_AV_Delay.get())
                self.parameters.append(self.entry_Dyn_AV_Delay.get())
                self.parameters.append(self.entry_AV_Delay_Off1.get())
                self.parameters.append(self.entry_Atr_Amp.get())
                self.parameters.append(self.entry_Vent_Amp.get())
                self.parameters.append(self.entry_Atr_Pulse.get())
                self.parameters.append(self.entry_Vent_Pulse.get())
                self.parameters.append(self.entry_Vent_Sens.get())
                self.parameters.append(self.entry_Atr_Sens.get())
                self.parameters.append(self.entry_VRP.get())
                self.parameters.append(self.entry_ARP.get())
                self.parameters.append(self.entry_PVARP.get())
                self.parameters.append(self.entry_PVARP_Ext.get())
                self.parameters.append(self.entry_Hyst.get())
                self.parameters.append(self.entry_Rate_Smooth.get())
                self.parameters.append(self.entry_ATR_Dur.get())
                self.parameters.append(self.entry_ATR_Fallback_Mode.get())
                self.parameters.append(self.entry_Act_Thres.get())
                self.parameters.append(self.entry_React_Time.get())
                self.parameters.append(self.entry_Resp_Fact.get())
                self.parameters.append(self.entry_Recv_Time.get())
                self.parameters.append(self.mode)
                break
        pickle.dump(self.parameters, f)
        f.close()

    def old_parameters(self):  ##gets the old parameters
        old_parameters = []
        try:
            f2 = open("Parameters.txt", 'rb')
            while True:
                try:
                    old_parameters = pickle.load(f2)
                except EOFError:
                    break
            f2.close()
        except IOError:
            f2 = open("Parameters.txt", 'w+')
            old_parameters = []
            f2.close()
        return old_parameters

    def write_parameters(self):
        i = 0
        while True:
            try:
                if self.user == self.parameters[i]:
                    if self.mode == self.parameters[i + 25]:
                        self.entry_Upperlim.insert(10, self.parameters[i + 1])
                        self.entry_Lowerlim.insert(10, self.parameters[i + 2])
                        self.entry_Sensor_Rate.insert(10, self.parameters[i + 3])
                        self.entry_AV_Delay.insert(10, self.parameters[i + 4])
                        self.entry_Dyn_AV_Delay.insert(10, self.parameters[i + 5])
                        self.entry_AV_Delay_Off1.insert(10, self.parameters[i + 6])
                        self.entry_Atr_Amp.insert(10, self.parameters[i + 7])
                        self.entry_Vent_Amp.insert(10, self.parameters[i + 8])
                        self.entry_Atr_Pulse.insert(10, self.parameters[i + 9])
                        self.entry_Vent_Pulse.insert(10, self.parameters[i + 10])
                        self.entry_Vent_Sens.insert(10, self.parameters[i + 11])
                        self.entry_Atr_Sens.insert(10, self.parameters[i + 12])
                        self.entry_VRP.insert(10, self.parameters[i + 13])
                        self.entry_ARP.insert(10, self.parameters[i + 14])
                        self.entry_PVARP.insert(10, self.parameters[i + 15])
                        self.entry_PVARP_Ext.insert(10, self.parameters[i + 16])
                        self.entry_Hyst.insert(10, self.parameters[i + 17])
                        self.entry_Rate_Smooth.insert(10, self.parameters[i + 18])
                        self.entry_ATR_Dur.insert(10, self.parameters[i + 19])
                        self.entry_ATR_Fallback_Mode.insert(10, self.parameters[i + 20])
                        self.entry_Act_Thres.insert(10, self.parameters[i + 21])
                        self.entry_React_Time.insert(10, self.parameters[i + 22])
                        self.entry_Resp_Fact.insert(10, self.parameters[i + 23])
                        self.entry_Recv_Time.insert(10, self.parameters[i + 24])

                        break
                    else:
                        break
                else:
                    i = i + 26
            except IndexError:
                break
            except TypeError:
                break


################################################################

list_of_users = read_users()
last_login = read_last_login()
