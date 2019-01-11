word = ["Apple", "Words", "Backpack", "Pencil", "Legs", "Pants", "Dog", "Cat", "Guitar", "Shoe"]
print(word)


string1 = "turquoise"
list1 = list(string1)
print(list1)
for i in range(len(list1)):
    if list1[i] == "u":
        list1.pop(i)
        list1.insert(i, "*")