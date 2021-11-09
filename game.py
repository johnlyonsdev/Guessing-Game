"""A number-guessing game."""
from random import randint


def askGame():
    min = enterMin()
    max = enterMax()
    guessLimit = findLimit()
    guessMin = min
    guessMax = max
    count = 0
    print('The computer will be guessing between', min, 'and', max, ". It will have", guessLimit, "guesses.")
    while const == True:
        print('Please enter the number the computer will be guessing for.')
        answer = input()
        if answer.isnumeric() == False:
                print("That is not a valid number. Try again.")
        else:
            answer = int(answer)
            if answer < min or answer > max:
                print("That is not between", min, "and", max,". Try again.") 
            else:
                while const == True:
                    guess = randint(guessMin, guessMax)
                    count += 1
                    print('The computer guessed', guess)
                    if guess == answer:
                        while const == True:
                            print("Haha! The computer found your number in", count, 'tries!\nTo play again input "Play again". To quit, input "Quit".')
                            response = input()
                            if response == 'Play again':
                                askGame()
                            elif response == 'Quit':
                                exit()
                            else:
                                print('Please enter "Play again" or "Quit".')

                    elif guess > answer:
                        if count > guessLimit-1:
                            while const == True:
                                print('You win! The computer took too many tries!\n''To play again input "Play again". To quit, input "Quit".')
                                response = input()
                                if response == 'Play again':
                                    askGame()
                                elif response == 'Quit':
                                    exit()
                                else:
                                    print('Please enter "Play again" or "Quit".')
                        else:
                            print("It's guess is too high.")
                            guessMax = guess-1
                    else:
                        if count > guessLimit-1:
                            while const == True:
                                print('You win! The computer took too many tries!\n''To play again input "Play again". To quit, input "Quit".')
                                response = input()
                                if response == 'Play again':
                                    askGame()
                                elif response == 'Quit':
                                    exit()
                                else:
                                    print('Please enter "Play again" or "Quit".')
                        else:
                            print("It's guess is too low.")
                            guessMin = guess+1




def enterMin():
    while const == True:
        print('Please enter the minimum value in your range.')
        min = input()
        if min.isnumeric() == False:
                print("That is not a valid number. Try again.")
        else:
            min = int(min)
            return min

def enterMax():
    while const == True:
        print('Please enter the maximum value in your range.')
        max = input()
        if max.isnumeric() == False:
                print("That is not a valid number. Try again.")
        else:
            max = int(max)
            if max <= min:
                print("The maximum value needs to be greater than the minimum value.")
            else:
                return max

def findLimit():
    range = max - min
    if range < 3:
        guessLimit = 1
    elif range < 7:
        guessLimit = 3
    elif range < 13:
        guessLimit = 5
    elif range < 25:
        guessLimit = 7
    elif range < 54:
        guessLimit = 10
    else:
        guessLimit = range / 5
        guessLimit = round(guessLimit)
    return guessLimit



def guessingGame(high):
    answer = randint(min,max)
    print(name + ", I'm thinking of a number between", min, "and", max,".\nTry to guess my number.\nYou will only have", guessLimit, "guesses. Begin!")
    count = 0
    while const == True:
        guess = input()
        print("Your guess? " + guess)
        count += 1
        if guess.isnumeric() == False:
            print("That is not a valid number. Try again.")
        else:
            guess = int(guess)
            if guess < min or guess > max:
                print("That is not between", min, "and", max,". Try again.") 
            else:
                if guess == answer:
                    print("Well done,", name, "You found my number in", count, "tries!")
                    if count < high:
                        high = count
                        print('Congratulations on your new high score!')
                    else:
                        print("Oh no! You did not beat your high score of", high)
                    while const == True:
                        print('To play again input "Play again". To quit, input "Quit".')
                        response = input()
                        if response == 'Play again':
                            guessingGame(high)
                        elif response == 'Quit':
                            exit()
                        else:
                            print('Please enter "Play again" or "Quit".')

                elif guess > answer:
                    if count > guessLimit-1:
                        while const == 0:
                            print('Game over! You took too many tries!\n''To play again input "Play again". To quit, input "Quit".')
                            response = input()
                            if response == 'Play again':
                                guessingGame(high)
                            elif response == 'Quit':
                                exit()
                            else:
                                print('Please enter "Play again" or "Quit".')
                    else:
                        print("Your guess is too high, try again.")
                else:
                    if count > guessLimit-1:
                        while const == 0:
                            print('Game over! You took too many tries!\n''To play again input "Play again". To quit, input "Quit".')
                            response = input()
                            if response == 'Play again':
                                guessingGame(high)
                            elif response == 'Quit':
                                exit()
                            else:
                                print('Please enter "Play again" or "Quit".')
                    else:
                        print("Your guess is too low, try again.")

print("Howdy, what's your name?")
name = input()
const = True
min = 1
max = 100
guessLimit = 10

print(name+', would you like to ask or guess?\nInput "Ask" to ask, input "Guess" else to guess')
while const == True:
    response = input()
    if response == 'Ask':
        askGame()
    elif response == 'Guess':
        print('Would you like to select your own range of numbers to guess from?\nInput "Yes" to enter a range, input "No" to play with the classic 1-100 variant.')
        while const == True:
            response = input()
            if response == 'Yes':
                min = enterMin()
                max = enterMax()
                guessLimit = findLimit()
            elif response == 'No':
                high = guessLimit + 1
                guessingGame(high)
            else:
                print('Please enter "Yes" or "No".')
    else:
        print('Please enter "Ask" or "Guess".')
