# -*- coding: utf-8 -*-
"""
Created on Tue Nov 16 21:17:42 2021

@author: Latitude E5430
"""

import random
lottery=random.randint(11,23)
print(lottery)
guess=eval(input("Enter your guess:"))
lottery_tens=lottery//10
lottery_ones=lottery%10
guess_tens=guess//10
guess_ones=guess%10
print("The lottery number was",lottery)
if lottery == guess:
    print("The reward is $10,000")
else:
    if (lottery_tens == guess_ones and lottery_ones == guess_tens):
        print("you won 3000$")
    elif (guess_tens == lottery_tens or guess_ones == lottery_tens or guess_tens == lottery_ones):
        print("you won 1000$")
    else:
        print("sorry Better luck next time")