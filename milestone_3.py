import random

favourite_fruits = ["pineapple", "grapes", "mango", "strawberry", "kiwi"]

word_list = favourite_fruits

print(word_list)

random_word = random.choice(word_list)

print(random_word)

def ask_for_input():
    """
    Takes in a letter as an input. 
    Checks if the input is valid i.e. it is a single letter from the alphabet.
    """

    while True:
        guess = input("Enter a single letter: ")

        if len(guess) == 1 and guess.isalpha():
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    
    check_guess(guess)

def check_guess(guess):
    """
    Converts user guess to lower case. 
    Checks if the input is in the randomly selected word.
    """
    lowercase_guess = guess.lower()

    if lowercase_guess in random_word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")

ask_for_input()


