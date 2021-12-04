# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 16:44:32 2021

@author: duy
"""

import speech_recognition 
#robot noi 
robot_ear = speech_recognition.Recognizer()
#with : giup cho roboot nghe xong thi mic tu ta
with speech_recognition.Microphone() as mic:
    print("Robot:I'm listening")
    #am thanhh dc khoi tao = viec robot tiep thu tu mic
    audio = robot_ear.listen(mic)
#bat loi
try:
    you = robot_ear.recognize_google(audio)
except:
    you=""
    
print("You : "+you)