# We all have played the game of Snake, Water, and Gun. , google the rules of this game and write a python program capable of playing this game with the usser.


import random

#"S"=1
#"W"=-1
#"G"=0

computer=random.choice([1,-1,0])
youstr=input("Enter your choice : ")
yourDict={"S":1,"W":-1,"G":0}
reverseDict={1:"Snake",-1:"Water",0:"Gun"}
you=yourDict[youstr]

print(f"you chose {reverseDict[you]} \ncomputer chose {reverseDict[computer]}")

if(computer==you):
    print("DRAW")
else:
    if(computer==-1 and you==1):
        print("YOU WON")

    elif((computer==-1 and you==0)):
        print("YOU LOSE")
    elif((computer==1 and you==-1)):
        print("YOU LOSE")
    elif((computer==1 and you==0)):
        print("YOU WIN")
    elif((computer==0 and you==-1)):
        print("YOU WIN")
    elif((computer==0 and you==1)):
        print("YOU LOSE")
    else:
        print("Something went wrong") 


