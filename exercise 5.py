# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 14:45:15 2024

@author: winch
"""
"""
Exercise 5
Days of the Month
"""

month = int(input("What month? ")) # Ask for user input
year = int(input("What year? ")) # Ask for user input

# Dictionary of month with days.
days_dictionary = {'1' : 31,
                   '2' : 28,
                   '3' : 31,
                   '4' : 30,
                   '5' : 31,
                   '6' : 30,
                   '7' : 31,
                   '8' : 31,
                   '9' : 30,
                  '10' : 31,
                  '11' : 30,
                  '12' : 31
                  }

# Leap year formula
if (year % 4 == 0 ) and (not(year % 100 == 0)) or (year % 400 == 0): 
        leap_year = True  # if the year is a leap year, it will print the IF condition.             
        print ("This year", year, "and month", month, "is a leap year!") # Output of IF condition.
        breakpoint

else: # If the year is not leap year, it will print the ELSE condition.
   leap_year = False
   print (f"This {month} and year {year} is not a leap year.") # Output of ELSE condition
   
   if 1 <= month <=12: # The user input should not be greater than 12 and not less than 1.
       print (days_dictionary[str(month)],"days") # printing the user input.
       
   else: # Ex. if the user put 13 and up or 0 it will print the ELSE condition.
       print ("Please input a valid integer between 1 and 12.")

    
    



        



            