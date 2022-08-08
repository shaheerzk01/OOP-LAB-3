# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 20:34:48 2021

@author: Latitude E5430
"""

import random
computer_guess = random.randint(0,2)
print(computer_guess)
user_guess = int(input("Enter your guess : "))
if computer_guess == 0:
    scissor = computer_guess
    if user_guess == scissor:
        print("draw")
    elif user_guess == 1:
        print("User wins")
    elif user_guess == 2:
        print("computer wins")
elif computer_guess == 1:
    rock = computer_guess
    if user_guess == rock:
        print("Draw")
    elif user_guess == 0:
        print("computer wins")
    elif user_guess == 2:
        print("User wins")
elif computer_guess == 2:
    paper = computer_guess
    if user_guess == paper:
        print("Draw")
    elif user_guess == 0:
        print("user wins")
    elif user_guess == 1:
        print("computer wins")