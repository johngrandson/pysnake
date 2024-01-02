import curses

from classes.drawer import Drawer
from classes.fruit import Fruit
from classes.snake import Snake


class GameState:
    def __init__(self, window):
        self.snake = Snake()
        self.fruit = Fruit()
        self.window = window
        self.score = 0

    @property
    def is_game_over(self):
        return self.snake.hit_border(self.window) or self.snake.hit_itself()


class Game:
    INITIAL_TIMEOUT = 1000
    TIMEOUT_DECREMENT = 50

    def __init__(self, window):
        self.window = window
        self.state = GameState(window)
        self.drawer = Drawer(window)
        self.timeout = self.INITIAL_TIMEOUT

    def game_loop(self):
        while True:
            self.drawer.draw_screen(self.state.score)
            self.state.snake.draw(self.window)
            self.state.fruit.draw_actor(self.state.fruit.position, self.window, curses.ACS_DIAMOND)

            direction = self.get_new_direction(self.timeout)
            
            if direction is None or self.state.snake.direction_is_opposite(direction=direction):
                direction = self.state.snake.current_direction

            self.state.snake.move(direction=direction, fruit_eaten=self.state.snake.fruit_eaten)
            
            if self.state.is_game_over:
                return self.drawer.draw_game_over(self.state.score)
            
            if self.state.snake.hit_fruit(fruit=self.state.fruit.position):
                self.state.snake.fruit_eaten = True
                self.state.fruit.position = self.state.fruit.get_fruit(self.window)
                self.state.score += 1
                if self.timeout > self.TIMEOUT_DECREMENT:
                    self.timeout -= self.TIMEOUT_DECREMENT
            else:
                self.state.snake.fruit_eaten = False
            
            self.state.snake.current_direction = direction

    def get_new_direction(self, timeout):
        self.window.timeout(timeout)
        direction = self.window.getch()
        if direction in [curses.KEY_UP, curses.KEY_LEFT, curses.KEY_DOWN, curses.KEY_RIGHT]:
            return direction
        return None