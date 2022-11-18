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
beat_count = 8
instrument_count = 6


def draw_grid():
    left_menu = pygame.draw.rect(screen, gray, [0, 0, 200, HEIGHT - 200], 5)
    bottom_menu = pygame.draw.rect(
        screen, gray, [0, HEIGHT - 200, WIDTH, 200], 5)
    boxes = []
    colours = [gray, white, gray]

    hi_hat_text = label_font.render("Hi Hat", True, white)
    screen.blit(hi_hat_text, (20, 30))
    snare_text = label_font.render("Snare", True, white)
    screen.blit(snare_text, (20, 130))
    kick_text = label_font.render("Bass Drum", True, white)
    screen.blit(kick_text, (20, 230))
    crash_text = label_font.render("Crash", True, white)
    screen.blit(crash_text, (20, 330))
    clap_text = label_font.render("Clap", True, white)
    screen.blit(clap_text, (20, 430))
    floor_tom_text = label_font.render("Floor Tom", True, white)
    screen.blit(floor_tom_text, (20, 530))

    for i in range(1, instrument_count + 1, 1):
        pygame.draw.line(screen, gray, (0, i * 100), (200, i * 100), 3)

    for i in range(beat_count):
        for j in range(instrument_count):
            rect_shape = pygame.draw.rect(
                screen,
                gray,
                [
                    i * (WIDTH - 200) // beat_count + 200,
                    (j * 100),
                    (WIDTH - 200) // beat_count,
                    (HEIGHT - 200) // instrument_count
                ],
                5,
                5
            )


run = True
while run:
    timer.tick(fps)  # as long as run is True, execute code 60 times per sec
    screen.fill(black)
    draw_grid()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()  # throw everything onto the screen
pygame.quit()
