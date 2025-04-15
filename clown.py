import pygame
from pygame.math import Vector2

clown_image = pygame.image.load("clown.png")
clown_rect = clown_image.get_rect()

class Clown(object):
    def __init__(self, clown_rect):
        self.location = Vector2(clown_rect[0], clown_rect[1])
        self.velocity = Vector2(0.2, 0.2)
        self.acceleration = Vector2(0,0)
        self.clown_rect = clown_rect

    def display(self):
        self.clown_rect.x = self.location.x
        self.clown_rect.y = self.location.y
        return self.clown_rect

    def update(self):
        self.location+=self.velocity
        self.velocity+= self.acceleration

        self.acceleration*=0

    def applyForce(self, force):
        self.acceleration += force

    def inSurface(self, pos):
        if self.clown_rect.center[0]-32 < pos[0] < self.clown_rect.center[0]+32 and self.clown_rect.center[1] - 32 < pos[1] < self.clown_rect.center[1] + 32:
            return True
        else:
            return False

    def checkEdges(self, WIDTH, HEIGHT):
        if self.location.x>(WIDTH-64) or self.location.x<0:
            self.velocity.x*=-1
        elif self.location.y>(HEIGHT-64) or self.location.y<0:
            self.velocity.y*=-1