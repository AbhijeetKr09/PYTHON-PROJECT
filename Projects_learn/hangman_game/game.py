import random as r
from hangman_words import word_list, pokedex
from hangman_art import logo, stages

# from replit import clear
option = int(input(
    f"Choose one of them to play: 1 for pokemon, 2 for outerspace, 3 for random words\n"))


def random():
    if option == 1:
        chosen_word = r.choice(pokedex)
    elif option == 3:
        chosen_word = r.choice(word_list)

    
    word_length = len(chosen_word)
    end_of_game = False
    lives = 6

    print(logo)

    # print(f'Pssst, the solution is {chosen_word}.')

    display = []
    for _ in range(word_length):
        display += "_"

    while not end_of_game:
        guess = input("Guess a letter: ").lower()
        # clear()

        if guess in display:
            print("You have already guessed the letter in word.")
    	# replace the _ with the letter in choosen word
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter

        if guess not in chosen_word:

            lives -= 1
            print(
                f"You guessed {guess}. You lost a life. {lives} lives remain.")
            if lives == 0:
                print(f"Word was {chosen_word}")
                end_of_game = True
                print("You lose.")

        print(f"{' '.join(display)}")

        if "_" not in display:
            end_of_game = True
            print("You win.")
        print(stages[lives])

random()