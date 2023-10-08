import random
r,p,s=0,0,0
x=1
while x == True:
    choice = input("enter your choice : ")
    if choice=="y":
        player1=random.randint(1,3)
        player2=int(input("1. rock \n2. paper \n3. scissor"))
        print("computer's choice : ",player1)
        print("user's input : ",player2)
        if(player1==1):
            if(player2==1):
                print("Tie")
            elif(player2==2):
                print("Player 2 won!!")
            elif(player2==3):
                print("player 1 won!!")
        elif(player1==2):
            if(player2==1):
                print("player 1 won!!")
            elif(player2==2):
                print("Tie")
            elif(player2==3):
                print("player 2 won")
        elif(player1==3):
            if(player2==1):
                print("player 2 won")
            elif(player2==2):
                print("player 1 won!!")
            elif(player2==3):
                print("Tie")
    else:
        print("Thanks for playing!!")
        x=False