import os
import numpy as np
import hashlib
import time

from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askdirectory


class Frame():
    def __init__(self,init_window_name):
        self.init_window_name = init_window_name

    #Set Windows
    def set_init_window(self):
        self.init_window_name.title("File Generators")           #Windows name
        self.init_window_name.geometry('800x180')
        self.init_window_name.resizable(width=False,height=False)   # Stable Width

        # Button
        self.init_open_path = Button(self.init_window_name, text="Choose Image Path",  command=self.open_button)
        self.init_open_path.place(x=20,  y=10,anchor='nw')

        self.init_generate = Button(self.init_window_name, text="Generate",  command=self.generate_button)
        self.init_generate.place(x=20,  y=130,anchor='nw')

        # Label
        self.init_input_name_label = Label(self.init_window_name, text="input file's name" )
        self.init_input_name_label.place(x=20,  y=50,anchor='nw')

        self.init_input_counts_label = Label(self.init_window_name, text="input file's counts" )
        self.init_input_counts_label.place(x=20,  y=90,anchor='nw')

        # Entry
        self.init_path_entry = Entry(self.init_window_name, textvariable="", width=80)  # Input Content
        self.init_path_entry.place(x=160,  y=10,anchor='nw')

        self.init_name_entry = Entry(self.init_window_name, textvariable="", width=20)  # Input Content
        self.init_name_entry.place(x=140,  y=50,anchor='nw')

        self.init_counts_entry = Entry(self.init_window_name, textvariable="", width=20)  # Input Content
        self.init_counts_entry.place(x=140,  y=90,anchor='nw')

    def open_button(self):
        filename = askdirectory()
        if filename != '':
            a = self.init_path_entry.get() + filename            
            self.init_path_entry.delete(0, len(self.init_path_entry.get()))
            self.init_path_entry.insert(0, a)
    
    def generate_button(self):
        if self.init_path_entry.get() == "":
            messagebox.showinfo("Error", "Please give a directory")
        elif self.init_name_entry.get() == "": 
            messagebox.showinfo("Error", "Please give a name")            
        elif self.init_counts_entry.get() == "":
            messagebox.showinfo("Error", "Please give a counts")
        else:
            try:
                for n in range (int(self.init_counts_entry.get())):
                    os.mkdir( str(self.init_path_entry.get()) + "\\" + str(self.init_name_entry.get()) + str(n))   
            except:
                messagebox.showinfo("Error", "Please give a correct number to the counts")



def frame():
    init_window = Tk()           
    ZMJ_PORTAL = Frame(init_window)
    ZMJ_PORTAL.set_init_window()
    init_window.mainloop()

if __name__ == '__main__':
    frame()

