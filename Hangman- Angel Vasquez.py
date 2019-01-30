import random
import string
win = False
guess = 8
pun = list(string.punctuation)
list1 = list()
alphabet = list(string.ascii_letters)
words = ["Apple",
         "Word",
         "Backpack",
         "Pencil",
         "Legs",
         "Mouse",
         "Dog",
         "Cat",
         "Myth",
         "Shoe",
         "I love dogs!"]

random = random.choice(words)
letters_guessed = []


for i in range(len(random)):
    if random[i] in alphabet:
        list1.pop(i)
        list1.insert(i, "_")
    if random[i] in pun:
        list1.insert(i, "!")
print("".join(list1))
print(' '.join(words))

while guess > 0 and not win:
    guess1 = input("Guess a letter: ")
    print(guess)
    letters_guessed.append(guess1.lower())
    for i in range(len(words)):
        if random[i].lower() in letters_guessed:
            list1.pop(i)
            list1.insert(i, words[i])

if guess1.lower() not in list1 and guess1.upper() not in list1:
    guess -= 1
    print("".join(list1))
if "_" not in list1:
    win = True
    print("Well done winner you have guessed the word.")
