
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
            print("please enter yes or no")

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


    while True:
        try:
            reponse = int(input("what is the game gaol? "))

            if reponse < 13:
                print(error)
            else :
                return reponse

        except ValueError:
            print(error)


want_instructions = yes_no("Do you want to see the instructions? ")


if want_instructions == "yes":
    instructions()

game_goal=int_check()
print(game_goal)


#-----------------------------------------------------------------
