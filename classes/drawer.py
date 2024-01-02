import time


class Drawer:
    def __init__(self, window):
        self.window = window

    def draw_screen(self, score):
        self.window.addch(3, 3, score)
        self.window.clear()
        self.window.border(0)

    def draw_game_over(self, score):
        height, width = self.window.getmaxyx()
        message = f"Game over! Fruits collected: {score}"
        y = int(height / 2)
        x = int((width - len(message)) / 2)
        self.window.addstr(y, x, message)
        self.window.refresh()
        time.sleep(10)