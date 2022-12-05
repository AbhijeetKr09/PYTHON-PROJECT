from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
money = MoneyMachine()

turn_off = False
while not turn_off:
    user_input = input(f"What would you like? ({menu.get_items()}): ").lower()
    if user_input == "report":
        coffee_maker.report()
        money.report()
    elif user_input == "off":
        turn_off = True
    else:
        drink_name = menu.find_drink(user_input)
        if coffee_maker.is_resource_sufficient(drink_name) and money.make_payment(drink_name.cost):
            coffee_maker.make_coffee(drink_name)
