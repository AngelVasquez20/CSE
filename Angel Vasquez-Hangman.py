import random
guess = 8
Words = ["Apple", "Word", "Backpack", "Pencil", "Legs", "Mouse", "Dog", "Cat", "Guitar", "Shoe", "I love dogs!"]
random = random.choice(Words)
display = []

for i in range(len(display)):
    display[i] = "_"
print(' '.join(display))
print()

while guess < len(Words):
    guess = input("Guess a letter: ")
    guess = guess.lower()
    print(guess)

for i in range(len(Words)):
    if Words[i] == guess:
        display[i] = guess
        guess = guess - 1
