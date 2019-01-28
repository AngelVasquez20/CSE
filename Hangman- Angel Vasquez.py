import random
guess = 8
puncuation = string.punctuation
string =
list1 = list(string)
print(list1)
alphabet = list(string.ascii_letters)
words = ["Apple", "Word", "Backpack", "Pencil", "Legs", "Mouse", "Dog", "Cat", "Myth", "Shoe", "I love dogs!"]
random = random.choice(words)
letters_guessed = []

for i in range(len(words)):
    if words[i] in alphabet:
        list1.pop(i)
        list1.insert(i, "_")

print("".join(words))
print()

while guess > 0:
    guess = input("Guess a letter: ")
    print(guess)
    letters_guessed.append(guess.lower())
    for i in range(len(words)):
        if words[i].lower() in letters_guessed:
            list1.pop(i)
            list1.insert(i, words[i])

if guess.lower() not in list1 and guess.upper() not in list1:
    guess -= 1
    print("".join(list1))
if "_" not in list1:
    win = True
    print("Well done winner you have guessed the word.")
