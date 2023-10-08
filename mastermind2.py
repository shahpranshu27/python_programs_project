# Mastermind game or code breaker for 5 digits
import random

num = random.randrange(10000,100000)

n=int(input("enter 5 digit number : "))

if(n==num):
    print("Great!! You guessed it in 1st guess, you are a mastermind!")
else:
    # cnt variable is initialized, it will keep count of number of tries player takes
    cnt = 0
    while(n!=num):
        # variable inccrements every time the loop is executed
        cnt+=1
        # for number of digits which are guessed correctly 
        count = 0
        # explicit type conversion of an integer to a string in order to ease extracting digits
        n =  str(n)
        # print(n)
        # explicit type conversion of string to an integer
        num = str(num)
        # print(num)
        # correct[] list stores digits which are correct
        correct = []*5

        # the for loop runs 5 times, since it's a 5 digit number
        for i in range(0,5):
            if(n[i]==num[i]):
                # number of digits guessed correctly
                count+=1
                # hence, the digit is stored in correct[]
                correct.append(n[i])
            else:
                continue
        # if the digits guessed correctly are < 5
        if((count<5)and (count!=0)):
            print("not quite the number, but you guessed ",count," digits correctly!!")
            print("Also these numbers in your input were correct.")
            # to show which digits are correctly placed
            for k in correct:
               print(k, end=' ')
            print('\n')
            print('\n')

            n = int(input("enter you next choice of numbers : "))

        elif(count == 0):
            print("none of the numbers in your input matches")
            n = int(input("enter your next choice of numbers : "))
    if(n==num):
        cnt += 1
        print("you've become mastermind, it took only ",cnt," tries to guess the number")
        if(cnt>15):
            print("you could have done better!!")