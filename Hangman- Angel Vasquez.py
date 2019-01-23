import random
guess = 8
words = ["Apple", "Word", "Backpack", "Pencil", "Legs", "Mouse", "Dog", "Cat", "Myth", "Shoe", "I love dogs!"]
random = random.choice(words)
display = []

for i in range(len(display)):
    display[i] = "_"

print(' '.join(display))
print()

string1 = words
list1 = list(string1)
print(list1)
for i in range(len(words)):
    if list1 ==