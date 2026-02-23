
#initialise list to hold game history
game_History = []


while True:
    rounds_played = input("Round? ")
    if rounds_played == "":
        break


    user_points = int(input("User points? "))
    comp_points = int(input("Computer points? "))
    winner = input 
    user_score = int(input("User score: "))
    comp_score = int(input("Computer score: "))



    game_results = (f"Round {rounds_played}: User Points: {user_points} |"
    f" Computer Points {comp_points}, {winner} wins (15 | 0)"
    f"({user_score} | {comp_score})")


    game_History.append(game_results)

print("Game History")

for item in game_History:
    print(item)