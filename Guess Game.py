import random

guesses = 5
playing = True
random_integer = random.randint(1, 10)
while playing and guesses > 0:
    guess = input("Choose a number from 1 and 10")
    if int(guess) == int(random_integer):
        print("You have won!!")
        playing = False

    else:
        print("Try Again!!")
        guesses -= 1
    if int(guess) > int(random_integer):
        print("Too High")
    if int(guess) < int(random_integer):
        print("Too Low")
