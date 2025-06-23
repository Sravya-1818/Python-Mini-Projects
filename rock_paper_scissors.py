import random
options=("rock","paper","scissor")
player=None
playerpoints=0
computerpoints=0
print("--------------------------------------------------------------------")
print("----------------WELCOME TO ROCK PAPER SCISSORS----------------------")
print("--------------------------------------------------------------------")
while True:
    computer=random.choice(options)
    player=input("ENTER A CHOICE(ROCK,PAPER,SCISSORS)-(Q TO QUIT)").lower()
    if player=='q':
        break
    elif player not in options:
        print("Invalid input. Please choose rock, paper, or scissor.")
        continue
    else:
        print(f"Player:{player}")
        print(f"Computer:{computer}")
        if player==computer:
            print("IT'S A TIE")
        elif player=='rock' and computer=='scissor':
            print("YOU WIN")
            playerpoints+=1
        elif player=='scissor' and computer=='paper':
            print('YOU WIN')
            playerpoints+=1
        elif player=='paper' and computer=='rock':
            print('YOU WIN')
            playerpoints+=1
        else:
            print('YOU LOSE')
            computerpoints+=1
print("--------------------------------------------------------------------")
print(f"Your points={playerpoints}      Computer points={computerpoints}")
print("THANK YOU FOR PLAYING THE GAME")
print("--------------------------------------------------------------------")
 



    
