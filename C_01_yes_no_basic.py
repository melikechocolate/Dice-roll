

def yes_no(Qustion):

    """code for yes or no"""


    while True:

        responce = input(Qustion).lower()

        #check the yes or no 
        if responce == "yes" or responce == "y":
            return "yes"
        elif responce == "no" or responce == "n":
            return "no"
        else:
            print("please enter yes or no")



want_instuctions = yes_no("Do you want the instructions? ")

print("="*25)
print("      program done")
print("="*25)