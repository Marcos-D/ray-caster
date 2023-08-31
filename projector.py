from ray import *
import numpy as np

class Projector:
    def __init__(self, game, player):
        self.game = game
        self.player = player
    
    def projectRay(self):
        # currAngle = self.player.fovLeft
        # numRays = 100
        # print(math.degrees(self.player.fovLeft))
        # print(math.degrees(self.player.fovRight))
        
        for currAngle in np.arange(self.player.fovRight, self.player.fovLeft, 0.0174533 * 2):
            ray = Ray(self.game, self.player.x, self.player.y, currAngle)
            ray.cast()
            ray.draw()
             