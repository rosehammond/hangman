# Hangman
[CHECK AND EDIT ALL SECTIONS]
## Table of contents
- Description
- Installation instructions
- Usage instructions
- File structure
- License information


## Description
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

[MAYBE USE THIS]It selects a random word from a list of favorite fruits and asks the user to guess a letter. The user continues guessing until they correctly guess all the letters in the random word or until they give up.

[IS THIS OVER DETAILED??] The game stores a list of words, which the computer will choose from, at random. The user is then asked to input a letter and the game checks that this is a single letter from the alphabet, if it is not, the user is asked to input another letter. The code converts the letter to lowercase, if necessary, then checks if it is in the word, returning relevant statements if it is/isn't. 

## Installation instructions
1. Clone or download this repository to your local machine.

2. Open a terminal and navigate to the directory where the code is located.

3. Run the Python script using the following command: python milestone_5.py


## Usage instructions
1. The program will display a list of favorite fruits and select a random word from the list.

2. You will be prompted to enter a single letter.

3. Continue entering letters until you guess all the letters in the random word or decide to quit.

## File structure
- `milestone_5.py`: Contains the main Python code for the game.
- `favourite_fruits`: A list of favorite fruits from which a random word is selected.
- `ask_for_input()`: Function to take user input and validate it.
- `check_guess(guess)`: Function to check if the entered letter is in the random word.


## License information
[READ THE FOLLOWING WEBSITE https://choosealicense.com/licenses/mit/ FIRST]
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

!!DELETE THIS BEFORE THE END: At minimum, your README file should contain the following information:
Project Title - done
Table of Contents, if the README file is long
A description of the project: what it does, the aim of the project, and what you learned
Installation instructions
Usage instructions
File structure of the project
License information!!
