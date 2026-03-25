import pygame

pygame.init()
screen = pygame.display.set_mode(size=(1280, 720))
clock = pygame.time.Clock()
running = True 


while running:


    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False 
    

    screen.fill('purple')

    print("Game is going on...")

    pygame.display.flip()

    clock.tick(30)


pygame.quit()