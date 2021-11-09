"""A number-guessing game."""
from random import randint

print("Howdy, what's your name?")
name = input()

def enterMin():
    while high == 11:
        print('Please enter the minimum value in your range.')
        min = input()
        if min.isnumeric() == False:
                print("That is not a valid number. Try again.")
        else:
            min = int(min)
            return min

def enterMax():
    while high == 11:
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
    return guessLimit



def guessingGame(high):
    answer = randint(min,max)
    print(name + ", I'm thinking of a number between", min, "and", max,".\nTry to guess my number.\nYou will only have", guessLimit, "guesses. Begin!")
    count = 0
    while count >= 0:
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
                    print('To play again input "Yes". To quit, input something else.')
                    response = input()
                    if response == 'Yes':
                        guessingGame(high)
                    else:
                        exit()

                elif guess > answer:
                    if count > guessLimit-1:
                        print('Game over! You took too many tries!\n''To play again input "Yes". To quit, input something else.')
                        response = input()
                        if response == 'Yes':
                            guessingGame(high)
                        else:
                            exit()
                    else:
                        print("Your guess is too high, try again.")
                else:
                    if count > guessLimit-1:
                        print('Game over! You took too many tries!\n''To play again input "Yes". To quit, input something else.')
                        response = input()
                        if response == 'Yes':
                            guessingGame(high)
                        else:
                            exit()
                    else:
                        print("Your guess is too low, try again.")

high = 11
min = 0
max = 100
guessLimit = 10
print('Would you like to select your own range of numbers to guess from?\nInput "Yes" to enter a range, input no to play with the classic 1-100 variant.')
response = input()
if response == 'Yes':
    min = enterMin()
    max = enterMax()
    guessLimit = findLimit()
    
guessingGame(high)