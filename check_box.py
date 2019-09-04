# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 11:42:25 2019

@author: BSDU
"""

from tkinter import *

master = Tk()

var1 = IntVar() 
Checkbutton(master, text='Male', variable=var1).grid(row=0, sticky=W)

var2 = IntVar()
Checkbutton(master, text='Female', variable=var2).grid(row=1, sticky=W)

root.mainloop()

