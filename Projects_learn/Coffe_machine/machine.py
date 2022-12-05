MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit = 0


def check_ingredients(required_item):
    for ingredient in required_item:
        if resources[ingredient] < required_item[ingredient]:
            # resources[ingredient] -= required_item[ingredient]
            print(f"Sorry we have sortage of {ingredient}.\nplease try another coffee.")
            return False
    return True
    

def money_counter():
    '''quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01'''
    total = int(input("quarters: ")) * 0.25
    total += int(input("dimes: ")) * 0.10
    total += int(input("nickles: ")) * 0.05
    total += int(input("pennies: ")) * 0.01
    return total


def enough_money(money, required_money):
    global profit
    if required_money <= money:
        change = round(money - required_money, 2)
        if change != 0:
            print(f"Here is ${change} in change.")
        profit += required_money
        return True
    else:
        print("Sorry not enough money. Money refunded.")
        return False


def make_drink(ingredients, user_input):
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {user_input}. Enjoy!")


turn_off = False
while not turn_off:
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
    
    if user_input == "report":
        print(f'water: {resources["water"]} ml\nmilk: {resources["milk"]} ml\ncoffee: {resources["coffee"]} g')
        print(f'Money: ${profit}')
    elif user_input == "off":
        turn_off = True
    else:
        cafe = MENU[user_input]
        if check_ingredients(cafe["ingredients"]):
            money = money_counter()
            if enough_money(money, cafe["cost"]):
                make_drink(cafe["ingredients"], user_input)