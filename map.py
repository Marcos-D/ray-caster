import pygame, sys
from pygame.locals import *
_ = False
grid = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, _, _, 1, _, _, 1, 1, 1, _, _, _, _, _, _, 1],
    [1, _, _, 1, _, 1, 1, 1, 1, _, _, _, _, _, _, 1],
    [1, _, _, _, _, _, _, 1, 1, _, _, _, _, _, 1, 1],
    [1, 1, _, 1, _, _, _, 1, 1, _, _, _, _, _, 1, 1],
    [1, _, _, 1, _, _, _, 1, 1, _, _, 1, 1, 1, 1, 1],
    [1, 1, _, _, _, 1, _, 1, _, _, _, 1, 1, 1, 1, 1],
    [1, 1, _, _, 1, 1, _, _, _, _, _, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]
class Map:
    def __init__(self, game):
        # empty dic of rects
        # for quick lookup
        self.game = game
        self.s = 80
        self.world = {} 
        self.rects = []
        self.gen_map()

    def gen_map(self):
        for j, col in enumerate(grid):
            for i, value in enumerate(col):
                if(value):
                    self.world[(i,j)] = value
                    square = pygame.Rect(i * self.s, j * self.s, self.s, self.s)
                    self.rects.append(square)
    
    def draw(self):
        for square in self.rects:
            pygame.draw.rect(self.game.win, (127, 127, 127), square, 2)