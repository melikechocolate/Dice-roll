import time, sys, os

# At the start of the game, the comouter / user score are both zero
comp_score = 0
user_score = 0

game_goal = int(input("Game Goal: ")) # be called a founction cell.
# Play multiple rounds until a winner has been found
while comp_score < game_goal and user_score < game_goal:

    #Start of round loop
    #For testing purposes, ask the user what the points for the user / computer were
    comp_points = int(input("Enter the computer points at the end of the round: "))
    user_points = int(input("Enter the user points at the end of the round: "))

    # Outside round loop - Update sorce with round points, only add points to the score of the 
    comp_score += comp_points
    user_score += user_points

    # show overall scores (add this to round loop)
    for c in " *** Game Update ***\n": sys.stdout.write(c); sys.stdout.flush(); time.sleep(0.05)
    print(f"User Score: {user_score} | Computer Sorce  {comp_score}")



# end of entire game, output final reults
print()
if user_score > comp_score:
    print(f"╔{'═'* 14 }╗\n| THE USER WON |\n╚{'═'* 14}╝")
else:
    print(f"╔{'═'* 18 }╗\n| THE COMPUTER WON |\n╚{'═'* 18}╝")