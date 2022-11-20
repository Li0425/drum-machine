import pygame
from pygame import display, draw, mixer


pygame.init()

WIDTH = 1400
HEIGHT = 800

black = (0, 0, 0)
white = (255, 255, 255)
gray = (128, 128, 128)
dark_gray = (50, 50, 50)
green = (0, 255, 0)
gold = (212, 175, 55)
blue = (0, 255, 255)

screen = display.set_mode([WIDTH, HEIGHT])
display.set_caption("Beat Maker")
label_font = pygame.font.Font("freesansbold.ttf", 32)
medium_font = pygame.font.Font("freesansbold.ttf", 24)

fps = 60
timer = pygame.time.Clock()
beat_count = 8
instrument_count = 6
clicked = [[-1 for _ in range(beat_count)]
           for _ in range(instrument_count)]  # -1 means not active
bpm = 240
playing = True
active_length = 0
active_beat = 1
beat_changed = True

# load in sounds
hi_hat = mixer.Sound('./sounds/hi hat.WAV')
snare = mixer.Sound('./sounds/snare.WAV')
kick = mixer.Sound('./sounds/kick.WAV')
crash = mixer.Sound('./sounds/crash.wav')
clap = mixer.Sound('./sounds/clap.wav')
tom = mixer.Sound('./sounds/tom.WAV')
mixer.set_num_channels(instrument_count * 3)


def draw_grid(clicked, beat):
    left_menu = draw.rect(screen, gray, [0, 0, 200, HEIGHT - 200], 5)
    bottom_menu = draw.rect(
        screen, gray, [0, HEIGHT - 200, WIDTH, 200], 5)
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
        draw.line(screen, gray, (0, i * 100), (200, i * 100), 3)

    for i in range(beat_count):
        for j in range(instrument_count):
            if clicked[j][i] == -1:
                colour = gray
            else:
                colour = green
            rect_shape = draw.rect(
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
            draw.rect(
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
            draw.rect(
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
        active = draw.rect(
            screen,
            blue,
            [
                beat * ((WIDTH - 200)//beat_count) + 200,
                0,
                (WIDTH - 200) // beat_count,
                instrument_count * 100
            ],
            5,
            3
        )
    return boxes


def play_notes():
    for i in range(len(clicked)):
        if clicked[i][active_beat] == 1:
            if i == 0:
                hi_hat.play()
            if i == 1:
                snare.play()
            if i == 2:
                kick.play()
            if i == 3:
                crash.play()
            if i == 4:
                clap.play()
            if i == 5:
                tom.play()


run = True
while run:
    timer.tick(fps)  # as long as run is True, execute code 60 times per sec
    screen.fill(black)
    boxes = draw_grid(clicked, active_beat)

    # lower menu buttons
    play_pause = draw.rect(screen, gray, [
        50,
        HEIGHT - 150,
        200,
        100],
        0,
        5
    )
    play_text = label_font.render("Play/Pause", True, white)
    screen.blit(play_text, (70, HEIGHT - 130))
    if playing:
        play_text2 = medium_font.render("Playing", True, dark_gray)
    else:
        play_text2 = medium_font.render("Paused", True, dark_gray)
    screen.blit(play_text2, (70, HEIGHT - 100))

    if beat_changed:
        play_notes()
        beat_changed = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for box in boxes:
                rect_object = box[0]
                if rect_object.collidepoint(event.pos):
                    coords = box[1]
                    clicked[coords[1]][coords[0]] *= -1
        if event.type == pygame.MOUSEBUTTONUP:
            if play_pause.collidepoint(event.pos):
                if playing:
                    playing = False
                elif not playing:  # cannot be else!
                    playing = True

    beat_length = fps * 60 // bpm
    if playing:
        if active_length < beat_length:
            active_length += 1
        else:
            active_length = 0
            if active_beat < beat_count - 1:
                active_beat += 1
                beat_changed = True
            else:
                active_beat = 0
                beat_changed = True
    display.flip()  # throw everything onto the screen


pygame.quit()
