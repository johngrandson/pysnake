import curses

from classes.game import Game

if __name__ == '__main__':
    curses.wrapper(lambda window: Game(window).game_loop())