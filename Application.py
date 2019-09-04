# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 10:14:05 2019

@author: BSDU
"""

import tkinter 

window = tkinter.Tk()
window.title("GUI")

def PrintOnClick():
    tkinter.Label(window, text="Welcome").pack()
    
tkinter.Button(window, text="Click Me", command = PrintOnClick).pack()


window.mainloop()