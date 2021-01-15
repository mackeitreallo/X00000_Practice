import Final_Application_Database
from replit import clear

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

#STATUS REPORT
def status_report():
    print("\nHere are the supplies level:")
    x = resources["water"]
    y = resources["milk"]
    z = resources["coffee"]
    print(f"        Available Water:    {x}")
    print(f"        Available Milk:     {y}")
    print(f"        Available Coffee:   {z}")
    print(f"        Total Profit:       {profit}")

#TAKE ORDER
def place_order():
    clear()
    trigger_order = False
    while trigger_order != True:
        print("\nWhat would you like to order?")
        print("     - Latte\n     - Cappuccino\n     - Espresso")
        order = input("_____________________________\n").lower()
        if order == "cappucino" or order == "latte" or order == "espresso":
            clear()
            trigger_order = True
        elif order == "report":
            clear()
            status_report()
        else:
            clear()
            print("INVALID INPUT!")
    return order

#CHECK STOCKS
def check_stocks(n1, n2):
    for item in resources:
        if n1[item] > resources[item]:
            print("NOT ENOUGH STOCKS AVAILABLE!")
            return False
        else:
            resources[item] -= n1[item]

#ORDER INGREDIENTS
def order_entry(profit):
    x = place_order()
    n = Final_Application_Database.MENU[x]
    n1 = n["ingredients"]
    n2 = n["cost"]
    check_stocks(n1, n2)
    profit += n2
    status_report()

    

order_entry(profit)