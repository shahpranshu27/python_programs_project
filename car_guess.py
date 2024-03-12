import random
name=input("enter your name : ")
print("Good luck! ",name)
cars=["Audi","Jaguar","Ferrari","Lamborghini","Mustang","Ford","Tata","Hyundai","Bmw","Mercedes","Volvo"]
car=random.choice(cars)
print("Guess the car in 12 turns!!")
guesses=""
turns=12
while turns>0:
    fail=0 # number of times you failed to guess the car
    for char in car:
        if char in guesses:
            print(char,end=" ")
        else:
            print("_")
            fail+=1
    if fail==0:
        print("You win!!")
        print("the car is : ",car)
        break
    print()
    guess=input("guess the character of car : ")
    guesses+=guess

    if guess not in car:
        turns-=1
        print("you chose wrong character!")
        print("You have ",turns," more to guess the car!")

        if turns==0:
            print("You lose!!")