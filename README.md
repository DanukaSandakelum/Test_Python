# Random Number Guessing Game

A simple Python game where the player tries to guess a randomly generated number within a specified range.

## How It Works

1. The game uses the current system time in microseconds to generate a "random" number within your specified range
2. You input:
   - A minimum value for the range
   - A maximum value for the range
   - Your guess for what the number will be
3. The game tells you if you guessed correctly or shows you the generated number
4. If you didn't guess correctly, you can keep trying until you get it right

## How to Run

1. Make sure you have Python installed
2. Save the code as `guessing_game.py`
3. Run the program with: `python guessing_game.py`
4. Follow the on-screen prompts to play the game

## Example Gameplay

## Notes

- The randomness is based on the exact microsecond when the function runs
- The game will continue until you guess the correct number
- Each guess generates a new "random" number based on the current time

Enjoy the game!
