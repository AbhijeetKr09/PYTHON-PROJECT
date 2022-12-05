from art import logo

print(logo)

def auction(data):
    highest_bidder = 0
    winner = ""
    for name in data:
        bidder = int(data[name])
        if bidder > highest_bidder:
            highest_bidder = bidder
            winner = name
    print(f"{winner} did the highest bid of {highest_bidder} and won.")
data = {}
    
players = True
close = False
while not close:

    while players:
        name = input("What is your name? \n")
        bid = input("What is your bid price? $")
        player = input("Are there another players who can bid? yes or no? \n").lower()
        data[name] = bid

        if player == "no":
            players = False
            auction(data=data)
    turnoff = input("Do you want to close the program: y or n").lower()
    if turnoff == "y":
        close = True
    elif turnoff == "n":
        players = True          
        





