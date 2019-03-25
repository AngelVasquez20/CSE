import random
import string

guess = 8
pun = list(string.punctuation)
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
random_word = list(random)
letters_guessed = []

win = False
for i in range(len(random)):
    if random[i] in alphabet:
        random_word.pop(i)
        random_word.insert(i, "_")
    if random[i] in pun:
        random_word.insert(i, "!")
print(' '.join(random_word))

while guess > 0 and not win:
    guess1 = input("Guess a letter: ")
    print(guess)
    letters_guessed.append(guess1.lower())
    for i in range(len(random)):
        if random[i].lower() in letters_guessed:
            random_word.pop(i)
            random_word.insert(i, random[i])
    if guess1.lower() not in random_word and guess1.upper() not in random_word:
        guess -= 1
    print("".join(random_word))
if "_" not in random_word:
    win = True
print("Well done winner you have guessed the word.")
