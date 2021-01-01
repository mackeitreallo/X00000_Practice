import random
import Final_Application_Database

#Rock, Paper, Scissors Database
choice0 = Final_Application_Database.rock
choice1 = Final_Application_Database.paper
choice2 = Final_Application_Database.scissor

#Intro Message
print(f"\nWelcome to {choice0}, {choice1}, {choice2} game!")

#Rock, Paper, Scissors List
weapon = [choice0, choice1, choice2]

#Player Weapon Choosing
player_weapon = int(input("\nEnter 0 for Rock, 1 for paper and 2 for scissors!: "))
player = weapon[player_weapon]

#Machine Weapon Choosing
machine_weapon = [choice0, choice1, choice2]
machine = random.choice(machine_weapon)

#Battle Bets
output = player + " vs " + machine

#Conditions
result1 = f"{choice0} vs {choice2}"
result2 = f"{choice1} vs {choice0}"
result3 = f"{choice2} vs {choice1}"
result4 = f"{choice2} vs {choice0}"
result5 = f"{choice0} vs {choice1}"
result6 = f"{choice1} vs {choice2}"

#Result Message
print(f"\nPlayer = {output} = Machine")

#Battle Results
if output == result1 or output == result2 or output == result3:
    print("\nPlayer Wins!")
elif output == result4 or output == result5 or output == result6:
    print("\nMachine Wins!")
else:
    print("\nGame is a Draw!")
    
    