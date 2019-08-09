from flappia_bird.rna import RNA
from flappia_bird.window import WindowObject

STATE_ALIVE = 0
STATE_JUMPING = 1
STATE_PARACHUTE = 2
STATE_DEAD = 3
BIRD_BRAIN_LAYERS = 1
BIRD_BRAIN_INPUT = 4
BIRD_BRAIN_HIDE = 6
BIRD_BRAIN_OUTPUT = 2


class Bird(WindowObject):
    def __init__(self, sprite, x_pos, y_pos):
        super(Bird, self).__init__(sprite, x_pos, y_pos)
        self.speed = 0
        self.angle = 0
        self.state = STATE_ALIVE
        self.fitness = 0.0
        self.brain = RNA(BIRD_BRAIN_LAYERS, BIRD_BRAIN_INPUT, BIRD_BRAIN_HIDE, BIRD_BRAIN_OUTPUT)
        self.dna = []
        self.vertical_speed = 0.0

    @property
    def using_parachute(self):
        return self.state == STATE_PARACHUTE

    @property
    def is_dead(self):
        return self.state == STATE_DEAD

    def kill(self):
        self.state = STATE_DEAD

    def jump(self):
        self.vertical_speed = -3.5
        self.state = STATE_JUMPING


def build_birds(quantity, bird_sprites, x_pos, y_pos):
    birds = []
    for i in range(quantity):
        bird_sprite = bird_sprites.pop(0)
        bird_sprites.append(bird_sprite)
        bird = Bird(bird_sprite, x_pos, y_pos)
        birds.append(bird)

    return birds
