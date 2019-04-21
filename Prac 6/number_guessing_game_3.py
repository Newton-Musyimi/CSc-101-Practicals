"""This is a game in which the user has to make an accurate guess of a number in a range to
advance onto the next level. It has 10 levels. The player gets 5 guesses"""
import random
def level_gen2(i,levels):
    level=levels[i]
    return level
def guess_value2(level_upper):
    guess=random.randrange(0,level_upper)
    return guess
def game_progression2():
    levels=[1,2,3,4,5,6,7,8,9,10]
    guesses = 4
    game_over = False
    player = int(input("enter a number "))
    for i in range(0,10):
        level = level_gen2(i,levels)
        level_upper = level *10
        while guesses >= 0 and game_over ==False:
            print("Level is ",level)
            print("Guesses left are ",guesses)
            print("")
            guess = guess_value(level_upper)
            if guess == player and level<10:
                guesses += 4
                print ("Congratulations the computer proceeds!!")
                game_over = False
                break
            elif guesses>0 and level<10:
                guesses -= 1
                print ("Sorry PC, try again")
            elif guesses == 0:
                print("GAME OVER, YOU LOSE!!!")
                game_over = True
                game = "lose"
            elif level==10 and player!=guess:
                guesses-=1
                print("Try Again")
            elif player==guess and level==10:
                print("YOU WIN!")
                game = "win"
                game_over = True
                
    return game
                    
def game2():
    game = "neutral"
    while game != "win":
        game = game_progression2()
        if game == "lose":
            return
    
if __name__ == "__main__":
    main()