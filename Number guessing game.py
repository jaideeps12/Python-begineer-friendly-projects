import random
print("Welcome to the number guessing game")
print("You will have 6 choices")
Lower_value=int(input("Enter the lower limit of the numbers: "))
Upper_value=int(input("Enter the upper limit of the numbers: "))
num=random.randint(Lower_value,Upper_value)
n=0
cc=6
while n<cc:
    n=n+1
    guess=int(input("Enter your choice"))
    if guess==num:
        print("Yippe,you got it")
        break
    elif n>=cc and guess!=num:
        print("The number was",num,"Better luck net time")
    elif guess>num:
        print("The number is high, but you are close")
    elif guess<num:
        print("The number is low but too close")