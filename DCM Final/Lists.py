
from tkinter import *
import tkinter as tk

class Parameter_List():
    def __init__(self):
        self.box = tk.Toplevel()  # Creating a separate tk window for the errors
        self.frame_root = Frame(self.box, width=500, height=500)
        self.frame_root.pack()


        # Here we are setting the background image for the window. line 46 creates a reference to the image as python
        # will garbage collect the image if there is no reference made
        self.background_image = tk.PhotoImage(file='Parameter_List.png')
        self.label = Label(self.frame_root, image=self.background_image)
        self.label.image = self.background_image
        self.label.pack()
        self.box.resizable(0, 0)

    def remove(self):
        self.box.destroy()




