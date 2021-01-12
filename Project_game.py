import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))

pygame.display.set_caption('not spoilers')

x = 40
y = 40
width = 70
height = 76
speed = 5

work = True
while work:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            work = False
            
pygame.quit()
    
        