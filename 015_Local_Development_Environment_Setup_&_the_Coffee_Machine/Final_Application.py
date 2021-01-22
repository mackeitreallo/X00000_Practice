import Final_Application_Database
from replit import clear

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

#STATUS REPORT
def status_report(profit):
    print("\nHere are the supplies level:")
    x = resources["water"]
    y = resources["milk"]
    z = resources["coffee"]
    n = profit
    print(f"        Available Water:    {x}")
    print(f"        Available Milk:     {y}")
    print(f"        Available Coffee:   {z}")
    print(f"        Total Profit:       {n}")

#TAKE ORDER
def place_order(profit):
    trigger_order = False
    while trigger_order != True:
        print("\nWhat would you like to order?")
        print("     - Latte\n     - Cappuccino\n     - Espresso")
        order = input("_____________________________\n").lower()
        if order == "cappuccino" or order == "latte" or order == "espresso":
            clear()
            trigger_order = True
        elif order == "report":
            clear()
            status_report(profit)
        else:
            clear()
            print("INVALID INPUT!")
    return order

#CHECK STOCKS
def check_stocks(n1, n2):
    for item in resources:
        if n1[item] > resources[item]:
            return False
        else:
            return True

#PAYMENT METHOD
def payment_method(n2):
    pay = float(input("\nHow much are you gonna pay?: "))
    if pay < n2:
        print("INSUFFICIENT FUNDS!")
    else:
        clear()
        print("PAYMENT RECEIVED")
        change = pay - n2
        print(f"Here's your change amounting to: Php {change}")
        return True

#ORDER INGREDIENTS
def order_entry(profit):
    trigger_place_order = False
    while trigger_place_order != True:
        x = place_order(profit)
        n = Final_Application_Database.MENU[x]
        n1 = n["ingredients"]
        n2 = n["cost"]
        if check_stocks(n1, n2) == True:
            print(f"\nThat will be {n2}.")
            if payment_method(n2) == True:
                profit += n2
                for item in resources:
                    resources[item] -= n1[item]
                trigger_place_order = True
        else:
            clear()
            print("NOT ENOUGH STOCKS AVAILABLE!")
    print(f"\nHere is your {x.title()}. Enjoy!")
    status_report(profit)
    replay = (input("\nWould you like to order again? Y/N: ")).lower()
    if replay == "y":
        clear()
        return True
    elif replay == "n":
        clear()
        return False
    else:
        clear()
        print("INVALID INPUT!")
        return True

#SYSTEM TRIGGER
def apprun():
    profit = 0
    trigger_replay = True
    while trigger_replay != False:
        trigger_replay = order_entry(profit)
    clear()
    print("\nThank you and come again!")

apprun()