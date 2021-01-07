#Default Database
import random
from replit import clear
import Final_Application_Database
face = True

#Functions
#==============================================================================
#Card Reader and Randomizer
def card_shuffler(Final_Application_Database, face):
    """Shuffle Cards and Print Cards Drawn"""
    number = 0
    symbol = ""
    no = ""
    symbol = random.choice(Final_Application_Database.deck)
    number = random.choice(Final_Application_Database.numbers)
    if face != True:
        for n in range(len(Final_Application_Database.card_cover)):
            print(Final_Application_Database.card_cover[n])
    else:
        no = number
        if number == 10:
            no = 0
        elif number == 11:
            no = "J"
        elif number == 12:
            no = "Q"
        elif number == 13:
            no = "K"
        print(f" _____ \n|{no}    | \n|     | \n|  {symbol}  | \n|     | \n|____{no}|")
    return number
    
def draw_player(number, Final_Application_Database, face):
    """Draw 2 General Player Cards"""
    print("\nYour cards are:")
    x1 = card_shuffler(Final_Application_Database, face)
    x2 = card_shuffler(Final_Application_Database, face)
    return x1 + x2

def draw_computer(number, Final_Application_Database, face):
    """Draw 2 General Computer Cards"""
    print("\nComputer cards are:")
    y1 = card_shuffler(Final_Application_Database, face)
    face = False
    y2 = card_shuffler(Final_Application_Database, face)
    return y1 + y2
    
def hit(number, Final_Application_Database, face):
    """Draw Another Player Card"""
    x3 = card_shuffler(Final_Application_Database, face)
    return x3
    
#In Game
#==============================================================================
#Game Replay
trigger_replay = True

while trigger_replay != False:
    #Game Starter
    trigger_round = True
    
    #Card Draw
    trigger_draw = True
    
    #Game Again
    trigger_again = True
    
    #Reset Values
    comp = ""
    z = 0
    player = 0
    computer = 0
    number = 0
    symbol = 0
    
    #Opening Message
    clear()
    print(Final_Application_Database.splash_logo)
    print(Final_Application_Database.splash_text)

    #Round Verification
    while trigger_round != False:
        response = (input("Do you want to play the game? Y/N: ")).lower()
        if response == "y":
            clear()
            #Draw Cards
            x = draw_player(number, Final_Application_Database, face)
            y = draw_computer(number, Final_Application_Database, face)
            trigger_round = False
        elif response == "n":
            clear()
            print("\nGoodbye!")
            trigger_draw = False
            trigger_again = False
            trigger_replay = False
            trigger_round = False
        else:
            print("\nINVALID INPUT!")

        #Hit or Pass Verification
        while trigger_draw != False:
            comp = (input("Type 'Y' to get another card, 'N' to pass: ")).lower()
            if comp == "y":
                z = hit(number, Final_Application_Database, face)
                player = x + z
                computer = y
                if player <= 21 and player > computer and computer <= 21:
                    print("\nPLAYER WINS!")
                    print(f"Player = {player} : {computer} = Computer")
                elif player <= 21 and player < computer and computer <= 21:
                    print("\nCOMPUTER WINS!")
                    print(f"Player = {player} : {computer} = Computer")
                else:
                    print("\nCOMPUTER WINS!")
                    print(f"Player = {player} : {computer} = Computer")
            elif comp == "n":
                player = x
                computer = y
                if player < 21 and player > computer:
                    print("\nPLAYER WINS!")
                    print(f"Player = {player} : {computer} = Computer")
                elif player < 21 and player < computer:
                    print("\nCOMPUTER WINS!")
                    print(f"Player = {player} : {computer} = Computer")
                elif player == computer and player <= 21:
                    print("\nCOMPUTER WINS!")
                    print(f"Player = {player} : {computer} = Computer")
                else:
                    print("\nCOMPUTER WINS!")
                    print(f"Player = {player} : {computer} = Computer")
            else:
                print("\nINVALID INPUT!")
            
            trigger_draw = False

        trigger_round = False
    
    while trigger_again != False:
        trigger = (input("\nDo you want to play again? Y/N: "))
        if trigger == "y":
            trigger_again = False
        elif trigger == "n":
            trigger_again = False
            trigger_replay = False
            clear()
            print("\nGoodbye!")
        else:
            print("\nINVALID INPUT!")
        
print(Final_Application_Database.copyright)