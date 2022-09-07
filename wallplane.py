import random
import pygame
import numpy as np
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.state = np.array([SCREEN_WIDTH/2, SCREEN_HEIGHT/2])
        self.surf = pygame.Surface((10, 10))
        self.rect = self.surf.get_rect(
            center=(
                self.state[0],
                self.state[1],
            )
        )

    def update_rect(self):
        self.rect = self.surf.get_rect(
            center=(
                self.state[0],
                self.state[1],
            )
        )


class Wall(pygame.sprite.Sprite):
    def __init__(self, position_x, position_y, width, height):
        super(Wall, self).__init__()
        self.surf = pygame.Surface((width, height))
        self.rect = self.surf.get_rect(
            center=(
                position_x + width/2,
                position_y + height/2,
            )
        )


class WallPlane:
    def __init__(self):
        pygame.init()
        # Set up the drawing window
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.SCREEN_HEIGHT = SCREEN_HEIGHT
        self.screen = pygame.display.set_mode([self.SCREEN_WIDTH, self.SCREEN_HEIGHT])
        self.player = Player()
        self.player.state = np.array([self.SCREEN_WIDTH/2, self.SCREEN_HEIGHT/2])
        self.big_wall1 = Wall(0, 0, 800, 10)
        self.big_wall2 = Wall(0, 790, 800, 10)
        self.big_wall3 = Wall(0, 0, 10, 800)
        self.big_wall4 = Wall(790, 0, 10, 800)
        self.wall_1 = Wall(0, 100, 300, 10)
        self.wall_2 = Wall(500, 100, 300, 10)
        self.wall_3 = Wall(0, 200, 300, 10)
        self.wall_4 = Wall(500, 200, 300, 10)
        self.wall_5 = Wall(0, 300, 300, 10)
        self.wall_6 = Wall(500, 300, 300, 10)
        self.wall_7 = Wall(0, 400, 300, 10)
        self.wall_8 = Wall(500, 400, 300, 10)
        self.wall_9 = Wall(0, 500, 300, 10)
        self.wall_10 = Wall(500, 500, 300, 10)
        self.wall_11 = Wall(0, 600, 300, 10)
        self.wall_12 = Wall(500, 600, 300, 10)
        self.wall_13 = Wall(0, 700, 300, 10)
        self.wall_14 = Wall(500, 700, 300, 10)
        self.walls = pygame.sprite.Group()
        self.walls.add(self.wall_1)
        self.walls.add(self.wall_2)
        self.walls.add(self.wall_3)
        self.walls.add(self.wall_4)
        self.walls.add(self.wall_5)
        self.walls.add(self.wall_6)
        self.walls.add(self.wall_7)
        self.walls.add(self.wall_8)
        self.walls.add(self.wall_9)
        self.walls.add(self.wall_10)
        self.walls.add(self.wall_11)
        self.walls.add(self.wall_12)
        self.walls.add(self.wall_13)
        self.walls.add(self.wall_14)
        self.walls.add(self.big_wall1)
        self.walls.add(self.big_wall2)
        self.walls.add(self.big_wall3)
        self.walls.add(self.big_wall4)

    def reset(self):
        self.player.state = np.array([self.SCREEN_WIDTH/2, self.SCREEN_HEIGHT/2])
        return self.player.state

    def step(self, act):
        x_pre_state = self.player.rect[0]
        y_pre_state = self.player.rect[1]
        self.player.state = self.player.state - act
        self.player.update_rect()
        for args in self.walls:
            if pygame.sprite.collide_rect(self.player, args):

                x_state = self.player.rect[0]
                y_state = self.player.rect[1]
                self.player.state = self.player.state + act
                if x_pre_state != x_state:
                    act[0] = -act[0]
                if y_pre_state != y_state:
                    act[1] = -act[1]
                self.player.state = self.player.state - act 
                break
                # collide when this change

        return self.player.state

    def render(self):
        for event in pygame.event.get():
        # check if the event is the X button
            if event.type == pygame.QUIT:
                # if it is quit the game
                self.close()
                exit(0)
        self.screen.fill((255, 255, 255))
        for args in self.walls:
            self.screen.blit(args.surf, args.rect)
        self.screen.blit(self.player.surf, self.player.rect)
        pygame.display.flip()

    def close(self):
        if self.screen is not None:
            pygame.display.quit()
            pygame.quit()


plane = WallPlane()
plane.reset()
# Run until the user asks to quit
running = True

i = 1

while running:

    action = (np.random.rand(2)*10)-5

    plane.step(action)

    plane.render()

# Done! Time to quit.

plane.close()
