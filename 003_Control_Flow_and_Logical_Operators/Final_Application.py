#Minimalist Treasure Island!
print("\nWelcome to the Treasure Island Budget Friendly Version!")

choice1 = input("\nDo you want to go to the left or right? Type 'Left' or 'Right': ").lower()
if choice1 == "left":
    print("\nAwesome mate!")
    choice2 = input("The coast is near and there are 3 suspicious doors, swim or wait? Type 'Swim' or 'Wait': ").lower()
    if choice2 == "wait":
        print("\nNot bad boiiiiii!")
        choice3 = input("\nWe're at the end game now, choose 1 door amongst the 3. Blue, Red or White?: ").lower()
        if choice3 == "blue" or choice3 == "red":
            print("\nGame Over!")
        else:
            print("\nYou Win!")
    else:
        print("\nGame Over!")
else:
    print("\nGame Over!")