# Guessing game

## Game description:

This program is a simple guessing game for two players. Each player tries to guess a randomly generated number within a specified range entered by the player.The player whose guess is closer to the actual number wins the game. If both players are equally close to the number, it results in a tie. After the game ends, the program reveals the actual number.


## Pseudocode

1. **Initialize the game:**

   - Ask the user to enter the range for guessing 

   - Get the names of Player 1 and Player 2.

   - Call the start function with the specified range.


2. **Start Function:**
   - Accept the parameter n-(the range for guessing).
   - Create an empty list "numlist".
   - Append numlist with numbers from 0 to n-1.
   - Generate a random number between the range 0 to n-1.
   - Ask Player 1 and Player 2 to input their guesses.
   - Calculate the distance between each player's guess and the random number.
   - Determine the winner or if it's a tie based on the nearest guess of each player's guess to the random number.
   - Print the winner or a tie message along with the actual number.
