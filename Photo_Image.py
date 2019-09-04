# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 11:46:42 2019

@author: BSDU
"""

import tkinter 

window = tkinter.Tk()
window.title("GUI")


icon = tkinter.PhotoImage(file ="E:\\ML\card.jpg")

label = tkinter.Label(window, image = icon)
label.pack()

window.mainloop()