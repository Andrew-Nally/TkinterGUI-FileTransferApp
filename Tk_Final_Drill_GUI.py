from tkinter import *
import tkinter as tk

import Tk_Final_Drill_Func

""" This will create and place the app
    widgets and buttons and the database
    will be created if one doesnt already exist
"""
def load_gui(self):
    # create an entry text box and a source button and set  to a default string
    self.srcEntryBox = StringVar()
    self.srcEntryBox.set('Select a source directory')
    self.srctxt = tk.Entry(self.master, width=60, textvariable=self.srcEntryBox)
    self.srctxt.grid(row=0, column=0, rowspan=1, columnspan=2, padx=(5, 0),pady=(10, 20))
    self.srcBtn = tk.Button(self.master, width=12, height=1, text="Source",command=lambda: Tk_Final_Drill_Func.select_src(self))
    self.srcBtn.grid(row=0, column=2, padx=(10, 0), pady=(10, 20))

    # create an entry text box for destination button and set to a default string
    self.destEntryBox = StringVar()
    self.destEntryBox.set('Select a destination directory')
    self.desttxt = tk.Entry(self.master, width=60, textvariable=self.destEntryBox)
    self.desttxt.grid(row=1, column=0, rowspan=1, columnspan=2, padx=(5, 0), pady=(10, 20))
    self.destBtn = tk.Button(self.master, width=12, height=1, text="Destination",command=lambda: Tk_Final_Drill_Func.select_dest(self))
    self.destBtn.grid(row=1, column=2, padx=(10, 0), pady=(10, 20))
    
    # create and place a transfer button and the done button
    
    self.trnsBtn = tk.Button(self.master, width=16, height=2, text="Transfer Files",command=lambda: \
                             Tk_Final_Drill_Func.move_files(self,self.srcEntryBox, self.destEntryBox))
    self.trnsBtn.grid(row=2, column=0, padx=(0, 0), pady=(10, 10))
    self.DoneBtn = tk.Button(self.master, width=16, height=2, text="Done",command=lambda: Tk_Final_Drill_Func.close(self))
    self.DoneBtn.grid(row=2, column=1, padx=(0, 0), pady=(10, 10))

    # connect to the database and create the table if it doesn't exist
    Tk_Final_Drill_Func.create_db(self)


if __name__ == "__main__":
    pass
