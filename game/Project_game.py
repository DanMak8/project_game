import pygame

pygame.init()

win_width = 1300
win_height = 600
clock = pygame.time.Clock()
win = pygame.display.set_mode((win_width, win_height))

pygame.display.set_caption('not one spoilers')

sound = pygame.mixer.music.load("sounds/tra.wav")
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(loops=-1)

# загрузка спрайтов
left_stand = [pygame.image.load('stand/stand_left_1.png')]

right_stand = [pygame.image.load('stand/stand_right_1.png')]

right_walk = [pygame.image.load('walk/walk_right_1.png'),
              pygame.image.load('walk/walk_right_2.png'),
              pygame.image.load('walk/walk_right_3.png'),
              pygame.image.load('walk/walk_right_4.png'),
              pygame.image.load('walk/walk_right_5.png'),
              pygame.image.load('walk/walk_right_6.png')]
    
left_walk = [pygame.image.load('walk/walk_left_1.png'),
             pygame.image.load('walk/walk_left_2.png'),
             pygame.image.load('walk/walk_left_3.png'),
             pygame.image.load('walk/walk_left_4.png'),
             pygame.image.load('walk/walk_left_5.png'),
             pygame.image.load('walk/walk_left_6.png')]

shadow = [pygame.image.load('shadow_cloning/sc_1.png'),
          pygame.image.load('shadow_cloning/sc_2.png'),
          pygame.image.load('shadow_cloning/sc_3.png'),
          pygame.image.load('shadow_cloning/sc_4.png'),
          pygame.image.load('shadow_cloning/sc_5.png')]

right_run = [pygame.image.load('run/run_right_1.png'),
             pygame.image.load('run/run_right_2.png'),
             pygame.image.load('run/run_right_3.png'),
             pygame.image.load('run/run_right_4.png'),
             pygame.image.load('run/run_right_5.png'),
             pygame.image.load('run/run_right_6.png')]

left_run = [pygame.image.load('run/run_left_1.png'),
            pygame.image.load('run/run_left_2.png'),
            pygame.image.load('run/run_left_3.png'),
            pygame.image.load('run/run_left_4.png'),
            pygame.image.load('run/run_left_5.png'),
            pygame.image.load('run/run_left_6.png')]

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

last_move = 'right'
work = True

# техники
shadow_cloning = False
clon_x = x
clon_y = y
clon_width = width
clon_height = height
clon_anim_cnt = 0
cloning_anim_cnt = 0
clon_right = False
clon_left = False
clon_last_move = 'right'
clon_speed = 15

right_walk = [pygame.transform.scale(picture, (width, height)) for picture in right_walk]
left_walk = [pygame.transform.scale(picture, (width, height)) for picture in left_walk]
right_stand = [pygame.transform.scale(picture, (width, height)) for picture in right_stand]
left_stand = [pygame.transform.scale(picture, (width, height)) for picture in left_stand]
shadow = [pygame.transform.scale(picture, (140, 122)) for picture in shadow]
left_run = [pygame.transform.scale(picture, (116, 90)) for picture in left_run]
right_run = [pygame.transform.scale(picture, (116, 90)) for picture in right_run]

# рисующая функция
def draw():
    global anim_cnt, clon_anim_cnt, cloning_anim_cnt
    global cloning_anim_cnt, clon_speed
    win.fill((0, 100, 255))
    # хитбокс персонажа
    # pygame.draw.rect(win, (0, 255, 0), (x, y, width, height))
    
    if anim_cnt >= 30:
        anim_cnt = 0
        
    if clon_anim_cnt >= 30:
        clon_anim_cnt = 0
        
    if run:
        if right:
            win.blit(right_run[anim_cnt // 5], (x, y))
            anim_cnt += 1
        elif left:
            win.blit(left_run[anim_cnt // 5], (x, y))
            anim_cnt += 1   
        else:
            if last_move == 'right':
                win.blit(right_stand[0], (x, y))
            if last_move == 'left':
                win.blit(left_stand[0], (x, y))            
    else:
        if left:
            win.blit(left_walk[anim_cnt // 5], (x, y))
            anim_cnt += 1
        elif right:
            win.blit(right_walk[anim_cnt // 5], (x, y))
            anim_cnt += 1
        else:
            if last_move == 'right':
                win.blit(right_stand[0], (x, y))
            if last_move == 'left':
                win.blit(left_stand[0], (x, y))
        
    if shadow_cloning:
        # pygame.draw.rect(win, (255, 0, 0), (clon_x, clon_y, clon_width, clon_height))
        if cloning_anim_cnt != 25:
            clon_speed = 0
            win.blit(shadow[cloning_anim_cnt // 5], (clon_x - 15, clon_y - 15))
            cloning_anim_cnt += 1
        else:
            clon_speed = 15
            if clon_right:
                win.blit(right_run[clon_anim_cnt // 5], (clon_x, clon_y))
                clon_anim_cnt += 1
            elif clon_left:
                win.blit(left_run[clon_anim_cnt // 5], (clon_x, clon_y))
                clon_anim_cnt += 1            
            else:
                if clon_last_move == 'right':
                    win.blit(right_stand[0], (clon_x, clon_y))
                if clon_last_move == 'left':
                    win.blit(left_stand[0], (clon_x, clon_y))
    else:
        cloning_anim_cnt = 0
            
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
    if keys[pygame.K_DOWN]:
        clon_x = x + 46
        clon_y = y                
        shadow_cloning = True
    
    elif keys[pygame.K_RCTRL]:
        shadow_cloning = False
    
    if keys[pygame.K_RIGHT] and clon_x < win_width - width - 5:
        clon_x += clon_speed
        clon_right = True
        clon_left = False
        clon_last_move = 'right'
        
    elif keys[pygame.K_LEFT] and clon_x > 5:
        clon_x -= clon_speed
        clon_left = True
        clon_right = False
        clon_last_move = 'left'
        
    else:
        clon_left = False
        clon_right = False
    draw()
    
pygame.quit()
    
        