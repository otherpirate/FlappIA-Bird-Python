import pygame
from pygame.locals import QUIT, KEYUP, K_ESCAPE
from flappia_bird.game import Game
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

SPEED = 10.0


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

    pipes = build_pipes(QUANTITY_PIPES, sprites.upper_pipe, sprites.lower_pipe, sprites.floor.height, WINDOW_HEIGHT)
    for pipe in pipes:
        window.add(pipe)

    window.prepare(sprites.floor, QUANTITY_FLOOR, WINDOW_HEIGHT - sprites.floor.height)

    birds = build_birds(population_size, sprites.birds, 50, WINDOW_HEIGHT - 200)
    for bird in birds:
        window.add(bird)

    if GAME_MODE == GAME_MODE_CHALLENGE:
        # load_network()  # TODO too far
        pass

    return Game(window, sprites, birds, pipes, SPEED)


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
        game.bird_movement()
        game.apply_gravity()
        game.check_collisions()
        game.bird_choose()

        clock.tick(50)


if __name__ == '__main__':
    main()
