def is_arm(num):
    num_str=str(num)
    n=len(num_str)
    sum=0
    for i in num_str:
        sum+=int(i)**n
    return sum==num
num=int(input("enter n :"))
if is_arm(num):
    print("armstrong")
else:
    print("not armstrong")
