import pygame

pygame.init()

# Clock
clock = pygame.time.Clock()

# RGB colours

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Window set up
win_width = 500
win_height = 400
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Algorithm Visualiser")


# while loop

state = True

while state:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state = False
    
    win.fill(BLACK)

    pygame.display.update()
    clock.tick(30)

# Pygame quit
pygame.quit()
quit()
