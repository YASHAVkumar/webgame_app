import random
x = ["stone","paper","scissor"]
print("welcome user \n")
print("\n we have character stone paper scissor \n")
exit=0
win1=0
comp=0
while exit!='n':
    print("Enter your choice 1,2,3\n")
    player = int(input())
    print("PLAYER VALUE ", player)
    x = random.randrange(1, 4)
    print("COMPUTER VALUE ", x)
    if player == 1 and x == 2:
        print("Computer Won ")
        comp=comp+1
    elif x == 1 and player == 2:
        print("Player Won")
        win1=win1+1
    elif player == 2 and x == 3:
        print("Computer Won")
        comp=comp+1
    elif player == 3 and x == 2:
        print("Player Won")
        win1 = win1 + 1
    elif player == 1 and x == 3:
        print("Player Won")
        win1 = win1 + 1
    elif player == 3 and x == 1:
        print("Computer Won")
        comp=comp+1
    else:
        print("\nDraw\nTry again")
    print("\nDo you want to quit press n\n To continue y")
    exit=str((input()))

print("\n")
print("\n")
print("\n")
print("PLAYER WINS : {}    COMPUTER WINS : {}".format(win1,comp))





