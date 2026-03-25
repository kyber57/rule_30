import pygame
import random

pygame.init()
screen = pygame.display.set_mode(size=(1280, 720))
clock = pygame.time.Clock()
running = True 

# Rect cell
COLOR_BIN_BLACK = pygame.Color(0, 0, 0)
COLOR_BIN_WHITE = pygame.Color(255, 255, 255)
CELL_SIZE: float = 50
x_center = (screen.get_width() / 2) - (CELL_SIZE / 2)
y_center = (screen.get_height() / 2) - (CELL_SIZE / 2)
cell = pygame.Rect(x_center, y_center, CELL_SIZE, CELL_SIZE)

cells = [pygame.Rect(x_center, y_center, CELL_SIZE, CELL_SIZE) for _ in range(8)]


while running:


    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False 
    

    screen.fill('white')
    
    color = COLOR_BIN_BLACK if random.random().__round__() == 0 else COLOR_BIN_WHITE
    for cell in cells:
        cell.move(50., 0.)
        pygame.draw.rect(screen, color=color, rect=cell)

    print("Game is going on...")

    pygame.display.flip()

    clock.tick(30)


pygame.quit()