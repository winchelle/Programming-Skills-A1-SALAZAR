# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 16:59:18 2024

@author: winch
"""

"""
Exercise 3
Biography
"""

name=str(input("Enter your First Name: ")) # Ask for user first input.
mname=str(input("Enter your Surname: ")) # Ask for user second input.
print("You're name is", name + mname,", Nice to meet you!") # Print the first and second input.
hometown=str(input("Enter your hometown: ")) # Ask for use third input.
print("You're from the", hometown) # Print the user third input.

# If the user entered a str instead of int data, it will ask again the user input.
while True:
    age = input("How old are you? ") # Ask for fourth input.
    try:
        user_integer = int(age) # If the user input is == int,
        print ("You're", age, "years old.") # This output will show.
        break 
    except:
        name
        mname
        hometown


        
