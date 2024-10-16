# Scrabble Score Calculator

This project is a simple Scrabble score calculator written in C. It allows two players to input words and calculates the Scrabble score for each word based on the standard Scrabble letter values. The program then determines the winner or if the game is a tie.

## How It Works

1. **Input**: The program prompts each player to enter a word.
2. **Conversion**: Each letter in the word is converted to uppercase.
3. **Scoring**: The program calculates the score for each word by summing the values of its letters.
4. **Comparison**: The scores of the two players are compared to determine the winner.

## Letter Values

The letter values used in this program are based on the standard Scrabble game:

- A, E, I, L, N, O, R, S, T, U: 1 point
- D, G: 2 points
- B, C, M, P: 3 points
- F, H, V, W, Y: 4 points
- K: 5 points
- J, X: 8 points
- Q, Z: 10 points

## Example

```plaintext
Player 1: "HELLO"
Player 2: "WORLD"

Player 1 score: 8
Player 2 score: 9

Output: Player 2 wins!
```

## How to Run

1. Ensure you have the CS50 library installed.
2. Compile the program using a C compiler, for example:

    ```sh
    gcc -o scrabble scrabble.c -lcs50
    ```

3. Run the executable:

    ```sh
    ./scrabble
    ```

## Dependencies

- CS50 Library
- Standard C Libraries: `ctype.h`, `stdio.h`, `string.h`

## License

This project is licensed under the MIT License.

## Acknowledgements

This project is part of the CS50x course offered by Harvard University.
