import pygame
import time
import random
from classes.player import player
from classes.proj import proj
from classes.enemy import enemy
from classes.settings import *

pygame.init()
window = pygame.display.set_mode((RES))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 20)

run = True

projs = []
enems = []

score = 0

states = {
    'L_S': 0,
    'L_E': 0
}

info = {
    'AMMO':30
}

DEBOUNCE_S = .1
DEBOUNCE_E = 1


def checkColl(first, second):
    return first.obj.colliderect(second.obj)

def message_display(text):
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(30, 10))
    window.blit(text_surface, text_rect)


rect = player(window)
dt = 1

while run:
    dt = clock.tick(FPS)
    pygame.display.set_caption(f'Game, FPS: {round(clock.get_fps())}')
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if time.time() - states['L_S'] >= DEBOUNCE_S:
                    states['L_S'] = time.time()
                    newProj = proj(window, .4, 5)
                    newProj.update(rect.x + 10 - 7.5, rect.y + 10)
                    projs.append(newProj)

    keys = pygame.key.get_pressed()

    rect.run((keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]), (keys[pygame.K_DOWN] - keys[pygame.K_UP]), dt)

    rect.update(rect.obj.x % window.get_width(), rect.obj.y % window.get_height())

    window.fill(0)
    pygame.draw.rect(window, (255, 0, 0), rect.obj)

    if time.time() - states['L_E'] >= DEBOUNCE_E:
        states['L_E'] = time.time()
        enem = enemy(window)
        enem.update(random.randint(1 + 10, WIDTH) ,HEIGHT//2)
        enems.append(enem)
        

    for v in projs:
        v.run(0, 1, dt)
        pygame.draw.rect(window, (0, 255, 255), v.obj)
        for j in enems:
            if checkColl(v, j):
                enems.remove(j)
                score += 1
            else:
                pygame.draw.rect(window, (0, 255, 0), j.obj)


    message_display(f'score: {score}')
    pygame.display.flip()

pygame.quit()
exit()
