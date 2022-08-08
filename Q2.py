# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 21:03:14 2021

@author: Latitude E5430
"""

weight_in_pounds = eval(input("Enter your weight in pounds : "))
height_in_inches = eval(input("Enter your height in inches:"))
weight_in_kg = weight_in_pounds * 0.45356237
height_in_meters = height_in_inches *0.0254
BMI = weight_in_kg/(height_in_meters)**2
print("The BMI is:" ,BMI)
if BMI<=18.5:
    print("Under weight")
elif BMI >= 18.5 and BMI <= 29.9:
    print("Normal")
elif BMI > 25.0 and BMI <= 29.9:
    print("Over weight")
elif BMI > 30:
    print("Obese")