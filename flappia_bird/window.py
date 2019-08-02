import pygame

BLACK_COLOR = 20, 20, 40


class WindowObject(object):

    def __init__(self, sprite, x_pos, y_pos):
        self.sprite = sprite
        self.x_pos = x_pos
        self.y_pos = y_pos


class Window(object):

    def __init__(self, screen):
        self.screen = screen
        self.content = {}

    def prepare(self, sprite, quantity, y_pos):
        self.content[sprite.image] = []
        for i in range(quantity):
            obj = WindowObject(sprite, i*sprite.width, y_pos)
            self.add(obj)

    def add(self, obj):
        if obj.sprite.image not in self.content:
            self.content[obj.sprite.image] = []
        self.content[obj.sprite.image].append(obj)

    def draw(self):
        self.screen.fill(BLACK_COLOR)
        for k, v in self.content.items():
            for obj in v:
                self.screen.blit(obj.sprite.drawer, (obj.x_pos, obj.y_pos))
        pygame.display.update()
