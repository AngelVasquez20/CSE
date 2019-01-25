import random
words = ["Apple", "Word", "Backpack", "Pencil", "Legs", "Mouse", "Dog", "Cat", "Myth", "Shoe", "I love dogs!"]
random = random.choice(words)
display = []

for i in range(len(words)):
    words[i] = "_"
print(' '.join(words))
print()
