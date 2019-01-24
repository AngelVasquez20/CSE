import random
guesses = 8
words = ["Apple", "Word", "Backpack", "Pencil", "Legs", "Mouse", "Dog", "Cat", "Myth", "Shoe", "I love dogs!"]
random = random.choice(words)
display = []
for i in range(len(display)):
    display[i] = "_"
print(' '.join(display))
print()

playing = True

while playing and guesses > 0:
    guess = input("Guess a letter: ")
    if int(guess) == int(random):
        print("You guesses the word")
        playing = False

    else:
        print("try again")
        guesses -= 1
