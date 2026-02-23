import random, time, os
#clear

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

    round_feedback = f"""
    >>>>>>>>>><<<<<<<<<<
        The {winner} won.
    >>>>>>>>>><<<<<<<<<<
    """
else:
    winner = "computer"

    round_feedback = f"""
    >>>>>>>>>><<<<<<<<<<
      The {winner} won.
    >>>>>>>>>><<<<<<<<<<
        """
  
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
print(f"{X30_line_S3:^30}")
print(f"{Round_Reults:^30}") # 9 sapces
print(f"{X30_line_S3:^30}")
print(f"User Points: {user_points} | Computer Points: {comp_ponits}")
print("^"*38)
print(round_feedback)
print()