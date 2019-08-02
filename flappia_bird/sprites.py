from collections import OrderedDict
import pygame

QUANTITY_COLOR_BIRDS = 6
QUANTITY_SPRITES_BIRDS = 3


class Sprite(object):

    LOADED_IMAGES = OrderedDict()

    def __init__(self, width, height, image):
        self.width = width
        self.height = height
        self.image = image
        if self.image not in self.LOADED_IMAGES:
            self.LOADED_IMAGES[self.image] = pygame.image.load('./images/{}'.format(image))

    @property
    def drawer(self):
        return self.LOADED_IMAGES[self.image]


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