"""A number-guessing game."""
from random import randint

print("Howdy, what's your name?")
response = input()

answer = randint(1,100)

print(response + """, I'm thinking of a number between 1 and 100.
Try to guess my number.""")

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
                print("Well done,", response, "You found my number in", count, "tries!")
                break
            elif guess > answer:
                print("Your guess is too high, try again.")
            else:
                print("Your guess is too low, try again.")

                
# alternate solution using try and except

# while count >= 0:
#     guess = input()
#     print("Your guess? " + guess)
#     count += 1
#     try:
#         guess = int(guess)
#         if guess < 1 or guess > 100:
#             print("That is not between 1 and 100. Try again.") 
#         else:
#             if guess == answer:
#                 print("Well done,", response, "You found my number in", count, "tries!")
#                 break
#             elif guess > answer:
#                 print("Your guess is too high, try again.")
#             else:
#                 print("Your guess is too low, try again.")
#     except:
#         print("This is not a valid number. Try again.")