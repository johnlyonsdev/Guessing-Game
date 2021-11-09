"""A number-guessing game."""
from random import randint

print("Howdy, what's your name?")
name = input()

high = 101

def guessingGame(high):
    answer = randint(1,100)
    print(name + """, I'm thinking of a number between 1 and 100.\nTry to guess my number.\nYou will only have 10 guesses. Begin!""")
    count = 0
    while count >= 0:
        guess = input()
        print("Your guess? " + guess)
        count += 1
        if guess.isnumeric() == False:
            print("That is not a valid number. Try again.")
        else:
            guess = int(guess)
            if guess < 1 or guess > 100:
                print("That is not between 1 and 100. Try again.") 
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
                    if count > 9:
                        print('Game over! You took too many tries!\n''To play again input "Yes". To quit, input something else.')
                        response = input()
                        if response == 'Yes':
                            guessingGame(high)
                        else:
                            exit()
                    else:
                        print("Your guess is too high, try again.")
                else:
                    if count > 9:
                        print('Game over! You took too many tries!\n''To play again input "Yes". To quit, input something else.')
                        response = input()
                        if response == 'Yes':
                            guessingGame(high)
                        else:
                            exit()
                    else:
                        print("Your guess is too low, try again.")

guessingGame(high)