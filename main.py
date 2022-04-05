import pygame

pygame.init()

# Clock
clock = pygame.time.Clock()

# RGB colours

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

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

    X = 100; Y = 120; width = 10; height = 30

    pygame.draw.rect(win, WHITE, (X, Y, width, height), border_radius = 5)

    pygame.display.update()
    clock.tick(30)

# Pygame quit
pygame.quit()
quit()
