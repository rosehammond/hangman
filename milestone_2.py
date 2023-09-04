import random

favourite_fruits = ["pineapple", "grapes", "mango", "strawberry", "kiwi"]

word_list = favourite_fruits

print(word_list)

random_word = random.choice(word_list)

print(random_word)

while True:
    guess = input("Enter a single letter: ")

    if len(guess) == 1 and guess.isalpha():
        print("Good guess!")
        break
    else:
        print("Oops! That is not a valid input.")
        break
