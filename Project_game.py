import pygame

pygame.init()

win_width = 500
win_height = 500
win = pygame.display.set_mode((win_width, win_height))

pygame.display.set_caption('not one spoilers')

# параметры персонажа
width = 70
height = 76
x = 40
y = win_height - height - 5
speed = 5
in_the_air = False
jump_count = 10

last_move = None

work = True
while work:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            work = False
    
    # список клавиш
    keys = pygame.key.get_pressed()
    # отслеживание нажатий и выполнение действий
    if not in_the_air:
        if keys[pygame.K_a] and x > 5:
            x -= speed
            last_move = 'left'
        elif keys[pygame.K_d] and x < win_width - width - 5:
            x += speed
            last_move = 'right'
        else:
            last_move = 'stand'
            
        if keys[pygame.K_SPACE] or keys[pygame.K_w]:
            in_the_air = True
        
        if keys[pygame.K_LSHIFT]:
            speed = 12
        else:
            speed = 5
    else:
        # способность прыгать
        if jump_count >= -10:
            if jump_count < 0:
                y += (jump_count ** 2) / 2
            else:
                y -= (jump_count ** 2) / 2
            jump_count -= 1
        else:
            in_the_air = False
            jump_count = 10
            
        if last_move == 'left' and x > 5:
            x -= speed
        elif last_move == 'right' and x < win_width - width - 5:
            x += speed
        
        
        
    
    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()
    
pygame.quit()
    
        
