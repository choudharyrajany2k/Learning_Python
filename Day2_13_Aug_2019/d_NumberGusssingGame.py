#!/usr/bin/python
"""
Purpose: Number Gussing game
"""
LUCKY_NUMBER = 67
guessing_number = int(input("Guessing Number: "))

if guessing_number==LUCKY_NUMBER:
    print("Congrats! Your guess is right")
elif guessing_number > LUCKY_NUMBER:
    print('lower your guess!')
else:
    print('Increase your guess')