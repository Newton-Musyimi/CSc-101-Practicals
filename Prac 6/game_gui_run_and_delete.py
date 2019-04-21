import random
import turtle

my_screen = turtle.Screen()
feedback = turtle.Turtle()
feedback.ht()
board = turtle.Turtle()
board.ht()
bxoffset = -200
byoffset = 200
xoffset = 200
yoffset = 200


def makeSecret(level):
    return random.randrange(0, level * 10)


def displayInfo(level, guesses):
    feedback.clear()
    feedback.goto(xoffset, yoffset)
    feedback.write("level:" + str(level))
    feedback.goto(xoffset, yoffset - 10)
    feedback.write("Guesses left: " + str(guesses))

    print("level: ", level)
    print("Gueusses left:", guesses)


def drawBoard(level):
    board.penup()
    for i in range(level):
        for j in range(10):
            board.goto(bxoffset + j * 10, byoffset)
            board.write(str(i) + str(j))


def markGuess(guess):
    board.goto(bxoffset + 30 * (guess % 10), byoffset)
    board.stamp()


def game(level, guesses, secret):
    print(secret)
    displayInfo(level, guesses)
    guess = -1
    board.clear()
    drawBoard(level)
    while guesses >= 0 and guess != secret:
        guess = my_screen.numinput("Guess a number", "Please make a guess: ")
        markGuess(guess)
        displayInfo(level, guesses)
        feedback.goto(xoffset, yoffset - 20)
        if guess > secret:
            feedback.write("Too big, please guess a smaller number")
        elif guess < secret:
            feedback.write("Too small, please guess a bigger number")
        else:
            feedback.write("Well Done! you got it!")
        return True
    guesses = guesses - 1
    return False


def main():
    level = 1
    guesses = 4
    while guesses >= 0 and level <= 10:
        (won, guesses) = game(level, guesses, makeSecret(level))
        if won:
            guesses = guesses + 4
            level = level + 1
        else:
            break
    if guesses > 0 and level >= 10:
        print("Well done, you have beaten the game")
    else:
        print("Too bad, you lose")
    my_screen.exitonclick()


if __name__ == "__main__":
    main()
