# The game () function in a program lets a user play a game return the score as an integer ,
# you need to read a file "Hi-score.txt" which is either blank or conatins the previous Hi-score , 
# You need to WAP to update the Hi-score whenever the game() function breaks the Hi-score

import random

def game():

    print("YOU ARE PLAYING")
    score=random.randint(1,62)
    with open("file_input_and_ouput/hiscore.txt") as f:
        highscore=f.read()

        if(highscore!=""):
            highscore=int(highscore)
        else:
            highscore=0

    print(f"YOUR SCORE {score}")

    if(score>highscore):

        with open("file_input_and_ouput/hiscore.txt","w") as f:
            f.write(str(score))



        return score

game()

