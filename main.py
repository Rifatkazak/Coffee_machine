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
resources_water = resources['water']
resources_milk = resources['milk']
resources_coffee = resources['coffee']
is_on = True

#Check sufficient

def check_sufficient():
    if chose=="espresso":
        water = MENU["espresso"]["ingredients"]["water"]
        coffee = MENU["espresso"]["ingredients"]["coffee"]
        milk = 0
        cost = 1.5
    elif chose=="latte":
        water = MENU["latte"]["ingredients"]["water"]
        milk= MENU["latte"]["ingredients"]["milk"]
        coffee = MENU["latte"]["ingredients"]["coffee"]
        cost = 2.5
    elif chose == "cappuccino":
        water = MENU["cappuccino"]["ingredients"]["water"]
        milk = MENU["cappuccino"]["ingredients"]["milk"]
        coffee = MENU["cappuccino"]["ingredients"]["coffee"]
        cost = 3.0
    else:
        print("Please enter valid value :")
    if water < resources_water  and milk < resources_milk and coffee < resources_coffee :

        coin_quarters = float(input("How many quarters (0,25$) ? "))
        coin_dimes = float(input("How many dimes (0,10$) ? "))
        coin_nickles = float(input("How many nickles (0,05$) ? "))
        coin_pennies = float(input("How many pennies (0,01$) ? "))
        total = (coin_quarters*0.25)+(coin_nickles*0.1)+(coin_dimes*0.05)+(coin_pennies*0.01)
        profit = total
        if profit < cost :
            print("Sorry that'/s not enough money. Money refunded.")
        else :
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}")
            print(f"Money: ${round(profit,2)}")
        print(f"Here is your {chose}. Enjoy!")
    else:
        print("Sorry there is not enough water")


# Print input "What would you like"(espresso/latte/cappuccino)
while is_on:
    chose = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if chose == "off":
        is_on = False
    elif chose == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}")
        print(f"Money: ${profit}")
    else:
        check_sufficient()