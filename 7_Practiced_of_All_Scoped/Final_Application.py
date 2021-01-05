#Hangman v2.0

#Database
import random
import Final_Application_Database
from replit import clear

#Health Bar
Health = 8
def HP():
    if Health == 8:
        print(Final_Application_Database.hp8)
    elif Health == 7:
        print(Final_Application_Database.hp7)
    elif Health == 6:
        print(Final_Application_Database.hp6)
    elif Health == 5:
        print(Final_Application_Database.hp5)
    elif Health == 4:
        print(Final_Application_Database.hp4)
    elif Health == 3:
        print(Final_Application_Database.hp3)
    elif Health == 2:
        print(Final_Application_Database.hp2)
    elif Health == 1:
        print(Final_Application_Database.hp1)

#Word Picker
word = random.choice(Final_Application_Database.Dictionary)
nword = len(word)
display = []
guess = []
used = []
gui = ""

#Word Expand
for n in range(nword):
    display += ("_")
    guess += (word[n])
    gui += (display[n] + " ")
    
def update():
    gui = ""
    for n in range(nword):
        gui += display[n]
    
#Scoreboard
Score = True

#Game Intro
print("\nHangman v2.0\n")
print(display)
#print(guess)

#Word Evaluator
while Score == True:
    letter = input("\nGuess a letter: ")
    for n in range(nword):
        if letter == guess[n]:
            display[n] = letter
            update()
            
    clear()
    
#Health Deductor
    if letter not in word:
        Health -= 1
        print("\nYou lose a life, letter not in the word.")
    elif letter in used:
        Health -= 1
        print("\nYou lose a life, you've already used that letter.")

#Used Letter Registry
    used.append(letter)
        
#Health Status
    print("\n")
    HP()
    
#Current Game Status
    print(f"\n{display}")

#Game Deciding Factor
    if Health == 0:
        Score = False
    elif guess == display:
        Score = False

#Finished Game
if display == guess:
    print("\nYOU WIN!")
else:
    print(Final_Application_Database.hp0)
    print("\nGAME OVER!")