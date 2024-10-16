# Runoff Voting System

This project implements a runoff voting system in C. The program simulates an election where voters rank candidates in order of preference. If no candidate wins a majority, the candidate with the fewest votes is eliminated, and votes are redistributed to the next preferred candidate. This process continues until a candidate wins a majority.

## Files

- `runoff.c`: The main program file containing the implementation of the runoff voting system.

## How It Works

1. **Initialization**: The program initializes the list of candidates and the number of voters.
2. **Voting**: Voters rank the candidates in order of preference.
3. **Tabulation**: Votes are counted for non-eliminated candidates based on voter preferences.
4. **Winner Check**: The program checks if any candidate has more than half of the total votes.
5. **Elimination**: If no candidate has a majority, the candidate with the fewest votes is eliminated.
6. **Repeat**: Steps 3-5 are repeated until a winner is found or a tie is detected.

## Functions

- `bool vote(int voter, int rank, string name)`: Records a voter's preference if the vote is valid.
- `void tabulate(void)`: Counts votes for non-eliminated candidates.
- `bool print_winner(void)`: Prints the winner of the election if there is one.
- `int find_min(void)`: Finds the minimum number of votes any remaining candidate has.
- `bool is_tie(int min)`: Checks if the election is tied between all remaining candidates.
- `void eliminate(int min)`: Eliminates the candidate(s) with the fewest votes.

## Usage

To run the program, compile it using a C compiler and execute it with the names of the candidates as command-line arguments:

```sh
gcc -o runoff runoff.c -lcs50
./runoff Alice Bob Charlie
```

The program will then prompt for the number of voters and their ranked preferences for the candidates.

## Example

```sh
./runoff Alice Bob Charlie
Number of voters: 3
Rank 1: Alice
Rank 2: Charlie
Rank 3: Bob

Rank 1: Bob
Rank 2: Charlie
Rank 3: Alice

Rank 1: Charlie
Rank 2: Alice
Rank 3: Bob
```

The program will then process the votes and determine the winner based on the runoff voting system.

## License

This project is licensed under the MIT License.

## Acknowledgments

This project is part of the CS50 course by Harvard University.
