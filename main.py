import pygame
import random
import time

pygame.init()

sleep_time = 0.5

rect_height = []

def get_rect_height():
    rect_height = random.shuffle([i for i in range(1, 500)])

def draw_screen():

    X = 0
    width = 10

    for i in rect_height:
        pygame.draw.rect(win, WHITE, (X, 0, width, i), border_radius = 5)
        X += 10

    pygame.display.update()

def bubble_sort():
    swap = True
    while swap:
        swap = False
        for i in range(len(rect_height) - 1):
            if rect_height[i] > rect_height[i + 1]:
                temp = rect_height[i]
                rect_height[i] = rect_height[i + 1]
                rect_height[i + 1] = temp
                swap = True
                time.sleep(sleep_time)
                draw_screen()                

# Clock
clock = pygame.time.Clock()

# RGB colours

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Window set up
win_width = 1000
win_height = 500
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Algorithm Visualiser")


# while loop

state = True

while state:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state = False
    win.fill(BLACK)
    get_rect_height()
    draw_screen()
    clock.tick(30)


# Pygame quit
pygame.quit()
quit()
