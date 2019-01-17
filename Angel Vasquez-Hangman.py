import random
guess = 8
answerlist = ["Apple", "Word", "Backpack", "Pencil", "Legs", "Mouse", "Dog", "Cat", "Guitar", "Shoe", "I love dogs!"]
random = random.choice(answerlist)
answer = list(answerlist[0])
letters_guessed = []
display = []
display.extend(answer)

for i in range(len(display)):
    display[i] = "_"

print(' '.join(display))
print()

count = 0

while count < len(answer):
    guess = input("Guess a letter: ")
    guess = guess.lower()
    print(count)

for i in range(len(answer)):
    if answer[i] == guess:
        display[i] = guess
        count = count + 1

print(' '.join(display))
print()
