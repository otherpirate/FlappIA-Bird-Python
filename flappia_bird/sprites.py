from collections import OrderedDict
import pygame

QUANTITY_COLOR_BIRDS = 6
QUANTITY_SPRITES_BIRDS = 3

FONT_BLACK = (0, 0, 0)
FONT_RED = (255, 0, 0)
FONT_BLUE = (0, 0, 255)


class Sprite(object):

    LOADED_IMAGES = OrderedDict()

    def __init__(self, width, height, name):
        self.width = width
        self.height = height
        self.name = name
        if self.name not in self.LOADED_IMAGES:
            self.LOADED_IMAGES[self.name] = pygame.image.load('./images/{}'.format(self.name))

    @property
    def drawer(self):
        return self.LOADED_IMAGES[self.name]


class Text(object):
    def __init__(self, message, color, size):
        font = pygame.font.Font('freesansbold.ttf', size)
        self.text = font.render(message, True, color)

    @property
    def drawer(self):
        return self.text


class SpriteInitializer(object):

    def __init__(self):
        self.cloud = Sprite(959, 114, 'nuvens.png')
        self.build = Sprite(959, 54, 'predios2.png')
        self.tree = Sprite(959, 52, 'arvores.png')
        self.floor = Sprite(209, 75, 'chao.png')
        self.pipe = Sprite(86, 836, 'cano.bmp')
        self.parachute = Sprite(50, 50, 'paraquedas.png')

        widths = [54, 55, 58]
        heights = [46, 46, 46]
        self.birds = []
        for i in range(QUANTITY_COLOR_BIRDS):
            for j in range(QUANTITY_SPRITES_BIRDS):
                bird = Sprite(widths[j], heights[j], 'flap{}{}.png'.format(j+1, i))
                self.birds.append(bird)

        self.neuron_inactive = Sprite(50, 50, 'neuronio7.png')  # TODO Sizes?
        self.neuron_active = Sprite(50, 50, 'neuronio7.png')  # TODO Sizes?
        self.light = Sprite(50, 50, 'luz.png')  # TODO Sizes?
        self.arrow = Sprite(50, 50, 'seta2.png')  # TODO Sizes?0;