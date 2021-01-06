#Default Database
import Final_Application_Database
from replit import clear
replay1 = True

while replay1 != False:
#Into Message
    clear()
    print(Final_Application_Database.splash_logo)
    print(Final_Application_Database.splash_text)
    replay2 = True

#Data Inputs
    x1 = float(input("\nWhat is the first number?: "))

    while replay2 != False:
        for n in range(len(Final_Application_Database.mdas)):
            print(Final_Application_Database.mdas[n])
        rule = input("\nWhat operation you want to do?: ")
        
        x2 = float(input("\nWhat is the next number?: "))
    
#Function Operators
        def addition(x1, x2):
            """Triggers Addition"""
            return x1 + x2

        def subtraction(x1, x2):
            """Triggers Subtraction"""
            return x1 - x2
    
        def multiplication(x1, x2):
            """Triggers Multiplication"""
            return x1 * x2

        def division(x1, x2):
            """Triggers Division"""
            return x1 / x2

#Operation Conditions        
        if rule == "+":
            x = addition(x1, x2)
        elif rule == "-":
            x = subtraction(x1, x2)
        elif rule == "*":
            x = multiplication(x1, x2)
        else:
            x = division(x1, x2)

#Results
        print(f"\n{x1} {rule} {x2} = {x}")

#Loop Trigger
        trigger = (input(f"Type 'Y' you want to continue calculating with {x}, or 'N' to start a new calculation: ")).lower()
        if trigger == 'y':
            x1 = x
            x2 = float(0)
            rule = ""
        else:
            x1 = float(0)
            x2 = float(0)
            rule = ""
            replay2 = False

#Copyright            
    print(Final_Application_Database.copyright)
