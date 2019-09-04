# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 12:32:15 2019

@author: BSDU
"""


import tkinter as tk
from functools import partial

def call_result(label_result, n1, n2):
    num1 = (n1.get())
    num2 = (n2.get())
    result = int(num1)+int(num2)
    label_result.config(text="Result is %d" % result)
    return


def call_result(label_result, n1, n2):
    num1 = (n1.get())
    num2 = (n2.get())
    result = int(num1)-int(num2)
    label_result.config(text="Result is %d" % result)
    return


def call_result(label_result, n1, n2):
    num1 = (n1.get())
    num2 = (n2.get())
    result = int(num1)*int(num2)
    label_result.config(text="Result is %d" % result)
    return


def call_result(label_result, n1, n2):
    num1 = (n1.get())
    num2 = (n2.get())
    result = int(num1)%int(num2)
    label_result.config(text="Result is %d" % result)
    return



root = tk.Tk()
root.geometry('400x200+100+200')
root.title('Calculator-Addition')

number1 = tk.StringVar()
number2 = tk.StringVar()


labelTitle = tk.Label(root, text="Calculator-Addition").grid(row=0, column=2)


labelNum1 = tk.Label(root, text="Enter a Number").grid(row=1, column=0)
labelNum2 = tk.Label(root, text="Enter Another Number").grid(row=2, column=0)

labelResult = tk.Label(root)
labelResult.grid(row=7, column=2)

abelResult = tk.Label(root)
labelResult.grid(row=7, column=3)


abelResult = tk.Label(root)
labelResult.grid(row=7, column=4)


abelResult = tk.Label(root)
labelResult.grid(row=7, column=5)


enterNum1 = tk.Entry(root, textvariable=number1).grid(row=1, column=2)
enterNum2 = tk.Entry(root, textvariable=number2).grid(row=2, column=2)

call_result1 = partial(call_result, labelResult, number1, number2)
call_result2 = partial(call_result, labelResult, number1, number2)
call_result3 = partial(call_result, labelResult, number1, number2)
call_result4 = partial(call_result, labelResult, number1, number2)

buttonCal1 = tk.Button(root, text="Sum", command=call_result).grid(row=3, column=0)
buttonCal2 = tk.Button(root, text="Subtriction", command=call_result).grid(row=4, column=0)
buttonCal3 = tk.Button(root, text="Multipction", command=call_result).grid(row=5, column=0)
buttonCal4 = tk.Button(root, text="Divied", command=call_result).grid(row=6, column=0)

root.mainloop()

