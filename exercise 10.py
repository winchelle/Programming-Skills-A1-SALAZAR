# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 16:12:50 2024

@author: winch
"""

"""
Exercise 10
Is it even?
"""

num=int(input("Enter your number: ")) #asking for user input.


if num%2==0: # Formula for even.
    print("The number", num, "is Even") 
else: # When the number is not compatible with the formula it will print the ELSE command.
    print("The number", num, "is Odd")
