print(3 !=4)
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
print (icecreamflavors)

icecreamflavors[2] = "mango"
print("The last thing in the lists is %s" % icecreamflavors[len(icecreamflavors) - 1])
