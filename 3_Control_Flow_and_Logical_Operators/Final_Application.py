#Minimalist Treasure Island!
print("\nWelcome to the Treasure Island Budget Friendly Version!")

choice1 = input("\nDo you want to go to the left or right? Type 'Left' or 'Right': ")
if choice1 == "Left":
    print("\nAwesome mate!")
    choice2 = input("The coast is near and there are 3 suspicious doors, swim or wait? Type 'Swim' or 'Wait': ")
    if choice2 == "Wait":
        print("\nNot bad boiiiiii!")
        choice3 = input("\nWe're at the end game now, choose 1 door amongst the 3. Blue, Red or White?: ")
        if choice3 == "Blue" or choice3 == "Red":
            print("\nGame Over!")
        else:
            print("\nYou Win!")
    else:
        print("\nGame Over!")
else:
    print("\nGame Over!")