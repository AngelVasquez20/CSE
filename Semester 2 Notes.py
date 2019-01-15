import string
age = input("How old are you")
print("%s?? Really???" % age)

colors = ["Red", "Blue", "Black", "Yellow", "orange"]
colors.append("cyan")
colors.pop(0)
print(colors)
print(colors[1])
print(len(colors))

print(string.ascii_letters)
print(string.digits)
print(string.punctuation)

# hangman
output = word
word = word
word_letters = ['w', 'o', 'r', 'd']
