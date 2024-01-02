import curses


class Snake:
    def __init__(self):
        self.snake = [[13, 15], [12, 15], [11, 15], [10, 15]]
        self.current_direction = curses.KEY_DOWN
        self.fruit_eaten = False

    def move(self, direction, fruit_eaten):
        head = self.snake[0].copy()
        self.snake.insert(0, head)
        self.move_actor(head, direction)

        if not fruit_eaten:
            self.snake.pop()

    def move_actor(self, actor, direction):
        match direction:
            case curses.KEY_UP:
                actor[0] -= 1
            case curses.KEY_LEFT:
                actor[1] -= 1
            case curses.KEY_DOWN:
                actor[0] += 1
            case curses.KEY_RIGHT:
                actor[1] += 1

    def direction_is_opposite(self, direction):
        match direction:
            case curses.KEY_UP:
                return self.current_direction == curses.KEY_DOWN
            case curses.KEY_LEFT:
                return self.current_direction == curses.KEY_RIGHT
            case curses.KEY_DOWN:
                return self.current_direction == curses.KEY_UP
            case curses.KEY_RIGHT:
                return self.current_direction == curses.KEY_LEFT

    def hit_border(self, window):
        head = self.snake[0]
        return self.actor_hit_border(head, window)
    
    def hit_fruit(self, fruit):
        return fruit in self.snake
    
    def hit_itself(self):
        head = self.snake[0]
        return head in self.snake[1:]

    def actor_hit_border(self, actor, window):
        height, width = window.getmaxyx()
        if (actor[0] <= 0) or (actor[0] >= (height - 1)):
            return True
        if (actor[1] <= 0) or (actor[1] >= (width - 1)):
            return True
        return False

    def draw(self, window):
        head = self.snake[0]
        body = self.snake[1:]
        self.draw_actor(head, window, "@")
        for body_part in body:
            self.draw_actor(body_part, window, "s")

    def draw_actor(self, actor, window, char):
        window.addch(actor[0], actor[1], char)
