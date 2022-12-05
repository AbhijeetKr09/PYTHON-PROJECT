from random import randint
from art import logo
from brain import Brain

life = Brain()

print(logo)
def play():
    number = randint(1, 101)
    print("I'm thinking of a number between 1 and 100.")
    live = life.level()
    guess = 0
    while guess != number:
        print(f"You have {live} attempts remaining to guess the number.")
        user_guess = int(input("Guess the number: "))
        live = life.result(user_guess, number)
        guess = user_guess
        if live == 0:
            print(f"You've run out of guesses, you lose, number was {number}")
            return
        elif guess != number:
            print("Guess again.")

play()
