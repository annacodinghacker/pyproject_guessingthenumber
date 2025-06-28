#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      nayak
#
# Created:     05-04-2025
# Copyright:   (c) nayak 2025
# Licence:     <your licence>
#----------------------------------------------------------------------------
import random

def guess_the_number():
    print("🎯 Welcome to 'Guess the Number'!")
    print("I'm thinking of a number between 1 and 50.")

    number_to_guess = random.randint(1, 50)
    attempts = 0

    while True:
        try:
            guess = int(input("🔢 Enter your guess: "))
            attempts += 1

            if guess < number_to_guess:
                print("📉 Too low! Try again.")
            elif guess > number_to_guess:
                print("📈 Too high! Try again.")
            else:
                print(f"✅ Correct! The number was {number_to_guess}.")
                print(f"👏 You guessed it in {attempts} tries.")
                break
        except ValueError:
            print("❌ Please enter a valid number.")

if __name__ == "__main__":
    guess_the_number()

