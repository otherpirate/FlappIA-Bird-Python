import pygame
from pygame.locals import QUIT, KEYUP, K_ESCAPE
from sprites import SpriteInitializer, Window

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
WINDOW_SIZE = [WINDOW_WIDTH, WINDOW_HEIGHT]

GAME_MODE_EVOLUTION = 0
GAME_MODE_TEST = 0
GAME_MODE_CHALLENGE = 0
GAME_MODE = GAME_MODE_EVOLUTION

POPULATION_SIZE = 0

QUANTITY_CLOUD = 3
QUANTITY_BUILD = 3
QUANTITY_TREE = 3
QUANTITY_FLOOR = 10


def initial_config():
    pygame.init()
    pygame.display.set_caption('Flappy Bird - Python')
    screen = pygame.display.set_mode(WINDOW_SIZE)

    sprites = SpriteInitializer()
    window = Window(screen)
    window.prepare(sprites.floor, QUANTITY_FLOOR, WINDOW_HEIGHT - sprites.floor.height)
    window.prepare(sprites.cloud, QUANTITY_CLOUD, WINDOW_HEIGHT - 275)
    window.prepare(sprites.build, QUANTITY_BUILD, WINDOW_HEIGHT - 175)
    window.prepare(sprites.tree, QUANTITY_TREE, WINDOW_HEIGHT - 125)
    # window.prepare(sprites.graph, QUANTITY_FLOOR, 0)  # TODO Graph not ready

    return window


def main():
    clock = pygame.time.Clock()
    window = initial_config()

    finish = False
    while True:
        for e in pygame.event.get():
            if e.type == QUIT or (e.type == KEYUP and e.key == K_ESCAPE):
                finish = True
                break
        if finish:
            break

        window.draw()
        clock.tick(50)


if __name__ == '__main__':
    main()
