#Hangman

#Plugins
import random
import Final_Application_Database

#Health Bar
Health = 7

#Word chooser and breaker
n = random.randint(0, len(Final_Application_Database.Dictionary) - 1)
word = Final_Application_Database.Dictionary[n]
nword = len(word)
complete = []
finish = ""
verify = []

#Checker
blank = ""
guess = ""
for characters in range (0, nword):
    character = word[characters]
    complete += "_"
    blank += "_"
    guess += character
print(guess)
print(blank)

#Evaluation
choice = ""
letter = input("\nGuess a letter: ")
for check in range (0, nword):
    if letter == word[check]:
        choice = letter
        complete[check] = choice
        finish += complete[check]
        print("correct")
    else:
        choice = "_"
        print("incorrect")

Health -= 1
print(complete)
print(finish)
print(guess)
print(Health)
    
print("\nGame Over!")