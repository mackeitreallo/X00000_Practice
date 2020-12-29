#Multiple If Statements in Succession
#Small Pizza 15
#Medium Pizza 20
#Large Pizza 25
#addon pepperoni small +2
#addon pepperoni m/l +3
#addon cheese +1

print("\nJollibee Pizza Branch Delivery, May I take your order?")
bill = 0
order = input("\nWould you like to place your order? Y/N: ")
if order == "Y":
    size = input("\nWhat is the size of the pizza you want to order? S, M or L? ")
    if size == "S":
        bill = 15
        print("\nThat will be $15.")
    elif size == "M":
        bill = 20
        print("\nThat will be $20.")
    else:
        bill = 25
        print("\nThat will be $25.")
    
    addon1 = input("\nWould you like to add extra pepperoni? Y/N: ")
    addon2 = input("\nWould you like to add more cheese? Y/N: ")
    
    if addon1 == "Y":
        if size == "S":
            bill += 2
        elif size == "M":
            bill += 3
        else:
            bill += 3
    
    if addon2 == "Y":
        bill += 1
    
    print(f"\nYour total order would be ${bill}.")
    checkout = print(input("Proceed to checkout? Y/N: "))
    print("\nThank you for the purchase!")
else:
    print("\nAlright then! Have great day!")