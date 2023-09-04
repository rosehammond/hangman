import random

class Hangman:

    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.list_of_guesses = []
        self.word = random.choice(word_list)
        self.word_guessed = ["_" for _ in self.word]
        self.num_letters = len(set(self.word))

    def ask_for_input(self):
        """
        Takes in a letter as an input. 
        Checks if the input is valid i.e. it is a single letter from the alphabet.
        """
        while True:
            self.guess = input("Enter a single letter: ")

            if len(self.guess) != 1 or not self.guess.isalpha():
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif self.guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.check_guess(self.guess)
                self.list_of_guesses.append(self.guess)

        self.check_guess(guess)

    def check_guess(self, guess):
        """
        Converts user guess to lower case. 
        Checks if the input is in the randomly selected word.
        """
        lowercase_guess = guess.lower()

        if lowercase_guess in self.word:
            print(f"Good guess! {guess} is in the word.")

            for index, letter in enumerate(self.word):
                if lowercase_guess == letter:
                    self.word_guessed[index] = lowercase_guess
            self.num_letters -= 1
            
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left.")

hangman_game = Hangman(["pineapple", "grapes", "mango", "strawberry", "kiwi"])
hangman_game.ask_for_input()


