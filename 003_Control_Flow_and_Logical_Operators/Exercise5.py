#Logical Operators
print("\nWelcome to the Love Calculator!")
name1 = input("What is your full name? \n")
name2 = input("What is their full name? \n")
#Begin code below
print("\n ")
name = name1 + name2
translated = name.lower()
#counttest = int(translated.count("a"))

T = translated.count("t")
R = translated.count("r")
U = translated.count("u")
E = translated.count("e")
L = translated.count("l")
O = translated.count("o")
V = translated.count("v")
E = translated.count("e")

nn = T + R + U + E
n = L + O + V + E

score = (nn * 10) + n

if score < 10 or score > 90:
    print(f"\nYour score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"\nYour score is {score}, you are alright together.")
else:
    print(f"\nYour score is {score}.")