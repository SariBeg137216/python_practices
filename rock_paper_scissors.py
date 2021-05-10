import random

input_list = ['r', 'p', 's']
AI_win = 0
User_win = 0
while True:
    print("player win {} time".format(User_win))
    print("AI win {} time".format(AI_win))

    AI = random.choice(input_list)
    player = input("please enter rock-paper or scissors:")

    if AI == player:
        print("its Tie")
    elif AI == 'r' and player == 's':
        print("AI win")
        AI_win += 1
    elif AI == 'p' and player == 'r':
        print("AI win")
        AI_win += 1
    elif AI == 's' and player == 'p':
        print("AI win")
        AI_win += 1
    else:
        print("USER win")
        User_win += 1
