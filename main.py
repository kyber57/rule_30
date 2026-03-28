import pygame
import random


def save_sequence(sequence: list[str]):
    with open('sequence.txt', 'w') as f:
        for s in sequence:
            for v in s:
                f.write(v+', ')
            f.write('\n')
        
        f.close()


pygame.init()
screen = pygame.display.set_mode(size=(1280, 720))
clock = pygame.time.Clock()
running = True 

BLOCK_SIZE = 8

COLOR_BIN_BLACK = pygame.Color(0, 0, 0)
COLOR_BIN_WHITE = pygame.Color(255, 255, 255)
CELL_SIZE: float = 50.
x_center = (screen.get_width() / 2) - (CELL_SIZE / 2)
y_center = (screen.get_height() / 2) - (CELL_SIZE / 2)

cells = [pygame.Rect(x_center + (i*CELL_SIZE) - (CELL_SIZE * (BLOCK_SIZE / 2)), y_center, CELL_SIZE, CELL_SIZE) for i in range(BLOCK_SIZE)]

sequence = []
while running:

    try:

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                running = False
                save_sequence(sequence)
                print("Bye bye...")
                
        screen.fill('white')
        
        inner_sequence = []
        for cell in cells:
            color = COLOR_BIN_BLACK if random.random().__round__() == 0 else COLOR_BIN_WHITE
            
            if color == COLOR_BIN_BLACK:
                inner_sequence.append('1')
                pygame.draw.rect(screen, color=color, rect=cell, width=0)
            elif color == COLOR_BIN_WHITE:
                inner_sequence.append('0')
                pygame.draw.rect(screen, color=color, rect=cell, width=1)

        print("Game is going on...")
        print("/n/n")

        pygame.display.flip()

        clock.tick(10)
        sequence.append(inner_sequence)

    except KeyboardInterrupt:
        save_sequence(sequence)

        print("Bye bye motherfucker!")
        pygame.quit()



pygame.quit()