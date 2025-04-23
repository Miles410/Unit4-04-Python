#!/usr/bin/env python3
# Created By: Boluwatife Dada
# created on April 16
# This program generates a random correct guess. It then uses a loop to keep asking the user to guess the number until they guess correctly


import random


def guessing_game():
    """Plays a number guessing game with the user."""
    secret_number = random.randint(1, 100)  # Generate a random number between 1 and 100
    attempts = 0

    print("Welcome to the Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        try:
            guess_str = input("Take a guess: ")
            guess = int(guess_str)
            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(
                    f"Congratulations! You guessed the number in {attempts} attempts."
                )
                break  # Exit the loop when the guess is correct

        except ValueError:
            print("Invalid input. Please enter a whole number.")


if __name__ == "__main__":
    guessing_game()
