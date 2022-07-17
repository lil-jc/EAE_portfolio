#make choices scissors, paper, stone.

#write of statement to rule |scissors over paper|paper over stone|stone over scissos.

#make computer choose scissors, paper, stone.

#print output

#loop everything
import random
choices = ["scissors", "paper", "stone"]

def user_win(user_choice, com_choice):
    user_points=0
    com_points=0
    if user_choice == "scissors" and com_choice == "paper":
        print("you win!")
        new_user_points=user_points+1
        return 1
    if user_choice == "paper" and com_choice == "stone":
        print("you win!")
        new_user_points=user_points+1
        return 1
    if user_choice == "stone" and com_choice == "scissors":
        print("you win!")
        new_user_points=user_points+1
        return 1
    print("you did not win")
    new_com_points=com_points+1
    return 0

def user_choice():
    user_choice= input("Scissors paper stone! Enter stop to exit game: ").lower().strip()
    print("user choice: ", user_choice)
    return user_choice

def com_choice():
    com_choice = random.choice(choices)
    return com_choice

def game():
    c = com_choice()
    u = user_choice()
    if u == "stop":
        return False
    print("computer choice: ", c)
    user_win(u,c)
    if new_com_points<10 and new_user_points<10:
        return True
    if new_com_points>=10 or new_user_points>=10:
        print("~end of game~")
        return False

while game():
    continue
    

        


# TASKS:
# Make program exit when user enters "stop"
# Implement a score counter to count score
    # Make program exit automatically after a player (either com or user) reaches 10
# Implement function to determine whether it is a draw or a loss

