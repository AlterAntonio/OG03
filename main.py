import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.setmode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Тир')
icon = pygame.image.load('img/duckhunt.jpg')
target_img = pygame.image.load('img/duck.png')
target_width = 50
target_height = 50
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_у = random.randint(0, SCREEN_HEIGHT - target_height)
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

running = True
while running:
    pass

pygame.quit()