import random
guess = 8
Words = ["Apple", "Word", "Backpack", "Pencil", "Legs", "Mouse", "Dog", "Cat", "Myth", "Shoe", "I love dogs!"]
random = random.choice(Words)
display = []
# Apple
string1 = "Apple"
list1 = list(string1)
for i in range(len(list1)):
    if list1[i] == "Apple":
        list1.pop(i)
        list1.insert(i, "_")
# Word
string2 = "Word"
list2 = list(string2)
for i in range(len(list2)):
    if list2[i] == "Word":
        list2.pop(i)
        list2.insert(i, "_")
# Backpack
string3 = "Backpack"
list3 = list(string3)
for i in range(len(list3)):
    if list3[i] == "Backpack":
        list3.pop(i)
        list3.insert(i, "_")
# Pencil
string4 = "Pencil"
list4 = list(string4)
for i in range(len(list4)):
    if list4[i] == "Pencil":
        list4.pop(i)
        list4.insert(i, "_")
# Leg
string5 = "Leg"
list5 = list(string5)
for i in range(len(list5)):
    if list5[i] == "Leg":
        list5.pop(i)
        list5.insert(i, "_")
# Dog
string6 = "Dog"
list6 = list(string6)
for i in range(len(list6)):
    if list6[i] == "Dog":
        list6.pop(i)
        list6.insert(i, "_")
# Cat
string7 = "Cat"
list7 = list(string7)
for i in range(len(list7)):
    if list7[i] == "Cat":
        list1.pop(i)
        list1.insert(i, "_")
# Myth
string8 = "Myth"
list8 = list(string8)
for i in range(len(list8)):
    if list8[i] == "Myth":
        list8.pop(i)
        list8.insert(i, "_")
# Shoe
string9 = "Shoe"
list9 = list(string9)
for i in range(len(list9)):
    if list9[i] == "Shoe":
        list9.pop(i)
        list9.insert(i, "_")
# Love dogs
string10 = "I love dogs!"
list10 = list(string10)
for i in range(len(list10)):
    if list10[i] == "I love dogs!":
        list10.pop(i)
        list10.insert(i, "_")
        print(' '.join(display))
        print()

while guess == len(random):
    guess = input("Guess a letter: ")
    guess = guess.lower()
    print(guess)

for i in range(len(random)):
    if random[i] == guess:
        display[i] = guess
        guess = guess - 1
