# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 16:03:15 2021

@author: duy
"""
import pyttsx3
engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()