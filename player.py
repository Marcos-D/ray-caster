import pygame, sys
from pygame.locals import *
import math

speed = 80;
angularSpeed = 0.0872665 * 30 ;
playerRadius = 5

class Player:
    def __init__(self, game, x, y, heading):
        # self.heading = math.pi * 2 - heading
        self.heading = heading
        self.x = x
        self.y = y
        # 60 is standard for FOV
        self.fov = 1.0472
        self.fovLeft = (self.heading + (self.fov/2)) %(2*math.pi) 
        self.fovRight = (self.heading - (self.fov/2)) %(2*math.pi) 
        
        
        self.game = game
        # self.gridX, self.gridY = self.getGridCoord(self.x, self.y) 
    
    # returns a point on the grid based on some x, y
    def getGridCoord(self, x, y):
        return (x // self.game.map.s, y // self.game.map.s)
    
    # returns true if point corresponds to wall
    # @param point: grid coordinates not standard pixels 
    def checkCollision(self, point):
        return point in self.game.map.world
    
    # handles collision + wall sliding 
    def tryMove(self, cX, cY, fX, fY):
        # X is limiting, Y is not 
        xColliding = self.checkCollision(self.getGridCoord(fX,cY))
        # Y is limiting, X is not 
        yColliding = self.checkCollision(self.getGridCoord(cX,fY))   

        # default to returning future position
        validMove = [fX, fY]
        
        # resort to current if future clips out of bounds
        if(xColliding):
            validMove[0] = cX
        if(yColliding):
            validMove[1] = cY      
        return validMove   
        
        # naive approach, don't move if moving into prohibited area
        # isColliding = self.checkCollision(self.getGridCoord(fX, fY))
        # if(isColliding):
        #     return [cX, cY] 
        # return [fX, fY]
    
    def handleMovement(self, dt):
        keys = pygame.key.get_pressed()
        #TODO: change to mouse controls in the future
        if keys[pygame.K_LEFT]:
            self.heading += angularSpeed * dt

        if keys[pygame.K_RIGHT]:
            self.heading -= angularSpeed * dt
        self.heading = self.heading%(2*math.pi) 

        dX = self.x
        dY = self.y
        if keys[pygame.K_w]:
            dX += speed * math.cos(self.heading) * dt
            dY -= speed * math.sin(self.heading) * dt
            # dX, dY = tryMove(pos_x, pos_y, dX, dY, objects, circles)

        if keys[pygame.K_a]:
            dX -= speed * math.cos(self.heading - math.pi/2) * dt 
            dY += speed * math.sin(self.heading - math.pi/2) * dt
            # dX, dY = tryMove(pos_x, pos_y, dX, dY, objects, circles)

        if keys[pygame.K_s]:
            dX -= speed * math.cos(self.heading)* dt
            dY += speed * math.sin(self.heading)* dt
            # dX, dY = tryMove(pos_x, pos_y, dX, dY, objects, circles)

        if keys[pygame.K_d]:
            dX += speed * math.cos(self.heading - math.pi/2)* dt
            dY -= speed * math.sin(self.heading - math.pi/2)* dt

        self.x, self.y = self.tryMove(self.x, self.y, dX, dY)

    def update(self, dt):
        self.handleMovement(dt)
        self.fovLeft = (self.heading + (self.fov/2)) %(2*math.pi) 
        self.fovRight = (self.heading - (self.fov/2)) %(2*math.pi) 
        
        # print(self.gridX, self.gridY)

    def draw(self):
        playerRect = pygame.Rect(self.x - playerRadius, self.y - playerRadius, playerRadius * 2, playerRadius * 2)
        pygame.draw.rect(self.game.win, (255,255,255), playerRect)

