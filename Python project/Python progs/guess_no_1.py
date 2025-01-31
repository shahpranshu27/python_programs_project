import random

def guess(x): #guessed by computer
    random_number=random.randint(1,x)
    guess=0
    while guess!=random_number:
        guess=int(input(f"guess a number between 1 and {x} : "))
        # print(guess)
        if guess < random_number:
            print("guess again! Too low")
        elif guess > random_number :
            print("guess again! Too high")
    print(f"Congrats!! you guessed the number {random_number}correctly ")
def computer_guess(x): # guessd by user
    low=1
    high = x
    feedback = ""
    while feedback != 'c':
        if low != high:
            guess = random.randint(low,high)
        else:
            guess=low
        feedback = input(f"is the guess {guess} too high(H) or too low(L) or correct(C)??").lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f"Comp  guessed {guess} it correctly")

computer_guess(10)

