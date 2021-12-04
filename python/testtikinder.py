# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 11:29:20 2021

@author: duy
"""
from tkinter import *
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename(filetypes=(("docx file",".docx"),("all file","."))) # show an "Open" dialog box and return the path to the selected file
print(filename)