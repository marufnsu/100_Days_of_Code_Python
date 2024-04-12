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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    """ Returns True if there is enough resources, else returns False """
    for ingredient in order_ingredients:
        if order_ingredients[ingredient] >= resources[ingredient]:
            print(f"Sorry, you don't have enough {ingredient}")
            return False
        return True


def calculate_cost():
    """ Returns the total cost of the ingredients """
    print("Please insert coins.")
    total_cost = int(input("How many quarters?")) * 0.25
    total_cost += int(input("How many dimes?")) * 0.1
    total_cost += int(input("How many nickles?")) * 0.05
    total_cost += int(input("How many pennies?")) * 0.01
    return total_cost


def is_transaction_sufficient(money_received, drink_cost):
    """ Returns True if the payment is sufficient, else returns False """
    if drink_cost < money_received:
        change = round(money_received - drink_cost, 2)
        print(f"You have {change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, you don't have enough")
        return False


def make_coffee(drink_name, order_ingredients):
    """ Deduct the ingredients from the drink list"""
    for order_ingredient in order_ingredients:
        resources[order_ingredient] -= order_ingredients[order_ingredient]
    print(f" Here is your drink {drink_name} ☕️")


is_on = True
while is_on:
    choice = input("What would you like? (esspresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = calculate_cost()
            if is_transaction_sufficient(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])


