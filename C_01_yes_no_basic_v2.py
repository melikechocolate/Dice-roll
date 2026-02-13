

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




want_instructions = yes_no("Do you want to see the instructions? ")


if want_instructions == "yes":
    instructions()



print("="*25)
print("    program continues")
print("="*25)
