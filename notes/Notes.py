print(3 != 4)
"""
a = 3  # A is set to 3
a == 3 # Is a equal to 3?
"""

# Creating a list
fruit = ['apple', 'oranges', 'blackberries', 'strawberries',
         'blueberries', "raspberries", "pineapple", "mango", "coconut"]
print(fruit)

# Pulling items from a list
print(fruit[1])

# Getting the length of a list
print(len(fruit))
print("The length of the list is %d" % len(fruit))

# Modifying Lists
fruit[8] = 'Banana'
print(fruit)


# Looping through Lists
for item in fruit:
    print(item)

icecreamflavors = ["vanilla", "strawberry", "mango", "pineapple"]
print(icecreamflavors)

icecreamflavors[2] = "mango"
print("The last thing in the lists is %s" % icecreamflavors[len(icecreamflavors) - 1])

food_lists = ["pizza", "tamales", "tacos", "pie", "enchiladas", "burrito",
              "sushi", "poke", "flan", "poutine", "noodles", "chicken", "chili", "Hot wings", "salmons", "chip",
              "lasagna", "soup", "fettuccine", "salad", "carne"]

# Slicing
print(food_lists[2:5])
print(food_lists[3:4])
print(food_lists[10:])
print(food_lists[:5])

# Adding stuff to a list (part1)
food_lists.append("oranges")
food_lists.append("bacon")
print(food_lists)
# Everything is in the form from object.method(parameters)

# Adding to a lists (not at the end)
food_lists.insert(2, "Ramen")
print(food_lists)

# Removing from a list
food_lists.remove("tacos")
food_lists.remove("pie")
print(food_lists)
# This removes the specific item from the lists

# Removing from a lists (part2)
# Sometimes, you don't know what is in the lists, but you know
# you want to get rid of something at a specific index
food_lists.pop(0)
print(food_lists)
# Notice that " is no longer in the last because was is an index 0.

new_lists = ["pineapple", "pizza", "tacos"]

food_lists.insert(3, "soup")
print(food_lists)
new_lists.remove("pizza")
print(food_lists)


# Finding things in a lists
print(food_lists.index("chicken"))
# This printed 9 for me, so chicken must be at index 9.
# This is an easy way of finding things in a lists

# Things I notice people do:
# Some people have made lists which parentheses instead of brackets
brands = ("apple", "samsung", "HTC")
# This is a TUPLE, not a lists. Tuples are immutable (cannot be changed)

# CHANGING THINGS INTO A NEW LISTS
string1 = "turquoise"
list1 = list(string1)
print(list1)

# HangMan hints
for i in range(len(list1)):   # The number i goes through all indices
    if list1[i] == "u":  # if we find "u"
        list1.pop(i)  # Remove the i-th index
        list1.insert(i, "_")  # put a * there instead

# CHANGING BACK INTO A STARING (LIST→STRING)
print("".join(list1))


# Function Notes
# a**2 + b**2 = c**2
def pythagorean(a, b):
    return (a**2 + b**2) ** (1/2)


print(pythagorean(3, 4))
