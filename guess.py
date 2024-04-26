import random

def start(n):
    numlist = []
    for i in range(n):
        numlist.append(i)
    randomnum = random.randrange(n)
    print("----------------Lets start--------------")
    p1g = int(input("Enter player 1 guess:"))    
    p2g = int(input("Enter player 2 guess:"))
    
    l1 = numlist[randomnum:p1g]
    l2 = numlist[randomnum:p2g]
    
    if p1g == randomnum:
        print()
    
    if len(l1)<len(l2):
        print("player 1 is close to the number.So",p1,"is the winner")
    elif len(l1)>len(l2):
        print("player 2 is close to the number.So",p2,"is the winner")
    elif len(l1) == len(l2):            
        print("Its a tie.Both were equally close to the number")
    print("The number was",randomnum)
    
    
n = int(input("Enter the range for guessing i.e:{10 for 0 to 10} :"))
p1 = input("Enter player 1 name:")
p2 = input("Enter player 2 name:")
start(n)
