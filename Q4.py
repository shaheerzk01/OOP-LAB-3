# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 21:11:54 2021

@author: Latitude E5430
"""

import random 
b = random.randint(0,1)
a = int(input("Guess head as 0 or tail as 1 : "))
if a==b:
    print("Your guess is right")
else:
    print("Not right")