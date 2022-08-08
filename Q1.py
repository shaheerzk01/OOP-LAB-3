# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 20:51:21 2021

@author: Latitude E5430
"""

import random 
number1 = random.randint(1,10)
number2 = random.randint(1,10)
if number2 > number1:
    number2 = number2 + number1
    number1 = number2 - number1
    number2 = number2 - number1
    print(number1, "-", number2)
    b = number1 - number2
    a = int(input("Subtract the given number and write the answer : "))
    if a==b:
        print("your answer is correct")
    else:
        print("your answer is false")
elif number1 > number2:
    print(number1, "-", number2)
    b = number1 - number2
    a = int(input("Subtract the given number and write the answer : "))
    if a==b:
        print("your answer is correct")
    else:
        print("your answer is false")   