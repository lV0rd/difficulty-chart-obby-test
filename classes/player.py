import pygame


class player:
    def __init__(self, window):
        self.obj = pygame.Rect(0, 0, 20, 20)
        self.obj.center = window.get_rect().center
        self.speed = .4
        self.weight = .7
        self.x = 0
        self.y = 0

    def run(self, xVel, yVel, dt):
        self.x += (self.weight * self.speed * xVel) * dt
        self.y += (self.weight * self.speed * yVel) * dt
        self.obj.x = self.x
        self.obj.y = self.y

    def update(self, x, y):
        self.x = x
        self.y = y
        self.obj.x = self.x
        self.obj.y = self.y

    def updateCentre(self, x, y):
        self.obj.centerx = x
        self.obj.centery = y
