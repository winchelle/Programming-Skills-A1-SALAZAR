# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 15:06:20 2024

@author: winch
"""

"""
Exercise 8
Simple Search
"""

name_list = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"] # A list of string name.

names = str(input("What's the name you're looking for? ")) # Asking for user input.

# If, Else when the name is == to name_list it will print the if command, 
# and if != to name_list it will print the else command.

if names in name_list:
    print ("The", names, "you're looking for is here", name_list.index(names))
   
else:
     print ("The", names, "you're looking for is not here.")
        
        
      