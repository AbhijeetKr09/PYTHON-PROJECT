from art import logo, vs
from random import choice
from game_data import data
print(logo)

# Random personality from the game_data.py file


def personality():
    '''will assign a random personality from game data file'''
    person = choice(data)
    return person


def check(compare, against, user_choice):
    '''will compare the follower count of both personality'''
    compare_follower_count = compare['follower_count']
    against_follower_count = against['follower_count']
    if compare_follower_count > against_follower_count:
        return user_choice == "a"
    else:
        return user_choice == 'b'


# compare need to save against data on every correct guess since game() have to run again compare will change on every call. That's why it have to access globally
compare = personality()


def game():
    score = 0
    play = True
    while play:
        global compare
        against = personality()
        while against == compare:
            against = personality()
        print(f"Your Current score: {score}.")
        print(f"Compare A: {compare['name']}, a {compare['description']}, from {compare['country']}")
        print(vs)
        print(f"Against B: {against['name']}, a {against['description']}, from {against['country']}")
        user_choice = input(
            "Who has more followers? Type 'A' or 'B': ").lower()
        result = check(compare, against, user_choice)

        if result == True:
            score += 1
            compare = against
        elif result == False:
            play = False
            print(f"Sorry, that's wrong. Final score: {score}")


game()
