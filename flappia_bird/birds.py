from flappia_bird.rna import RNA
from flappia_bird.window import WindowObject

STATE_ALIVE = 1
STATE_DEAD = 2
BIRD_BRAIN_LAYERS = 1
BIRD_BRAIN_INPUT = 2
BIRD_BRAIN_HIDE = 2
BIRD_BRAIN_OUTPUT = 1


class Bird(WindowObject):
    def __init__(self, sprite):
        super(Bird, self).__init__(sprite, 0, 0)
        self.speed = 0
        self.angle = 0
        self.state = STATE_ALIVE
        self.fitness = 0.0
        self.brain = RNA(BIRD_BRAIN_LAYERS, BIRD_BRAIN_INPUT, BIRD_BRAIN_HIDE, BIRD_BRAIN_OUTPUT)
        self.dna = []


def build_birds(quantity, bird_sprites):
    birds = []
    for i in range(quantity):
        bird_sprite = bird_sprites.pop(0)
        bird_sprites.append(bird_sprite)
        bird = Bird(bird_sprite)
        birds.append(bird)

    return birds
