"""We are going to write a program that generates a random number and asks the user 
to guess it.

If the player's guess is higher than the actual number, the program displays "Lower number
please". 
Similarly, if the user's guess is too low, the program prints "higher number please"
 When the user guesses the correct number, 
the program displays the number of guesses the player used to arrive at the number.

Hint: Use the random module. """

import random

def guess_number():
    guess_count = 0
    actual_number = random.randint(1, 20)

    while True:
        n = int(input("Enter your guessed number: "))
        guess_count += 1

        if n < actual_number:
            print("Higher number please")

        elif n > actual_number:
            print("Lower number please")

        else:
            print("You successfully guessed the number")
            print("Number of guesses:", guess_count)
            break

guess_number()