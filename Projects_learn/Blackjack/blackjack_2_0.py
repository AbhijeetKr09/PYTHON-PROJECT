from art import logo
import random



def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate(card):
    total = sum(card)
    if total == 21 and len(card) == 2:
        return 0
    elif 11 in card and total > 21:
        card.remove(11)
        card.append(1)
    return total


def compare(user_total, computer_total, computer_cards):
    if user_total == computer_total:
        return f"""
            computer cards: {computer_cards}
            Your total: {user_total}
            Computer total: {computer_total}
            It's a Draw."""
    elif user_total == 0:
        return f"""
            computer cards: {computer_cards}
            Your total: {user_total}
            Computer total: {computer_total}
            You got blackjack, you won."""
    elif computer_total == 0:
        return f"""
            computer cards: {computer_cards}
            Your total: {user_total}
            Computer total: {computer_total}
            computer got blackjack, you won."""
    elif user_total > 21:
        return f"""
            computer cards: {computer_cards}
            Your total: {user_total}
            Computer total: {computer_total}
            You lost, Computer won."""
    elif computer_total > 21:
        return f"""
            computer cards: {computer_cards}
            Your total: {user_total}
            Computer total: {computer_total}
            You won, Computer lost."""
    elif user_total > 21 and computer_total > 21:
        if user_total < computer_total:
            return f"""
                computer cards: {computer_cards}
                Your total: {user_total}
                Computer total: {computer_total}
                You won, Computer lost."""
        else:
            return f"""
                computer cards: {computer_cards}
                Your total: {user_total}
                Computer total: {computer_total}
                You lost, Computer won."""
    elif user_total > computer_total:
        return f"""
            computer cards: {computer_cards}
            Your total: {user_total}
            Computer total: {computer_total}
            You won, Computer lost."""
    else:
        return f"""
            computer cards: {computer_cards}
            Your total: {user_total}
            Computer total: {computer_total}
            You lost, Computer won."""
def play():
    print(logo)

    computer_cards = []
    user_cards = []
    game_end = False
    for _ in range(2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())

    while not game_end:
        user_total = calculate(user_cards)
        computer_total = calculate(computer_cards)
        print(f"""
        Your cards: {user_cards}, current total: {user_total}
        computer first card: {computer_cards[0]}
        """)
        if user_total == 0 or computer_total == 0 or user_total > 21:
            game_end = True
        else:
            deal = input("Do you want to deal or exit? y to deal, n to exit: ").lower()
            if deal == "y":
                user_cards.append(deal_cards())
            else:
                game_end = True
    while computer_total != 0 and computer_total < 17:
        computer_cards.append(deal_cards())
        computer_total = calculate(computer_cards)
    result = compare(user_total, computer_total, computer_cards)
    print(result)
while input("Do you want to play blackjack? y for yes and n for no: ").lower() == "y":
    play()

