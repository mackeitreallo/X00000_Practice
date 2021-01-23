import menu
import money_machine
import coffee_maker

x = money_machine.MoneyMachine()
y = coffee_maker.CoffeeMaker()
z = menu.Menu()
is_on = True

while is_on:
    options = z.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        y.report()
        x.report()
    else:
        drink = z.find_drink(choice)
        if y.is_resource_sufficient(drink):
            if x.make_payment(drink.cost):
                y.make_coffee(drink)