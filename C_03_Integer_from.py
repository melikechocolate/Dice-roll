import math

def int_check():
    """checks users enter an integer more than / equal to 13"""

    error = "Please enter an integer more than / equal to 13"


    while True:
        try:
            reponse = int(input("what is the game gaol? "))

            if reponse < 13:
                print(error)
            else :
                return reponse

        except ValueError:
            print(error)


#response starts here.
game_goal = int_check()
print(game_goal)
