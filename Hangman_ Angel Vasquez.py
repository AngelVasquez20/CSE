import random
Words = ["Apple", "Word", "Backpack", "Pencil", "Legs", "Mouse", "Dog", "Cat", "Myth", "Shoe", "I love dogs!"]
random = random.choice(Words)
display = []

string = Words
list1 = list(string)
for i in range(len(Words)):
    if list1[i] == "Apple":
        list1.pop(i)
        list1.insert(i, "_")

