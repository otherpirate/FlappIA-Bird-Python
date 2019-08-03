import pygame
from pygame.locals import QUIT, KEYUP, K_ESCAPE
from flappia_bird.birds import build_birds
from flappia_bird.pipes import build_pipes
from flappia_bird.sprites import SpriteInitializer
from flappia_bird.window import Window


WINDOW_WIDTH = 730
WINDOW_HEIGHT = WINDOW_WIDTH-290
WINDOW_SIZE = [WINDOW_WIDTH, WINDOW_HEIGHT]

GAME_MODE_EVOLUTION = 0
GAME_MODE_TEST = 1
GAME_MODE_CHALLENGE = 2
GAME_MODE = GAME_MODE_EVOLUTION

QUANTITY_CLOUD = 3
QUANTITY_BUILD = 3
QUANTITY_TREE = 3
QUANTITY_FLOOR = 10
QUANTITY_PIPES = 6

SPEED = 100.0


class Game(object):
    def __init__(self, window, sprites, birds, speed):
        self.window = window
        self.sprites = sprites
        self.birds = birds
        self.record = 0
        self.generation = 0
        self.speed = speed

    def background_movement(self):
        self.movement(self.sprites.cloud.name, 45)
        self.movement(self.sprites.build.name, 15)
        self.movement(self.sprites.tree.name, 5)
        self.movement(self.sprites.floor.name, SPEED)
        self.movement(self.sprites.upper_pipe.name, SPEED)
        self.movement(self.sprites.lower_pipe.name, SPEED)

    def movement(self, name, step):
        for obj in self.window.content.get(name, []):
            obj.x_pos -= self.speed/step
            if obj.x_pos + obj.sprite.width >= 0:
                continue
            obj.x_pos += (len(self.window.content[name]) - 1) * obj.sprite.width


def initial_config():
    pygame.init()
    pygame.display.set_caption('Flappy Bird - Python')
    screen = pygame.display.set_mode(WINDOW_SIZE)

    if GAME_MODE == GAME_MODE_EVOLUTION:
        population_size = 2000
    elif GAME_MODE == GAME_MODE_TEST:
        population_size = 1
    elif GAME_MODE == GAME_MODE_CHALLENGE:
        population_size = 2

    sprites = SpriteInitializer()
    window = Window(screen)
    window.prepare(sprites.cloud, QUANTITY_CLOUD, WINDOW_HEIGHT - 275)
    window.prepare(sprites.build, QUANTITY_BUILD, WINDOW_HEIGHT - 175)
    window.prepare(sprites.tree, QUANTITY_TREE, WINDOW_HEIGHT - 125)

    birds = build_birds(population_size, sprites.birds, 50, WINDOW_HEIGHT - 200)
    for bird in birds:
        window.add(bird)

    pipes = build_pipes(QUANTITY_PIPES, sprites.upper_pipe, sprites.lower_pipe, sprites.floor.height, WINDOW_HEIGHT)
    for pipe in pipes:
        window.add(pipe)

    window.prepare(sprites.floor, QUANTITY_FLOOR, WINDOW_HEIGHT - sprites.floor.height)

    if GAME_MODE == GAME_MODE_CHALLENGE:
        # load_network()  # TODO too far
        pass

    return Game(window, sprites, birds, SPEED)


def main():
    clock = pygame.time.Clock()
    game = initial_config()

    finish = False
    while True:
        for e in pygame.event.get():
            if e.type == QUIT or (e.type == KEYUP and e.key == K_ESCAPE):
                finish = True
                break
        if finish:
            break

        game.window.draw()
        game.background_movement()
        clock.tick(50)


if __name__ == '__main__':
    main()
