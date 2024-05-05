import random
print('snake-water-gun')
n = int(input("enter number of rounds:"))
options =['s','g','w']
rounds = 1
comp_win=0
user_win = 0
while rounds <= n:
    print(f"Round:{rounds}\nSnake - 's'\nwater - 'w' \nGun - 'g'")
    try:
        player = input("choose your option:")
    except EOFError as e :
        print(e)
    if player !='s' and player !='w' and player !='g':
        print("invalid input try again")
        continue
    computer = random.choice(options)
    if computer =='s':
        if player == 'w':
            comp_win += 1
        elif player == 'g':
            user_win+=1
    elif computer == 'w':
        if player == 'g':
            comp_win += 1
        elif player == 's':
            user_win += 1
 
    elif computer == 'g':
        if player == 's':
            comp_win += 1
        elif player == 'w':
            user_win += 1
    if user_win> comp_win:
        print(f"You won Round {rounds}\n")
    elif comp_win> user_win:
        print(f"Computer won round {rounds}\n")
    else:
        print("draw!!\n")
    rounds += 1
if user_win>comp_win:
    print("congratulation You won")
elif comp_win>user_win:
    print("You lost the game")
else : 
    print("MAtch dRaw")            
        