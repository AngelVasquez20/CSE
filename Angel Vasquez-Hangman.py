import random
guess = 8
Words = ["Apple", "Word", "Backpack", "Pencil", "Legs", "Mouse", "Dog", "Cat", "Guitar", "Shoe", "I love dogs!"]
random = random.choice(Words)
display = []

for i in range(len(display)):
    display[i] = "_"
print(' '.join(display))
print()

while guess < len(random):
    guess = input("Guess a letter: ")
    guess = guess.lower()
    print(guess)

for i in range(len(random)):
    if random[i] == guess:
        display[i] = guess
        guess = guess - 1

if guess == 0:
    input("You ran out of chances")
