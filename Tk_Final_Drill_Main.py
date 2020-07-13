#################
### 4/29/2020
### Python 3.8
##
#
### Andrew Nally
##
#
### Tkinter/Python Final Drill-- The Tech Academy
##
#
### File Transfer Application to move only '.txt' files
### modified within the last 24 hours from the source directory
### to the destination directory, and print the moved files
### with their absolute path name and time last modified to the console.
#########################################################################



from tkinter import *
import tkinter as tk

import Tk_Final_Drill_GUI

##creates the dimensions of the frame base and initiates the interface/application
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(495, 235)
        self.master.maxsize(495, 235)
        self.master.title("File Transfer Application")
        self.master.configure(bg="#F0F0F0")

        Tk_Final_Drill_GUI.load_gui(self)


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
