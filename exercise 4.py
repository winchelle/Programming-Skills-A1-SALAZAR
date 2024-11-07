# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 14:27:18 2024

@author: winch
"""
"""
Exercise 4
Primitive Quiz
"""
#Dictionary of the 10 capitals of european countries.
capitals_of_european_countries = {"France":"Paris",
                                  "Italy":"Rome",
                                  "Spain":"Madrid",
                                  "Germany":"Berlin",
                                  "United Kingdom":"London",
                                  "Netherland" :"Amsterdam",
                                  "Belgium" :  "Brussels",
                                  "Portugal" :"Lisbon",
                                  "Austria" : "Vienna",
                                  "Greece":"Athens"
                                  }

# Initialize score
score = 0

# This loop will determine the right and wrong answer of the user.
for country, capital in capitals_of_european_countries.items():
    user_input = input(f"What is the capital of {country}? ").lower() # Converting user input to lowercase.
    
    if user_input == capital.lower():  # Compare with lowercase capital
        print(f"Correct! The capital of {country} is {capital}.")
    else:
        print(f"Incorrect. The correct answer is {capital}.")

# Printing the final score.
print(f"Your final score is: {score}/{len(capitals_of_european_countries)}")