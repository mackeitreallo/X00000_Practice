#Default Database
import random
from replit import clear
import Final_Application_Database

#Random Number Chooser
def draw():
    number = []
    for n in range(1, 101):
        number.append(n)
    return random.choice(number)

#Game Difficulty
def gameplay():
    trigger_gameplay = False
    while trigger_gameplay != True:
        difficulty = input("\nChoose a difficulty: 'Easy' or 'Hard'? ").lower()
        if difficulty == "hard":
            trigger_gameplay = True
            return difficulty
        elif difficulty == "easy":
            trigger_gameplay = True
            return difficulty
        else:
            clear()
            print("\nINVALID INPUT!\n")
        
#Game A.I
def start():
    x = draw()
    if gameplay() == "hard":
        health = 5
    else:
        health = 10
    trigger_clear = False
    print(f"\nYou have {health} attempts remaining to guess the number.")
    while trigger_clear != True:
        y = int(input("\nMake a guess: "))
        if health > 0:
            if x == y:
                print("\nYOU WIN!")
                trigger_clear = True
            elif y > x:
                print(f"\nToo high,\nGuess again.\nYou have {health} attempts to guess the numnber.")
                health -= 1
            elif y < x:   
                print(f"\nToo low,\nGuess again.\nYou have {health} attempts to guess the numnber.")
                health -= 1
        elif health == 0:
            print("\nGAME OVER!")
            trigger_clear = True
            
#InGame
trigger_replay = True
while trigger_replay != False:
    clear()
    print(Final_Application_Database.splash_text)
    start()
    replay = (input("\nDo you want to play again? Y/N: ")).lower()
    if replay == "n":
        trigger_replay = False
    elif replay == "y":
        trigger_replay = True
    else:
        print("\nINVALID INPUT!")
        trigger_replay = False
        
print(Final_Application_Database.copyright)