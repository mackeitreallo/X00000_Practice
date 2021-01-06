#Nested if statements and elif statements
print("\nBody Mass Index Calculator Ver.X")
wt = float(input("\nWhat is your weight in kg? "))
ht = float(input("What is your height in m? "))
bmi = round(wt / (ht ** 2), 2)
if bmi >= 18.5:
    if bmi >= 25:
        if bmi >= 30:
            if bmi >= 35:
                print(f"Your BMI is {bmi}, you should go and see a doctor.")
            else:
                print(f"Your BMI is {bmi}, you are obese.")
        else:
            print(f"Your BMI is {bmi}, you are slightly overweight.")
    else:
        print(f"Your BMI is {bmi}, you are perfectly normal!")
else:
    print(f"Your BMI is {bmi}, you need nutrients!")
