#Interactive Coding Exercise Leap Year
#REMEMBER!
#year / 4 is leap
#year / 400 is leap
#year / 100 is not leap

print("\nLEAP YEAR CHECKER")
year = int(input("What year do you want to check? "))

centurycheck = year % 100

if centurycheck == 0:
    if year % 400 == 0:
        print(f"\nyep, {year} is a leap year indeed.")
    else:
        print(f"\nhaiyaaaaa, although {year} is divisible by 4, Century years have different rules so it is not a leap year.")
elif centurycheck > 0:
    if year % 4 == 0:
        print(f"\nyep, {year} is a leap year indeed.")
    else:
        print(f"\nnope, tis not a leap year boiiiii.")
else:
    if year % 4 == 0:
        print(f"\nyep, {year} is a leap year indeed.")
    else:
        print(f"\nnope, tis not a leap year boiiiii.")