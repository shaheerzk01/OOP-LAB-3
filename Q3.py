# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 21:09:55 2021

@author: Latitude E5430
"""

a = int(input("Enter a year : "))
if a%4==0:
    if a%100==0:
        if a%400==0:
            print("It is a leap year")
        else:
            print("It is not leap year")
    else:
        print("It is not leap year")
else:
    print("It is not leap year")
    