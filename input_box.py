""" -*- coding: utf-8 -*-

#Created on Fri Aug 23 11:56:00 2019
#
#@author: BSDU
"""

from tkinter import *


Label(box, text='First Name').grid(row=0)
Label(box, text='Midle Name').grid(row=1)
Label(box, text='Last Name').grid(row=2)
Label(box, text='Address').grid(row=3)
Label(box, text='Email').grid(row = 4)

a1 = Entry(box)
a2 = Entry(box)
a3 = Entry(box)
a4 = Entry(box)
a5 = Entry(box)

a1.grid(row=0 , column=1)
a2.grid(row=1 , column=1)
a3.grid(row=2 , column=1)
a4.grid(row=3 , column=1)
#a5.grid(row=4 , column=1)



user.mainloop()

