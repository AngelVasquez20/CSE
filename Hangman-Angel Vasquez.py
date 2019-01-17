import random

words = ["Guitar", "Apple", "Legs", "People", "Myth", "Backpack", "Dogs", "Cats", "Mouse", "I love my mother!"]
word = random.choice(words)
answer = []

while True:
    print("Your word has", len(word), "Letters in it")
    print(answer)
    guess = guess.lower(