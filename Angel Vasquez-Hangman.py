import random
guesses = 8
words = ["Apple", "Word", "Backpack", "Pencil", "Legs", "Mouse", "Dog", "Cat", "Guitar", "Shoe", "I love dogs!"]
random = random.choice(words)

answer = list(words[0])
screen = []
screen.extend(words)
for i in range(len(screen)):
    screen[i] = "_"
print(' '.join(screen))
print()
while guesses < len(words):
    guess = input("Guess a letter: ")
    guess = guess.lower()
for i in range(len(answer)):
    if answer[i] == guesses:
        screen[i] = guesses
        guesses = guesses - 1

print("You Have Guessed the answer")
