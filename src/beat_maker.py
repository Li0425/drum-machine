import pygame
from pygame import mixer

pygame.init()

WIDTH = 1400
HEIGHT = 800

black = (0, 0, 0)
white = (255, 255, 255)
gray = (128, 128, 128)

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Beat Maker")
label_font = pygame.font.Font("freesansbold.ttf", 32)

fps = 60
timer = pygame.time.Clock()

run = True
while run:
    timer.tick(fps)  # as long as run is True, execute code 60 times per sec
    screen.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip  # throw everything onto the screen
pygame.quit()
