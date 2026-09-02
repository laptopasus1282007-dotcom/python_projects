#This is my 2nd Project.
# Number Guessing Game.

import random

number= random.randint(1,100)
attempts = 0
max_attempts = 6

print("Guess the number between 1 and 100!")

while attempts < max_attempts :
    guess = int(input("Enter Your Guess : "))
    attempts = attempts+1
    max_attempts = 6

    if guess < number :
        print("Too Low ! Try again.")
    elif guess > number :
        print("Too High ! Try again.")
    else :
        print(f"Correct ! You guessed it in {attempts} attempts.")
        break
else :
    print(f"Game Over! The Number was {number}.")

"""output :-

Guess the number between 1 and 100!
Enter Your Guess : 12
Too Low ! Try again.
Enter Your Guess : 50
Too Low ! Try again.
Enter Your Guess : 80
Too Low ! Try again.
Enter Your Guess : 91
Correct ! You guessed it in 4 attempts."""