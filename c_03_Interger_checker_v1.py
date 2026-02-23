import math

error = "Please enter an integer more than / equal to 13"


while True:
    try:
        game_gaol = int(input("what is the game gaol? "))

        if game_gaol < 13:
            print(error)
        else :
            print(f"Game goal {game_gaol}")
            break

    except ValueError:
        print(error)

