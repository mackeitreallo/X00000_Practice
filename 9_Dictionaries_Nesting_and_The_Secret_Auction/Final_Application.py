#Default Database
import Final_Application_Database
from replit import clear
replay = True
replay_name = True
replay_amount = True
replay_bid = True
bids = {}
bidder_name = ""
bidder_value = 0

#Variables Deposits
def bidder_register(name = bidder_name, amount = bidder_value):
    bids[name] = amount

def bidder_reader(bids):
    bidder_winner = 0
    winner = ""
    for bidders in bids:
        bidder_amount = bids[bidders]
        if bidder_amount > bidder_winner:
            bidder_winner = bidder_amount
            winner = bidders
    clear()
    print(Final_Application_Database.splash_logo)
    print(f"\nThe winner to the secret auction is: {winner} with the amount of: ${bidder_winner}")

#Data Gathering
while replay != False:
    #Introduction and Cleared Inputs
    clear()
    replay_bid = True
    print(Final_Application_Database.splash_logo)
    
    #Name Input Verification
    while replay_name != False:
        bidder_name = input("\nWhat is your name?: ")
        trigger_name = (input(f"{bidder_name} is it? Y/N: ")).lower()
        if trigger_name == "n":
            replay_name = True
            clear()
        elif trigger_name == "y":
            replay_name = False
        else:
            replay_name = True
            clear()
            print("\nINVALID INPUT!\n")
    
    #Amount Input Verification
    while replay_amount != False:
        bidder_value = float(input("How much is your bid?: $"))
        trigger_amount = (input("Is the amount ok? Y/N: ")).lower()
        if trigger_amount == "n":
            replay_amount = True
            clear()
        elif trigger_amount == "y":
            replay_amount = False
        else:
            replay_amount = True
            clear()
            print("\nINVALID INPUT!\n")
    
    #Add to Dictionary
    bidder_register(name = bidder_name, amount = bidder_value)
    
    #Replay Bid Trigger
    while replay_bid != False:
        trigger = (input("\nAre there any more bidders? Y/N: ")).lower()
        if trigger == "n":
            replay = False
            replay_bid = False
        elif trigger == "y":
            replay_name = True
            replay_amount = True
            replay_bid = False
        else:
            clear()
            print("\nINVALID INPUT!\n")

#Bidding Evaluation
bidder_reader(bids)

#Copyright
print("\ncoded by: Mark Renz L. Carillo (c) 2021")