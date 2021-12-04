# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 10:46:56 2021

@author: duy
"""

import fasttext

# Skipgram model :

file = "cooking.train"

classifier = fasttext.train_supervised(file)
label = classifier.predict("Why not put knives in the dishwasher?", k=3)
print(label)

