import os
logo='''
     ____    _   _               _                               _     _                   
    |  _ \  | | (_)             | |       /\                    | |   (_)                  
    | |_) | | |  _   _ __     __| |      /  \     _   _    ___  | |_   _    ___    _ __    
    |  _ <  | | | | | '_ \   / _` |     / /\ \   | | | |  / __| | __| | |  / _ \  | '_ \   
    | |_) | | | | | | | | | | (_| |    / ____ \  | |_| | | (__  | |_  | | | (_) | | | | |  
    |____/  |_| |_| |_| |_|  \__,_|   /_/    \_\  \__,_|  \___|  \__| |_|  \___/  |_| |_|
'''
bidding_people={}
wannabid=True
while wannabid:
    print(logo)
    name=input("\nEnter the Name of Bidder : ")
    price=int(input("Enter the Price to bid? Rs. : "))
    bidding_people[name]=price
    decision=input("Is there another pearson wanna bid? Y or N : ")
    
    if decision=="N":
        print("Game Result")
        wannabid=False
        highest_bid=0
        winner=""
        for bidder in bidding_people:
            if bidding_people[bidder]>highest_bid:
                highest_bid=bidding_people[bidder]
                winner=bidder
        os.system('cls')
        print("\nList of Bidders:")
        for bidder in bidding_people:
            print("f {bidder} : {bidding_people[bidder]}")
        print(f"The Winner of the Game is {winner} with the highest bid of Rs.{highest_bid} ")
    
    elif decision=="Y":
        os.system('cls')


