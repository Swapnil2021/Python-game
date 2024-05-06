import random 
import math 
lower = int(input("Enter Lower bounds:-"))
upper = int(input("Enter Upper bounds:-"))
x = random.randint(lower,upper)
print("\n\tYou've only ",round(math.log(upper-lower +1,2)),"chances to guess the integer!\n")
count = 0
while count< math.log(upper-lower +1,2):
    count+=1
    guess = int (input ("Guess a Number:- "))
    if x == guess: 
        print("Congrratulations you did it in",count,"try")
        break
    elif x > guess:
        print("You guessed too small!")
    elif x< guess  :
        print("You Guessed too High !")
if count >= math.log (upper- lower +1,2):
    print("\nThe number is %d"%x)
    print("\tBetter Luck Next time!")