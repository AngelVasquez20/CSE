import random
answer = random.radint (1, 10)
guesses = 5
playing = True
while guesses > 0 and playing:
    guess = int (input("type in an number"))
    if