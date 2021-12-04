# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 20:22:25 2021

@author: duy
"""

import speech_recognition
from datetime import date
import pyttsx3

#mieng
robot_mouth = pyttsx3.init()
#nao
robot_brain = ""
#robot noi 
robot_ear = speech_recognition.Recognizer()
#with : giup cho roboot nghe xong thi mic tu ta
while True:
        with speech_recognition.Microphone() as mic:
            print("Robot:I'm listening")
            #am thanhh dc khoi tao = viec robot tiep thu tu mic
            audio = robot_ear.listen(mic)
            
            print("Robot ....")
        #bat loi
        try:
            you = robot_ear.recognize_google(audio)
        except:
            you=""
            
        print("You : "+you)
    
        if you == "":
            robot_brain = "I can't hear you, try again"
        elif "hello" in you:
            robot_brain = "Hello"
        elif "today" in you:
            today = date.today()
            robot_brain = today.strftime("%B %d, %Y")
        elif "time" in you:
            now = date.now()
            robot_brain = now.strftime("%H hours %M minutes %S seconds")
        elif "name" in you:
            robot_brain = "My name robot"
        elif "how old are you" in you:
            robot_brain = "I'm fine, thank you"
        elif "handsome" in you:
            robot_brain = "I don't know this !!!"
        elif "bye" in you:
            robot_brain = "Goodbye, see you again"
            print("Robot : "+ robot_brain)
            robot_mouth.say(robot_brain)
            robot_mouth.runAndWait()
            break
        else:
            robot_brain = "hmmmmm....."
        print("Robot : "+ robot_brain)
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()