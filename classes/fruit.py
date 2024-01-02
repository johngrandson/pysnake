import random


class Fruit:
    def __init__(self):
        self.position = [10, 20]

    def draw_actor(self, actor, window, char):
        window.addch(actor[0], actor[1], char)
    
    def get_fruit(self, window):
        height, width = window.getmaxyx()
        return [random.randint(1, height - 2), random.randint(1, width - 2)]

