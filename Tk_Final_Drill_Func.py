import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog


import datetime
import os
import shutil
import sqlite3
import time


def close(self):
  ##ask user if they want to exit the program, if user selects yes, computer will kill the program
    
    if messagebox.askokcancel("Exit Program",
                              "Are you sure you want to close the application?"):
        self.master.destroy()
        os._exit(0)

## this will establish and create the database if it desnt already exist
def create_db(self):
  
    conn = sqlite3.connect('Tk_Files.db')
    with conn:
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS modified_times(unix REAL)")
        conn.commit()
        c.close()
    conn.close()

    def read_db(self):
        ##WIll read the table and populate the widget with the last time the file was modified             
        conn = sqlite3.connect('Tk_Files.db')
        with conn:
            c = conn.cursor()
            c.execute("SELECT MAX(unix)FROM modified_times")
            most_recent = c.fetchone()[0]
            most_recent = time.ctime(most_recent)
            c.close()
        conn.close()
        self.label_print = tk.Label(self.master, width=60, height=2, text="Last modified: {}".format(most_recent))
        self.label_print.grid(row=3, column=0, rowspan=1, columnspan=3, padx=(0, 0), pady=(10, 10))

    read_db(self)

## thrse two Entry Boxes will open the os file system on the computer to select the folder for the source and destination directories
def select_src(self):
    self.srctxt.delete(0, 60)
    self.srcEntryBox = filedialog.askdirectory()
    self.srctxt.insert(0, self.srcEntryBox)


def select_dest(self):
    self.desttxt.delete(0, 60)
    self.destEntryBox = filedialog.askdirectory()
    self.desttxt.insert(0, self.destEntryBox)

##this will transfer the txt files and compare their last modified timestamp, if it was mofified within the last 24  hours
##it will be moved to the desitnation firectory. A pop up wiill congratulate their success and enter a timestampto the db 'Tk_FIles.db'
##from the source to the destination directory
def move_files(self, source, destination):
    now = datetime.datetime.now()
    ago = now - datetime.timedelta(hours=24)
    print('The following .txt files were modified in the last 24 hours: \n')

    for files in os.listdir(source):
        if files.endswith('.txt'):
            path = os.path.join(source, files)
            st = os.stat(path)
            mtime = datetime.datetime.fromtimestamp(st.st_mtime)
            if mtime > ago:
                print('{} ~ last modified {}'.format(path, mtime))
                file_source = os.path.join(source, files)
                file_destination = os.path.join(destination, files)
                shutil.move(file_source, file_destination)
                print("\tMoved {} to {}.\n".format(files, destination))

    current_time = time.time()
    conn = sqlite3.connect('Tk_Files.db')
    with conn:
        c = conn.cursor()
        c.execute("INSERT INTO modified_times VALUES({})".format(current_time))
        conn.commit()
        c.close()
    conn.close()

    messagebox.showinfo("File Transfer", "Success!")


## this willl read the table and populate the widget
    def read_db(self):
        conn = sqlite3.connect('Tk_Files.db')
        with conn:
            c = conn.cursor()
            c.execute("SELECT MAX(unix) FROM modified_times")
            most_recent = c.fetchone()[0]
            most_recent = time.ctime(most_recent)
            c.close()
        conn.close()

        self.label_print = tk.Label(self.master, width=60, height=2, text="Last modified: {}".format(most_recent))
        self.label_print.grid(row=3, column=0, rowspan=1, columnspan=3, padx=(0, 0), pady=(10, 10))

    read_db(self)
