from flappia_bird.pipes import build_pipes, PIPE_STEP


class Game(object):
    def __init__(self, window, sprites, birds, pipes, speed):
        self.window = window
        self.sprites = sprites
        self.birds = birds
        self.pipes = pipes
        self.record = 0
        self.generation = 0
        self.speed = speed

    def background_movement(self):
        self.movement_x(self.sprites.cloud.name, 45)
        self.movement_x(self.sprites.build.name, 15)
        self.movement_x(self.sprites.tree.name, 5)
        self.movement_x(self.sprites.floor.name, 1)
        self.movement_pipes(1)

    def movement_x(self, name, step):
        for obj in self.window.content.get(name, []):
            obj.x_pos -= self.speed/step
            if obj.x_pos + obj.sprite.width >= 0:
                continue
            obj.x_pos += (len(self.window.content[name]) - 1) * obj.sprite.width

    def movement_pipes(self, step):
        decrease = self.speed/step
        upper = self.window.content.get(self.sprites.upper_pipe.name, [])
        lower = self.window.content.get(self.sprites.lower_pipe.name, [])
        for i in range(len(lower)):
            upper[i].x_pos -= decrease
            lower[i].x_pos -= decrease
            if lower[i].x_pos + lower[i].sprite.width < 0:
                new_upper, new_lower = build_pipes(
                    1, upper[i].sprite, lower[i].sprite, self.sprites.floor.height, self.window.screen.get_height()
                )
                new_upper.x_pos = upper[i].x_pos + (PIPE_STEP * len(upper))
                new_lower.x_pos = lower[i].x_pos + (PIPE_STEP * len(lower))
                upper[i] = new_upper
                lower[i] = new_lower
            upper[i].vertical_movement()
            lower[i].vertical_movement()

    def bird_movement(self):
        for bird in self.birds:
            if bird.is_dead:
                if bird.sprite.width + 5 >= bird.x_pos:
                    bird.x_pos -= self.speed

                if bird.y_pos >= 400:
                    bird.vertical_speed = 0
                    bird.y_pos = 400
                else:
                    bird.y_pos += bird.vertical_speed
            else:
                bird.fitness += 2.0
                bird.y_pos += bird.vertical_speed

                if bird.y_pos < 75 or bird.y_pos >= 400:
                    bird.kill()

    def apply_gravity(self):
        for bird in self.birds:
            if bird.using_parachute:
                continue
            bird.vertical_speed += 0.08
