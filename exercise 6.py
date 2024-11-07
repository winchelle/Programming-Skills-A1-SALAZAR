# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 16:31:07 2024

@author: winch
"""

"""
Exercise 6
Brute Force Attack
"""

password = '12345' #Declaring a variable.
password= (input("Enter the passcode: ")) #asking for user input.
attempts= 5 #password attempts.

while attempts >0: 
    attempts= attempts - 1 # Subtract 1 to the attempt when the input is wrong.
    if password != '12345': 
        print (f"You have {{{attempts}}} left, try again.") 
        password = (input ("Enter your passcode: "))
        if attempts <= 0 :
            print ("No more attempt left.")
    else: # When the user input is equal to the password it will unlocked.
        password == '12345'
        print ("You have unlocked the code!") 
        break
        


    

 


