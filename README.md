# Hangman


## Table of contents
- Description
- Installation instructions
- Usage instructions
- File structure
- License information


## Description
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 


## Installation instructions
1. Clone or download this repository to your local machine.

2. Open a terminal and navigate to the directory where the code is located.

3. Run the Python script using the following command: python milestone_5.py


## Usage instructions
1. The program will ask you to enter a single letter.

2. Follow the instructions in the terminal as you guess different letters.

3. Continue entering letters until you guess all the letters in the random word, run out of lives or decide to quit.


## File structure
- `milestone_5.py`: Contains the main Python code for the game.
- 'Hangman()': Class which includes all the attributes and methods for the game
- `ask_for_input()`: Method to take user input and validate it.
- `check_guess(guess)`: Method to check if the entered letter is in the random word.
- 'play_game(word_list)': Function to run the logic of the game. Ends the game if a player runs out of lives and therefore loses, or guesses all the correct letters and wins.


## License information
This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details.


