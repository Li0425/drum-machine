import pygame
from pygame import mixer

pygame.init()

WIDTH = 1400
HEIGHT = 800

black = (0, 0, 0)
white = (255, 255, 255)
gray = (128, 128, 128)
green = (0, 255, 0)
gold = (212, 175, 55)

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Beat Maker")
label_font = pygame.font.Font("freesansbold.ttf", 32)

fps = 60
timer = pygame.time.Clock()
beat_count = 8
instrument_count = 6
clicked = [[-1 for _ in range(beat_count)]
           for _ in range(instrument_count)]  # -1 means not active


def draw_grid(clicked):
    left_menu = pygame.draw.rect(screen, gray, [0, 0, 200, HEIGHT - 200], 5)
    bottom_menu = pygame.draw.rect(
        screen, gray, [0, HEIGHT - 200, WIDTH, 200], 5)
    colours = [gray, white, gray]
    boxes = []

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
            if clicked[j][i] == -1:
                colour = gray
            else:
                colour = green
            rect_shape = pygame.draw.rect(
                screen,
                colour,
                [
                    i * (WIDTH - 200) // beat_count + 205,
                    (j * 100) + 5,
                    (WIDTH - 200) // beat_count - 10,
                    (HEIGHT - 200) // instrument_count - 10
                ],
                0,
                5
            )
            pygame.draw.rect(
                screen,
                gold,
                [
                    i * (WIDTH - 200) // beat_count + 200,
                    (j * 100),
                    (WIDTH - 200) // beat_count,
                    (HEIGHT - 200) // instrument_count
                ],
                5,
                5
            )
            pygame.draw.rect(
                screen,
                black,
                [
                    i * (WIDTH - 200) // beat_count + 200,
                    (j * 100),
                    (WIDTH - 200) // beat_count,
                    (HEIGHT - 200) // instrument_count
                ],
                2,
                5
            )
            # rect_shape is for collision detection
            boxes.append((rect_shape, (i, j)))
    return boxes


run = True
while run:
    timer.tick(fps)  # as long as run is True, execute code 60 times per sec
    screen.fill(black)
    boxes = draw_grid(clicked)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for box in boxes:
                rect_object = box[0]
                if rect_object.collidepoint(event.pos):
                    coords = box[1]
                    clicked[coords[1]][coords[0]] *= -1

    pygame.display.flip()  # throw everything onto the screen
pygame.quit()
