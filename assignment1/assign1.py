# Rock-paper-scissors-lizard-Spock template
import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def number_to_name(number):
    if number ==0:
        name= "rock"
    elif number == 1:
        name= "Spock"
    elif number == 2:
        name= "paper"
    elif number == 3:
        name= "lizard"
    elif number == 4:
        name ="scissors"
    else:
        print "no such utility"
    return name
    # fill in your code below
    # convert number to a name using if/elif/else
    # don't forget to return the result!

    
def name_to_number(name):
    if name=="rock":
        number= 0
    elif name == "Spock":
        number= 1
    elif name == "paper":
        number= 2
    elif name == "lizard":
        number= 3
    elif name == "scissors":
        number= 4
    else:
        print "wrong number"
    return number
    # fill in your code below

    # convert name to number using if/elif/else
    # don't forget to return the result!


def rpsls(name): 
    
    
    # fill in your code below
    print "Player chooses "+name
    player_number=name_to_number(name)
    # convert name to player_number using name_to_number
    
    comp_number=random.randrange(0,4)
    comp_name=number_to_name(comp_number)
    print "Computer chooses "+comp_name
    # compute random guess for comp_number using random.randrange()
    diff=player_number-comp_number
    #modulo = diff%5
    
    if diff==1 or diff==2 or diff==-3 or diff==-4:
        print "Player wins!"
    elif diff==0:
        print "Match tie!"
    else:
        print "Computer wins!"
    
    # compute difference of player_number and comp_number modulo five

    # use if/elif/else to determine winner

    # convert comp_number to name using number_to_name
    
    # print results

    
# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


