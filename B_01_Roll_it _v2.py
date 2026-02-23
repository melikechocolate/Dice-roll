import time, sys, random, os 

def yes_no(Qustion):

    """code for yes or no"""


    while True:

        responce = input(Qustion).lower()

        #check the yes or no 
        if responce == "yes" or responce == "y":
            return "yes"
            print(instructions)
        elif responce == "no" or responce == "n":
            return "no"
        else:
            print("\n\033[91m[!] ERROR: please enter yes or no...\033[0m\n")

#------------------------------------------------------------


def instructions():
    """gives instructions"""

    print("""
=============================   
   **** Instructions ****         
    
Roll the dice and try to win  
=============================        
    """)
#------------------------------------------------------------

def int_check():
    """checks users enter an integer more than / equal to 13"""

    error = "Please enter an integer more than / equal to 13"
#-------------------------------------------------------------

def clear():
    """Wipes the terminal screen clean."""
    # 'nt' is the internal name for Windows
    if os.name == 'nt':
        os.system('cls')
    # Otherwise, it's Mac or Linux
    else:
        os.system('clear')

def intial_points(which_player):
    """Roll dice twice and return total / if double points apply"""

    double = "no"

    #Roll the dice for the user and note if they got a double
    roll_one = random.randint( 1, 6)
    roll_two = random.randint( 1, 6)

    if roll_one == roll_two:
        double = "yes" 
    
    total = roll_one + roll_two

    print(f"{which_player} - Roll 1: {roll_one} \t| Roll 2: {roll_two} \t| Total: {total}")

    return total, double

def make_statement(statment, decoration):
    """add emoje"""

    end = decoration * 3
    print(f"\n{end} {statment} {end}")


#Clear the Run station to make it look good
clear()

print("\n\033[93m  [#] GAME START\033[0m",)
print()
#Main starts here

# At the start of the game, the comouter / user score are both zero
comp_score = 0
user_score = 0
Round_Played = 0

game_History = []

make_statement("Welcome to roll it 13 Game", "-")
print()

want_instructions = yes_no("Do you want to see the instructions? ")


if want_instructions == "yes":
    instructions()

game_goal = int_check()
print(game_goal)


game_goal = int(input("Game Goal: ")) # be called a founction cell.

# Play multiple rounds until a winner has been found
while comp_score < game_goal and user_score < game_goal:

    Round_Played += 1

    #Start of round loop
    make_statement( f"Round {Round_Played}", "🎲")
    #For testing purposes, ask the user what the points for the user / computer were
    # Roll the dice for the and note if they got a double
    initial_user = intial_points("User")
    initial_comp = intial_points("comp")

    #Retrieve user points frist item returned from function

    # Intieline rouncs points
    user_points = initial_user[0]
    comp_ponits = initial_comp[0]

    double_user = initial_user[1]
    #Let the user know if they qualify for double points
    if double_user == "yes":
        print("Great news - if you win, you will earn double points!")
    
    # assume user goes first...
    first = "User"
    second = "Computer"
    player_1_points = user_points
    player_2_ponits = comp_ponits

    # if user has fewer ponits, they start the game 
    if user_points < comp_ponits:
        print("You start because your initial your roll was less than the computer\n")

    # if the user and computer roll equal points, the user is player 1...
    elif user_points == comp_ponits:
        print("The initial roll were the same, the user starts!")

    # if the computer has fewer ponits, which the ompter to player 1'
    else:
        player_1_points, player_2_ponits = player_2_ponits, player_1_points

        first, secound = second, first

    while player_1_points < 13 and player_2_ponits < 13:
        print()
        input("press <enter> to contine this round\n")

        #Frist person rolls the die and scores is updated
        player_1_roll = random.randint( 1, 6)
        player_1_points += player_1_roll


        print(f"{first}: Rolled a {player_1_roll} - has {player_1_points} points")


        # if the frist person's score is over 13, end the round
        if player_1_points>= 13:
            break 

        # secound person roll the die (and scoure is update)
        player_2_roll = random.randint( 1, 6)
        player_2_ponits += player_2_roll

        print(f"{second}: Rolled a {player_2_roll} - has {player_2_ponits} points")
        print(f"{first}: {player_1_points} | {second} {player_2_ponits}")

    # end of round 

    # associate player points with either the user or the computer
    user_points = player_1_points
    comp_ponits = player_2_ponits

    if first == "Computer":
        user_points, comp_ponits = comp_ponits, user_points

    # work ou who won..
    if user_points >comp_ponits:
        winner = "user"
        loser = "computer"
        comp_ponits = 0 

        round_feedback = f"""
        >>>>>>>>>><<<<<<<<<<
            The {winner} won.
        >>>>>>>>>><<<<<<<<<<
        """
    else:
        winner = "computer"
        loser = "user"
        user_points = 0 

        round_feedback = f"""
        >>>>>>>>>><<<<<<<<<<
         The {winner} won.
        >>>>>>>>>><<<<<<<<<<
            """
    
    round_feedback = f"The {loser}'s points have been set to zero"
    # double user points if eligible 
    if winner == "user" and double_user == "yes":
        user_points = user_points * 2

    # line centering
    X30_line_S3 = "#"*30
    Round_Reults = "Round Reults"

    # Out round results
    for i in range(11):
        b =  b = '█'*i + '░'*(10-i)
        print(f'\rProgress. [{b}] {i*10}%', end=''); time.sleep(0.1)
    clear()
    print(f"   {X30_line_S3:^30}")
    print(f"   {Round_Reults:^30}") # 9 sapces
    print(f"   {X30_line_S3:^30}")
    print(f"User Points: {user_points} | Computer Points: {comp_ponits}")
    print("^"*38)
    print(round_feedback)
    print()


    # Outside round loop - Update sorce with round points, only add points to the score of the 
    comp_score += comp_ponits
    user_score += user_points

#makes the game history in a list.
    game_results = (f"Round {Round_Played}: User Points: {user_points} |"
    f""
    f" Computer Points {comp_ponits}, {winner} wins (15 | 0)"
    f""
    f"({user_score} | {comp_score})")

    game_History.append(game_results)


    # show overall scores (add this to round loop)
    for c in " *** Game Update ***\n": sys.stdout.write(c); sys.stdout.flush(); time.sleep(0.05)
    print(f"User Score: {user_score} | Computer Sorce  {comp_score}")



# end of entire game, output final reults

print()
if user_score > comp_score:
    print(f"╔{'═'* 14 }╗\n| The user won |\n╚{'═'* 14}╝")
else:
    print(f"╔{'═'* 18 }╗\n| The computer won |\n╚{'═'* 18}╝")

for c in '-----Game-History-----': sys.stdout.write(c); sys.stdout.flush(); time.sleep(0.05)
print()

for item in game_History:
    print(item)


print("\n\033[93m  [#] GAME END\033[0m",)
print()