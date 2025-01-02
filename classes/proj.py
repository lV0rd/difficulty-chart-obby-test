import pygame


class proj:
    def __init__(self, window, projSpeed, projWeight):
        self.obj = pygame.Rect(0, 0, 15, 15)
        self.obj.center = window.get_rect().center
        self.projSpeed = projSpeed or 4
        self.projWeight = projWeight or 2
        self.x = 0
        self.y = 0



    def run(self, xVel, yVel, dt):
        self.x += (self.projWeight * self.projSpeed * xVel) * dt
        self.y += (self.projWeight * self.projSpeed * yVel) * dt
        self.obj.x = self.x
        self.obj.y = self.y

    def update(self, x, y):
        self.x = x
        self.y = y
        self.obj.x = self.x
        self.obj.y = self.y

