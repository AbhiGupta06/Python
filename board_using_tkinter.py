# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 10:26:37 2019

@author: BSDU
"""

#3x3 board using tkinter

import tkinter 

root = tkinter.Tk()

for r in range(3):
    for c in range(3):
        tkinter.Label(root, text='Row%s/Col%s '%(r,c), borderwidth=1).grid(row=r, column=c)

root.mainloop()