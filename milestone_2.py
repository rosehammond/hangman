import random

favourite_fruits = ["pineapple", "grapes", "mango", "strawberry", "kiwi"]

word_list = favourite_fruits

print(word_list)

word = random.choice(word_list)

print(word)

guess = input("Choose a letter: ")

if len(guess) == 1 and guess.isalpha():
    print("Good guess")
else:
    print("Oops! That is not a valid input.")
    