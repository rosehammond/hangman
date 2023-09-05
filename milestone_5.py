import random

class Hangman:
    """
    This class is lets a user play hangman against the computer.
    
    Attributes:
        word list (list): a list of words for the program to choose from.
        num_lives (int): the number of lives a player has left, defualts to 5.
        list_of_guesses (list): a list of letters the player has guessed.
        word (str): a word chosen randomly by the program from the list of words.
        word_guessed (list): a representation of the word beign guessed. _ signify the letters of the word.
        num_letters (int): the number of letters left to guess in the word.
        """
    def __init__(self, word_list, num_lives):
        """
        See help(Hangman) for accurate signature.
        """
        self.word_list = word_list
        self.num_lives = num_lives
        self.list_of_guesses = []
        self.word = random.choice(word_list)
        self.word_guessed = ["_" for _ in self.word]
        self.num_letters = len(set(self.word))

    def ask_for_input(self):
        """
        This function takes in a letter as an input. 

        The purpose of this functions is to take in a letter and check if the input is valid 
        i.e. it is a single letter from the alphabet.
        It then returns a string to let the user know if this is an invalid input, or if they have already tried the letter.
        If it is valid and unique, it adds the input to a list of guesses and passes the letter through the check_guess function.
        """
        
        guess = input("Enter a single letter: ")

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid letter. Please, enter a single alphabetical character.")
        elif guess in self.list_of_guesses:
            print("You already tried that letter!")
        else:
            self.check_guess(guess)
            self.list_of_guesses.append(guess)


    def check_guess(self, guess):
        """
        This function checks if the guessed letter is in the word.

        Args:
            guess (str): the letter which the user inputs.

        The purpose of this functions is to convert the guess to lower case. 
        It then checks if the input is in the randomly selected word.
        If it is in the word, it returns a string, replaces the _ in word_guessed and reduces num_letters by 1.
        If it is not in the word it reduces num_lives by 1 and returns a string.
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


def play_game(word_list):
    """
    This function codes the logic for the game, allowing it to end.

        Args:
            word_list (list): a list of words the computer choses from at random.

        The purpose of this functions is to ensure the game ends either when the player loses as they run out of lives,
        or the player wins by guessing all the letters correctly.
    """
    num_lives = 5
    game = Hangman(word_list, num_lives)

    while True:
      if game.num_lives == 0:
          print(f"You lost! The word was {game.word}")
          break
      elif game.num_letters > 0:
          game.ask_for_input()   
      elif game.num_lives != 0 and game.num_letters < 1:
          print(f"Congratulations. The word was {game.word}. You won the game!")
          break

# Call the function to play the game, insert any list of words to play with.
play_game(["pineapple", "grapes", "mango", "strawberry", "kiwi"])
