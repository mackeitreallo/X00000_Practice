#Understanding the Offset and Appending Items to Lists
import random

print("\nThis is not KKB, who will be the next payer for the bill game!")

#Results Override
RNGGOD = int(input("\nEnter the number you want to control the results: "))
random.seed(RNGGOD)

#Bill Roullete
candidates = input("\nWho are the peasants that shall be the candidates to pay the bill?: ")
name = candidates.split(", ")

range = len(name)

choice = random.randint(0, range -1)
print(f"\n{name[choice]} will pay the bill. No more questions!")