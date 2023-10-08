import random
l=int(input("enter lower bound : "))
u=int(input("enter upper bound : "))
cnt=0
c=random.randint(l,u)
for i in range(l,u):
    # print("computer guessed : ",c)
    x=int(input("enter your choice of number : "))
    print("you chose : ",x)
    if(x>c):
        print("guessed too high!!")
        cnt+=1
    elif(x<c):
        print("guessed too low!!")
        cnt+=1
    elif(x==c):
        print("guessed it right!!")
        cnt+=1
        print("total guesses : ",cnt)
        break