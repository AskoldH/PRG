# -*- coding: utf-8 -*-
"""
Created on Tue Feb 05 11:49:29 2013

@author: Radek
"""

from tkinter import *

hlavni=Tk()
hodnota=IntVar()
hodnota.set(0)


def Nastav():
    l["text"]=str(hodnota.get())
    
w = Spinbox(hlavni, from_=-50, to=1000,increment=2,textvariable=hodnota,command=Nastav)
w.pack()

l=Label(text="0",font="Arial 20")
l.pack()

hlavni.mainloop()