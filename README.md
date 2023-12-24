# Red-Blue Nim with Alpha-Beta Pruning

This is a simple implementation of the Red-Blue Nim game using Alpha-Beta Pruning for decision-making. The game can be played in standard or misere mode, and the first player can be either a human or a computer. 

## Usage

To run the game, execute the following command:

```bash
python red_blue_nim.py <num-red> <num-blue> <version> <first-player> <depth>
```

- `<num-red>`: Number of red marbles in the initial pile.
- `<num-blue>`: Number of blue marbles in the initial pile.
- `<version>`: Game version, choose between "standard" or "misere".
- `<first-player>`: First player, choose between "computer" or "human".
- `<depth>`: Depth limit for the Alpha-Beta Pruning algorithm. (Optional)

Example:

```bash
python red_blue_nim.py 5 7 standard computer
```

## Rules

The Red-Blue Nim game is a two-player game where players take turns removing marbles from either the red or blue pile. The game continues until one of the piles is empty.

- In standard mode, the player who removes the last marble wins.
- In misere mode, the player who removes the last marble loses.

## Alpha-Beta Pruning

The implementation uses Alpha-Beta Pruning to efficiently find the best move for the computer player.

## Author

- Aravindh Gopalsamy
- gopal98aravindh@gmail.com

## License

This project is not open for external use or distribution. All rights reserved.

## Important Note for Students

**Warning:** This code is intended for educational purposes only. Please do not use this code for any assignment, and consider it as a reference implementation. Use your own implementation for academic assignments.
