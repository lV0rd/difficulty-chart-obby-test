import pygame
from classes.settings import *

class enemy:
    def __init__(self, window):
        self.obj = pygame.Rect(0, 0, 10, 10)
        self.obj.center = window.get_rect().center
        self.x = 0
        self.y = 0

    def walk(self):
        if self.x + 4 > WIDTH // 1.5:
            self.x -= 2
        else:
            self.x += 2

        self.obj.x = self.x
        

    def update(self, x, y):
        self.x = x
        self.y = y
        self.obj.x = self.x
        self.obj.y = self.y

