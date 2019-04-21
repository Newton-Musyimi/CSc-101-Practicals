"""This is a game in which the user has to make an accurate guess of a number in a range to
advance onto the next level. It has 10 levels. The player gets 5 guesses"""
import random
levels=[1,2,3,4,5,6,7,8,9,10]
def game_progression(levels):
    guesses = 5
    for i in range(0,10):
        level=levels[i]
        level_upper = level *10
        guess = random.randrange(0,level_upper)
        while guesses >= 0:
            player = int(input("What is the number generated? "))
            if player==guess:
                guesses += 4
                print ("Congratulations, you proceed!!")
                pass
            elif guesses>0:
                guesses -= 1
                print ("Sorry")
        if player==guess and level==10:
            print("YOU WIN!")
        if guesses == 0:
            print("GAME OVER, YOU LOSE!!!")
            break
        
            
        
game_progression(levels)