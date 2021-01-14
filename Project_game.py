import pygame

pygame.init()

win_width = 1300
win_height = 600
clock = pygame.time.Clock()
win = pygame.display.set_mode((win_width, win_height))

pygame.display.set_caption('not one spoilers')

# загрузка спрайтов


# параметры персонажа
width = 80
height = 108
x = 40
y = win_height - height - 5
speed = 5
in_the_air = False
jump_count = 10

left = False
right = False
run = False
stand = True
anim_cnt = 0

last_move = None
work = True

# техники
shadow_cloning = False
clon_x = x
clon_y = y

# рисующая функция
def draw():
    global anim_cnt, shadow_cloning
    
    win.fill((0, 100, 255))
    #хитбокс персонажа
    pygame.draw.rect(win, (0, 255, 0), (x, y, width, height))
    
    
    if shadow_cloning:
        #win.blit(right_walk[anim_cnt // 5], (clon_x, clon_y))
        #anim_cnt += 1
        pygame.draw.rect(win, (255, 0, 0), (clon_x, clon_y, width, height))
        
    pygame.display.update()
    
while work:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            work = False
    
    # список клавиш
    keys = pygame.key.get_pressed()
        
    # отслеживание нажатий и выполнение действий
    if not in_the_air:
        if keys[pygame.K_LSHIFT]:
            speed = 15
            run = True
        else:
            speed = 5
            run = False
            
        if keys[pygame.K_a] and x > 5:
            x -= speed
            left = True
            right = False
            last_move = 'left'
            stand = False
                
        elif keys[pygame.K_d] and x < win_width - width - 5:
            x += speed
            right = True
            left = False
            last_move = 'right'
            stand = False
                
        else:
            right = False
            left = False
            stand = True
            anim_cnt = 0
            
        if keys[pygame.K_SPACE] or keys[pygame.K_w]:
            in_the_air = True
        
        if keys[pygame.K_DOWN]:
            clon_x = x
            clon_y = y            
            shadow_cloning = True
        
        if keys[pygame.K_RIGHT] and clon_x < win_width - width - 5:
            clon_x += 15
        
        if keys[pygame.K_LEFT] and clon_x > 5:
            clon_x -= 15
        

    else:
        # прыжок
        if jump_count >= -10:
            if jump_count < 0:
                y += (jump_count ** 2) / 2
            else:
                y -= (jump_count ** 2) / 2
            jump_count -= 1
        else:
            in_the_air = False
            jump_count = 10
            
        if left == True and x > 5:
            x -= speed
        elif right == True and x < win_width - width - 5:
            x += speed
    draw()
    
pygame.quit()
