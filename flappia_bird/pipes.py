from random import randint
from flappia_bird.window import WindowObject


PIPE_STEP = 275
PIPE_AMPLITUDE = 150
PIPE_OPENNESS = 100
DOWN_DIRECTION = 0
UP_DIRECTION = 1
MINIMAL_PIPE_SIZE = 35
INITIAL_X_PIPE = PIPE_STEP + 200


class Pipe(WindowObject):
    def __init__(self, sprite, x_pos, y_pos, direction):
        super(Pipe, self).__init__(sprite, x_pos, y_pos)
        self.amplitude = PIPE_AMPLITUDE
        self.direction = direction


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
