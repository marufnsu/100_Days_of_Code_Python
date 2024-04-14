from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


money_machine = MoneyMachine()
menu = Menu()
coffee = CoffeeMaker()

is_on = True
while is_on:
    options = menu.get_items()
    choice = input(f"What do you like? {options}: ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(coffee.report())
        print(money_machine.report())
    else:
        drink = menu.find_drink(choice)
        if coffee.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee.make_coffee(drink)
