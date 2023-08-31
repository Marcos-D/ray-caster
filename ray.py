import pygame, sys
from pygame.locals import *
import math

class Ray:  
    def __init__(self, game, x, y, heading):
        self.x = x
        self.y = y
        self.game = game
        # self.player = player
        
        # self.angle = (math.pi*2) - player.heading # 0 <= theta < 2pi now
        self.angle = heading
        self.endX = self.x
        self.endY = self.y
        
        self.r = 0
    def getGridCoord(self, x, y):
        return (math.floor(x / self.game.map.s), math.floor(y / self.game.map.s))
    
    # returns true if point corresponds to wall
    # @param point: grid coordinates not standard pixels 
    def checkCollision(self, point):
        return point in self.game.map.world
    
    def withinWorld(self, x, y):
        return (x > 0 and x < self.game.w) and (y > 0 and y < self.game.h)
            
    # def calculateStep(self, x, y):
    #     mapX, mapY = self.getGridCoord(x,y)
    #     return 0 #placeholder
    
    def cast(self):
        # tao = self.angle%(2*math.pi)
        # rayFacingUp =  tao <= math.pi and tao >= 0
        # rayFacingRight = tao+(math.pi/2) < math.pi and tao+(math.pi/2) > 0
        rayFacingUp =  self.angle <= math.pi and self.angle >= 0
        rayFacingRight = self.angle <= math.pi/2 or self.angle >= 3*math.pi/2
        # print(math.degrees(self.angle))

        #Ax, Ay is point of collision through horizontal checking
        if(rayFacingUp):
            Ay = math.floor(self.y/self.game.map.s) * (self.game.map.s) - 1
            Ya = -1 * self.game.map.s
            Xa = self.game.map.s/math.tan(self.angle)
        #if ray facing down
        else:
            Ay = math.floor(self.y/self.game.map.s) * (self.game.map.s) + self.game.map.s
            Ya = self.game.map.s
            Xa = -self.game.map.s/math.tan(self.angle)
        
        Ax = self.x + (self.y - Ay)/math.tan(self.angle)

        #infinitely large number so it losses the comparison
        # if this does cause some performance issue TODO:
        dist1 = math.pow(10, 9)
        while(self.withinWorld(Ax, Ay)):
            if(self.checkCollision(self.getGridCoord(Ax, Ay))):
                dist1 = math.sqrt(math.pow(self.x - Ax, 2) + math.pow(self.y - Ay, 2))
                break
            Ax += Xa; 
            Ay += Ya  
            # print(Ax, Ay)

        # DEBUG
        # pygame.draw.line(self.game.win, (255,0,0), (self.x, self.y), (Ax, Ay))
        # pygame.draw.line(self.game.win, (0,0,255), (Ax, Ay), (Ax + Xa, Ay + Ya))
        
        #Bx, By is point of collision through vertical checking
        if(rayFacingRight):
            Bx = math.floor(self.x/self.game.map.s) * (self.game.map.s) + self.game.map.s
            Xb = self.game.map.s
            Yb = -self.game.map.s*math.tan(self.angle)
        else:
            Bx = math.floor(self.x/self.game.map.s) * (self.game.map.s) - 1
            Xb = -1 * self.game.map.s
            Yb = self.game.map.s*math.tan(self.angle)
        By = self.y+(self.x - Bx)*math.tan(self.angle)
    
        dist2 = math.pow(10, 9)  
        while(self.withinWorld(Bx, By)):
            if(self.checkCollision(self.getGridCoord(Bx, By))):
                dist2 = math.sqrt(math.pow(self.x - Bx, 2) + math.pow(self.y - By, 2))
                break            
            Bx += Xb; 
            By += Yb
            # print(Bx, By)

        # DEBUG
        # pygame.draw.line(self.game.win, (127,127,127), (self.x, self.y), (Bx, By))
        # pygame.draw.line(self.game.win, (0,0,255), (Bx, By), (Bx + Xb, By + Yb))
        
  
        self.r = min(dist1, dist2)
        self.endX += self.r * math.cos(self.angle)
        self.endY -= self.r * math.sin(self.angle)

    def test(self):
        testDistance = 50
        self.endX += testDistance * math.cos(self.angle)
        self.endY -= testDistance * math.sin(self.angle)
    
    def draw(self):
        pygame.draw.line(self.game.win, (255,0,0), (self.x, self.y), (self.endX, self.endY))


