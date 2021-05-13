# A Python interpretation of Steve Jackson's Zombie Dice
# Rules for the game can be found at http://www.sjgames.com/dice/zombiedice/img/ZDRules_English.pdf
# This script has been written such that the entire game is completely customisable.

import random

# Number of players
num_players=2

# The total number of turns in a game
max_turns=num_players * 500

# The score required to win
winning_score=13

# The total number of dice
max_dice=13

# The maximum number of sides a die has
max_sides=6

# Initialise the scores (assuming a two player game)
scores = [0] * num_players

# The number of dice selected each turn
dice_per_turn = 3

# Define the different basic dice types
# The final element in the array is the die colour
master_green_die = ["brain", "runner", "shotgun", "brain", "brain", "runner", "green"]
master_yellow_die = ["runner", "brain", "shotgun", "runner", "shotgun", "brain", "yellow"]
master_red_die = ["shotgun", "runner", "brain", "shotgun", "shotgun", "runner", "red"]

# Define the dice that the game will use based on the maximum number of die sides
green_die = []
yellow_die = []
red_die = []
for i in range(0, max_sides):
    green_die.append(master_green_die[i % (len(master_green_die) - 1)])
    yellow_die.append(master_yellow_die[i % (len(master_yellow_die) - 1)])
    red_die.append(master_red_die[i % (len(master_red_die) - 1)])
green_die.append("green")
yellow_die.append("yellow")
red_die.append("red")

# Define the available dice in the game
# Typically, six green dice, four yellow dice and three red dice
dice=[green_die, green_die, green_die, green_die, green_die, green_die, yellow_die, yellow_die, yellow_die, yellow_die, red_die, red_die, red_die]

# Ensure that the values selected for the game variables won't seriously break anything
if dice_per_turn > max_dice:
    print ("The number of dice selected per turn exceeds the total number of dice in the game (", dice_per_turn, ">", max_dice, ")")
    raise SystemExit

for j in range(0, max_turns):
    print ("SCORES")
    for i in range(0, num_players):
        print ("Player", i+1, ":", scores[i])
    print ("Player ",(j%num_players)+1,"'s turn...")
    input ("Press Enter to continue...")
    
    brains = 0
    shotguns = 0

    # Dice selections are predetermined, but the players are unaware of this
    dice_selections = random.sample(range(0, max_dice), max_dice)

    # Select the dice to roll
    # The first time the dice being rolled are simply the first three selected
    dice_to_roll = []
    for dice_pulled in range(0, dice_per_turn):
        dice_to_roll.append(dice_selections[dice_pulled])

    roll_again = "yes"
    # While the player wants to keep rolling...
    while roll_again == "yes" or roll_again == "y":
        # Roll the three dice...
        print ("You rolled: ")
        for i in range(0, dice_per_turn):
            roll = dice[dice_to_roll[i]][(random.randint(0, max_sides - 1))]
            print(dice[dice_to_roll[i]][max_sides], " - ", roll)
            # If the player got a brain, add one to their brain total for this round and select another die
            # If the player got a shotgun, add one to their shotgun total for this round and select another die
            # If the player got a runner, do nothing and do not select another die
            if roll == "brain":
                brains+=1
                dice_to_roll[i] = dice_selections[dice_pulled]
                dice_pulled+=1
            elif roll == "shotgun":
                shotguns+=1
                dice_to_roll[i] = dice_selections[dice_pulled]
                dice_pulled+=1
                
        print ("brains = ", brains, "; shotguns = ", shotguns)
        # If the player has not rolled three shotguns, then ask them if they want to keep rolling
        if shotguns < 3:
            roll_again = input("Do you want to roll again?")
        else:
            break
    
    # If the player has not rolled three shotguns, then add the number of brains they rolled to their total score
    if shotguns < 3:
        scores[j%num_players]+=brains
        # Check whether the player has enough brains to win
        if scores[j%num_players] >= winning_score:
            print ("Player", j%num_players+1, "wins!")
            raise SystemExit
        else:
            print ("Your score is", scores[j%num_players])
    else:
        print("Argh! You got shot!!!")

    print ("")
