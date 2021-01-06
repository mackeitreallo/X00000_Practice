#Import Database
import random
import Final_Application_Database

characters = []

#Alphabet Chooser
letter = Final_Application_Database.letters
nletter = int(len(Final_Application_Database.letters)) - 1

#Number Chooser
number = Final_Application_Database.numbers
nnumber = int(len(Final_Application_Database.numbers)) - 1

#Symbol Chooser
symbol = Final_Application_Database.symbols
nsymbol = int(len(Final_Application_Database.symbols)) - 1

#Front Message
print("\nWelcome to Random Password Generator!")
qletter = int(input("\nHow many letters would you like to be added in your password?\n"))
qnumber = int(input("\nHow many numbers would you like to be added in your password?\n"))
qsymbol = int(input("\nHow many symbols would you like to be added in your password?\n"))

#Password Conditions
for charletter in range(1, (qletter + 1)):
    pletter = random.randint(0, nletter)
    characters.append(str((letter[pletter])))
for charnumber in range(1, (qnumber + 1)):
    pnumber = random.randint(0, nnumber)
    characters.append(str((number[pnumber])))
for charsymbol in range(1, (qsymbol + 1)):
    psymbol = random.randint(0, nsymbol)
    characters.append(str((symbol[psymbol])))
        
#Password Easy Level
Passphrase_1 = ""
for char1 in characters:
    Passphrase_1 += char1
print(f"\nFor easy level, your password is: {Passphrase_1}")

#Password Hard Level
Passphrase_2 = ""
random.shuffle(characters)
for char2 in characters:
    Passphrase_2 += char2
print(f"\nFor hard level, your password is: {Passphrase_2}")