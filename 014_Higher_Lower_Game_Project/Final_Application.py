#sample link: https://repl.it/@appbrewery/higher-lower-final

import random
from replit import clear
import Final_Application_Database

def randomizer():
    n = len(Final_Application_Database.data)
    counts = []
    for n in range(n):
        counts.append(n)
    x = random.choice(counts)
    return x

def random_chooser():
    choice = int(randomizer())
    choice_select = Final_Application_Database.data[choice]
    choice_name = choice_select["name"]
    choice_description = choice_select["description"]
    choice_country = choice_select["country"]
    choice_count = choice_select["follower_count"]
    print(f"     {choice_name}\n     a {choice_description}\n     from {choice_country}")
    return choice_count

score = 0
trigger_replay = True
while trigger_replay != False:
    clear()
    print(Final_Application_Database.splash_logo)
    print(f"\nScore = {score}")
    print("\nCompare A:")
    choice_x = random_chooser()
    print(Final_Application_Database.indicator)
    print("\nAgainst B:")
    choice_y = random_chooser()
    trigger_answer = False
    while trigger_answer != True:
        answer = (input("\nWhich has more followers? A/B: ")).lower()
        if answer == "a":
            if choice_x > choice_y:
                score += 1
                trigger_answer = True
            else:
                trigger_answer = True
                trigger_replay = False
        elif answer == "b":
            if choice_x < choice_y:
                score += 1
                trigger_answer = True
            else:
                trigger_answer = True
                trigger_replay = False
        else:
            print("\nINVALID INPUT")
clear()
print(f"\nScore = {score}")
print("\nGAME OVER!")