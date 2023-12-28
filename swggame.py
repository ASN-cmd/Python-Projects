import random

c = [0,1,2]
u = [0,1,2,3]
computer = random.choice(c)

print("Enter a Choice")
print("0 for Snake, 1 for Water, 2 for Gun and 3 to Quit")
user = int(input())

if(computer == user):
    print("Computer choosed", computer)
    print("DRAW")
elif(computer == 0 and user == 1 or computer == 1 and user == 2 or computer == 2 and user == 0 ):
    print("Computer choosed", computer)
    print("Lose")
else:
    print("Computer choosed", computer)
    print("WON")



