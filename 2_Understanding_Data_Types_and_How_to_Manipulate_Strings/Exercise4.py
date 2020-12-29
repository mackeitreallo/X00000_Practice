#Number Manipulation and F Strings in Python
#commands used: round
age = input("What is your current age? ")
x = 365 #Days
y = 52 #Weeks
z = 12 #Months
remaining = 90 - int(age)
day = (remaining * x)
week = (remaining * y)
month = (remaining *z)
print(f"\nYou have {day} Days left or {week} Weeks left or {month} Months left before you turn 90")