import math
import random
import pygame
from pygame import mixer
# Ecran/Screen
pygame.init()
WIDTH, HEIGHT = 1500, 500
win = pygame.display.set_mode((1500, 500),pygame.RESIZABLE)
pygame.display.set_caption("Hangman By deiluc")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
BG = pygame.image.load("bg.png")


def get_font(size):
    return pygame.font.Font("font.ttf", size)

# Variabile butoane/Button variables
RADIUS = 20
GAP = 15
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
starty = 400
A = 65
for i in range(26):
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x, y, chr(A + i), True])

# Fonturi/Fonts
LETTER_FONT = pygame.font.SysFont('comicsans', 40)
WORD_FONT = pygame.font.SysFont('comicsans', 60)
TITLE_FONT = pygame.font.SysFont('comicsans', 70)

''' Optional 
# Muzica funda/Background music
mixer.music.load("sunet.mp3")
mixer.music.play(-1)
'''
# Incarcare imagini/Load image
images = []
for i in range(7):
    image = pygame.image.load(str(i) + ".png")
    images.append(image)

# Variabile joc/Game variables
hangman_status = 0
from cuvinte import cuv
word = random.choice(cuv)
guessed = []

# Culori/Colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


def draw():
    win.fill(WHITE)

    # Titlu/Title
    text = TITLE_FONT.render("Spanzuratoarea", 1, BLACK)
    win.blit(text, (WIDTH / 2 - text.get_width() / 2, 20))

    # Cuvinte/Words
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, 1, BLACK)
    win.blit(text, (400, 200))

    # Butoane/Buttons
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(win, BLACK, (x, y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, 1, BLACK)
            win.blit(text, (x - text.get_width() / 2, y - text.get_height() / 2))

    win.blit(images[hangman_status], (150, 100))
    pygame.display.update()


def display_message(message):
    pygame.time.delay(1000)
    win.fill(WHITE)
    text = WORD_FONT.render(message, 1, BLACK)
    win.blit(text,(WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 - text.get_height() / 2))
    pygame.display.update()
    pygame.time.delay(3000)


FPS = 60
clock = pygame.time.Clock()


def main():
    global hangman_status

    FPS = 60
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                for letter in letters:
                    x, y, ltr, visible = letter
                    if visible:
                        dis = math.sqrt((x - m_x) ** 2 + (y - m_y) ** 2)
                        if dis < RADIUS:
                            letter[3] = False
                            guessed.append(ltr)
                            if ltr not in word:
                                hangman_status += 1

        draw()

        won = True
        for letter in word:
            if letter not in guessed:
                won = False
                break

        if won:
            display_message("Ai castigat!")
            display_message("Se initiaza inchiderea automata!")
            break

        if hangman_status == 6:
            display_message("Cuvantul era: " + word)
            display_message("Ai pierdut")
            display_message("Se initiaza inchiderea automata!")
            break
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    main()
    break