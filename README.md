# Python Snake Game

This is a simple implementation of the classic Snake game in Python using the `curses` library.

## Classes

The game consists of three main classes:

- `Snake`: This class represents the snake in the game. It keeps track of the snake's body, its current direction, and whether it has eaten a fruit.

- `Fruit`: This class represents the fruit in the game. It keeps track of the fruit's position.

- `Game`: This class manages the game loop and user input. It uses the `Snake` and `Fruit` classes to update the game state and draw the game screen.

## How to Run

You can run the game using Python 3. Make sure you have the `curses` library installed, which is included in the Python standard library.

```
python snake_game.py
```

## Game Rules

- The snake moves in the direction of the arrow key pressed by the user.
- The snake cannot move in the opposite direction of its current direction.
- The game ends when the snake hits the border or itself.
- The snake grows longer each time it eats a fruit.
- The score is the number of fruits eaten by the snake.
