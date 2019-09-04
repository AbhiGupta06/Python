# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 12:17:00 2019

@author: BSDU
"""

import tkinter as tk
import tkinter.messagebox as msg

user = tk.Tk()

def user1():
    msg.showinfo('Machine Learing' , "abhisheaK")

button = tk.Button(user, text='Button', width=20, command = user1)
button.pack()

user.mainloop()
    