"""
Tristan Newey
2/26/2025
Homework 6 - Introduction
This program will take two numbers inputted by the user and provide the sum, difference, product, and quotient.
"""

# These are the user inputs for the numbers.
ans1 = input("Give me a number: ")
ans2 = input("Give me another number: ")

# These are the equations produced by the given numbers.
sum = int(ans1) + int(ans2)
diff = int(ans1) - int(ans2)
prod = int(ans1) * int(ans2)
quot = int(ans1) / int(ans2)

# These are what show up on the console to show the user the outputs.
print(f"{ans1} + {ans2} = {sum}")
print(f"{ans1} - {ans2} = {diff}")
print(f"{ans1} * {ans2} = {prod}")
print(f"{ans1} / {ans2} = {quot}")