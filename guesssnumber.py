import random
while True:
    guess = int(input("Enter a number between 1 and 10: "))
    if guess == random.randrange(1, 11):
        print("You guessed it right")
