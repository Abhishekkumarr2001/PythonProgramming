### IMPORTS ###
import random
from art import logo, vs
from game_data import data

def pick_celebrity():
    """Function that picks a random celebrity from out list of data from game_data.py"""
    return random.choice(data)

def return_celebrity_info(celebrity_dict):
    """ Function to print the celebrity information, such as name, descriptionn and country """
    return f"{celebrity_dict['name']}, a {celebrity_dict['description']} from {celebrity_dict['country']}"

def decide_winner(celebrity_A, celebrity_B):
    # print(celebrity_A['follower_count'])
    # print(celebrity_B['follower_count'])
    """ Function that returns the whether choice A or B have higher follower count """
    if celebrity_A['follower_count'] > celebrity_B['follower_count']:
        return 'a'
    return 'b'

def print_battle(celebrity_A, celebrity_B):
    print('Compare A: ' + return_celebrity_info(celebrity_A))

    print(vs)

    print('Against B: ' + return_celebrity_info(celebrity_B))

# initialize the variable to keep track of game and the game_score
isGameOver = False
game_score = 0

# pick our 2 initial celebrities
choiceA = pick_celebrity()
choiceB = pick_celebrity()

# in case we picked the same ones, repick again.
if choiceA == choiceB:
    choiceB = pick_celebrity()

# print the game's logo
print(logo)

# run the loop until the user guesses incorrectly and the game is over.
while not isGameOver:
    # print out the selections
    print_battle(choiceA, choiceB)

    # get the user guess
    user_pick = input("Who has more followers? Type 'A' or 'B' ").lower()

    # if user made the correct guess we clear the console, increase the score and reselect
    if user_pick == decide_winner(choiceA, choiceB):
        print(logo)
        game_score += 1
        print(f'You are right! The current score is {game_score}')
        choiceA = choiceB
        choiceB = pick_celebrity()
    # in case of the loss we print the final score and we are done
    else:
        print(f'Sorry! That\'s wrong :( \n\nFinal Score: {game_score}')
        isGameOver = True
