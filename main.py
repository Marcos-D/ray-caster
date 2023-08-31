import pygame, sys
from pygame.locals import *
import numpy as np
from map import *
from player import *
from ray import *
from projector import *

pygame.init()
gameWidth = 1280
gameHeight = 720
# pygame.event.set_grab(True)


class Game:    
    def __init__(self):
        self.w = gameWidth
        self.h = gameHeight
        self.win = pygame.display.set_mode((self.w, self.h))
        self.clock = pygame.time.Clock()
        self.map = Map(self)
        self.player = Player(self, 160, 160, math.pi/4)
        # print(self.map.world)

    def update(self):
        dt = self.clock.tick(60) / 1000
        self.player.update(dt)
        p = Projector(self, self.player)
        p.projectRay()

        pygame.display.flip()
        pygame.display.set_caption(f'{self.clock.get_fps() :.1f}')

    def draw(self):
        self.win.fill('black')
        self.map.draw()
        self.player.draw()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(self.player.x, self.player.y)
            if event.type == pygame.QUIT:
                pygame.quit()
    
    def run(self):
        while 1:
            self.check_events() 
            self.draw()
            self.update()
    
while __name__ == "__main__":
    g = Game()
    g.run()