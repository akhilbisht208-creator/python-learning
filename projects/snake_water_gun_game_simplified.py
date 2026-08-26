import random

computer=random.choice([1,-1,0])
youstr=input("Enter your choice : ")
yourDict={"S":1,"W":-1,"G":0}
reverseDict={1:'S',-1:"W",0:"G"}
you=yourDict[youstr]

print(f"COMPUTER CHOSE {reverseDict[computer]} \nYOU CHOSE {reverseDict[you]}")

if(computer==you):
    print("DRAW")
else:
    if((computer-you)==-1 or (computer-you)==2):
        print("YOU LOSE")
    else:
        print("YOU WIN")