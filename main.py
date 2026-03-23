from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

on = True
menu = Menu()
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()

while on:
    user_choice = input(f"What would you like? ({menu.get_items()}): ").lower()
    if user_choice == "off":
        on = False
    elif user_choice == "report":
        coffee_machine.report()
        money_machine.report()
    else:
        drink = menu.find_drink(user_choice)
        if drink:
            if coffee_machine.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_machine.make_coffee(drink)
