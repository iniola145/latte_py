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


# For inputting the currency


def first():
    print("Please insert coins")
    qua = int(input("How many quarters: "))
    dim = int(input("How many dimes: "))
    nick = int(input("How many nickels: "))
    penny = int(input("How many pennies: "))
    return qua, dim, nick, penny


# For converting the currencies to dollar
def conversion(quater, dime, nickel, penny):
    cur = [quater, dime, nickel, penny]
    cur2 = []
    for i in cur:
        div = i / 100
        cur2.append(div)
        sum_currency = sum(cur2)
    rounded_currency = round(sum_currency, 2)
    return rounded_currency


# To find the change left after paying


def change(dollar2, amount_2):
    amt_left = dollar2 - amount_2
    return amt_left


# To get the refund after paying


def money_refund(price):
    quarters, dimes, nickels, pennies = first()
    dollar = conversion(quarters, dimes, nickels, pennies)
    print(f"${dollar}")
    if price > dollar:
        print("Sorry that is not enough money. Money refunded")
        return resources["money"], True
    else:
        amount_remaining = change(dollar, price)
        amount_remained = round(amount_remaining, 2)
        print(f"Here is ${amount_remained} in change")
        print("Here is your espresso ☕. Enjoy!")
        # To return the amount paid into the machine
        return resources["money"] + price, False


def resorces_remaining(x, y, z):
    return resources["water"] - x, resources["milk"] - y, resources["coffee"] - z


# It is conditional statement that checks if the resorces are available to make any coffee


def coffe_maker(w, m, c):
    if resources["water"] < w:
        return True
    elif resources["milk"] < m:
        return True
    elif resources["coffee"] < c:
        return True


# To start the code


resources["money"] = 0
while True:
    ask = input("What would you like? (espresso/latte/cappuccino): ")
    # To print the current report of materials
    if ask == "report":
        print(f"Water: {resources["water"]}ml")
        print(f"Milk: {resources["milk"]}ml")
        print(f"Coffee: {resources["coffee"]}g")
        print(f"Money: ${resources["money"]}")
    elif ask == "espresso":
        check = coffe_maker(50, 0, 18)
        if check:
            print(f"Sorry there is not enough water")
            continue
        price_e = 1.50
        # To update the money part of the resources' dictionary.
        resources["money"], no_money = money_refund(price_e)
        # To update the resources in the machine for espresso
        if no_money:
            continue
        resources["water"], resources["milk"], resources["coffee"] = resorces_remaining(50, 0, 18)
    elif ask == "latte":
        check = coffe_maker(200, 150, 24)
        if check:
            print(f"Sorry there is not enough water")
            continue
        price_l = 2.50
        # To update the money part of the resources' dictionary.
        resources["money"], no_money = money_refund(price_l)
        # To update the resources in the machine for latte
        if no_money:
            continue
        resources["water"], resources["milk"], resources["coffee"] = resorces_remaining(200, 150, 24)
    elif ask == "cappuccino":
        check = coffe_maker(250, 100, 24)
        if check:
            print(f"Sorry there is not enough coffee")
            continue
        price_c = 3.00
        # To update the money part of the resources' dictionary.
        resources["money"], no_money = money_refund(price_c)
        if no_money:
            continue
        # To update the resources in the machine for latte
        resources["water"], resources["milk"], resources["coffee"] = resorces_remaining(250, 100, 24)
    elif ask == "off":
        break
