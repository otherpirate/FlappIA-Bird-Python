from random import randint
from flappia_bird.window import WindowObject


PIPE_STEP = 275
INITIAL_X_PIPE = PIPE_STEP + 200
PIPE_OPENNESS = 100
DOWN_DIRECTION = 0
UP_DIRECTION = 1
MINIMAL_PIPE_SIZE = 35
VERTICAL_SPEED = 10
MAX_AMPLITUDE = MINIMAL_PIPE_SIZE * 2


class Pipe(WindowObject):
    def __init__(self, sprite, x_pos, y_pos, direction):
        super(Pipe, self).__init__(sprite, x_pos, y_pos)
        self.amplitude = 0
        self.direction = direction

    def going_up(self):
        return self.direction == UP_DIRECTION

    def vertical_movement(self):
        if self.amplitude + VERTICAL_SPEED >= MAX_AMPLITUDE:
            if self.going_up():
                self.direction = DOWN_DIRECTION
            else:
                self.direction = UP_DIRECTION
            self.amplitude *= -1

        if self.going_up():
            self.y_pos -= VERTICAL_SPEED
        else:
            self.y_pos += VERTICAL_SPEED
        self.amplitude += VERTICAL_SPEED


def build_pipes(quantity, sprite_pipe_upper, sprite_pipe_lower, base_height, max_height):
    current_x = INITIAL_X_PIPE
    pipes = []
    max_y = max_height - base_height - MINIMAL_PIPE_SIZE - PIPE_OPENNESS
    for i in range(quantity):
        y = randint(MINIMAL_PIPE_SIZE, max_y)
        direction = randint(DOWN_DIRECTION, UP_DIRECTION)
        upper_pipe = Pipe(sprite_pipe_upper, current_x, y - sprite_pipe_upper.height, direction)
        lower_pipe = Pipe(sprite_pipe_lower, current_x, y + PIPE_OPENNESS, direction)
        pipes.append(upper_pipe)
        pipes.append(lower_pipe)
        current_x += PIPE_STEP

    return pipes
