import random


def game():
    print("you are playing the game..")
    score = random.randint(1,62)
    # fetch the hiscore
    with open("highscore.txt") as f:
        highscore = f.read()
        if(highscore!= ""):
            highscore = int(highscore)
        else:
            highscore = 0

    print(f"your score :{score}")
    if(score>highscore or highscore==""):
        #write this highscore to the file
        with open("highscore.txt","w") as f:
            f.write(str(score))
        return score

game()