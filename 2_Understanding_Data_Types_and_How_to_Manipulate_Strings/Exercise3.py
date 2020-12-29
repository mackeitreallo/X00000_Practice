#Mathematical Operations in Python
print("Body Mass Index Calculator")
bmiw = float(input("\nWhat is your weight in kilograms?\n"))
bmih = float(input("\nHow about your height in meters?\n"))
bmi = int(bmiw / (bmih **2))
print("\nYour Body Mass Index is: " + str(bmi))