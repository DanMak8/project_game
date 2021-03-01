import pygame

pygame.init()

show = True

font = pygame.font.SysFont('arialblack', 40)
mus = pygame.font.SysFont('arialblack', 20)
start_text = font.render('start', 1, (0, 0, 0))
quit_text = font.render('quit', 1, (0, 0, 0))
music_text = mus.render('mus', 1, (0, 0, 0))

win_width = 1600
win_height = 984
platform_width = 201
platform_height = 93
clock = pygame.time.Clock()
win = pygame.display.set_mode((win_width, win_height))

pygame.display.set_caption('not one spoilers')

sound = pygame.mixer.Sound("sounds/tra.wav")
sound.set_volume(0.3)

fail = pygame.mixer.Sound("sounds/no one.mp3")
fail.set_volume(0.3)

run_sound = pygame.mixer.Sound("sounds/run.mp3")

throw_sound = pygame.mixer.Sound("sounds/throw_sound.mp3")
throw_sound.set_volume(0.3)

pause = pygame.mixer.Sound("sounds/pause.mp3")
pause.set_volume(0.2)

sasuke = pygame.mixer.Sound("sounds/sasukeeee.wav")
sasuke.set_volume(0.5)


play_music = 1

level = [
       '        '
       '        ',
       '        ',
       '        ',
       '        ',
       '-      -',
       '        ',
       '--------']

# загрузка спрайтов
bg = pygame.image.load('texture/bg.jpg')

platform = pygame.image.load('texture/block_loc_1.png')

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

right_throw = [pygame.image.load('throw/right_throw_1.png'),
              pygame.image.load('throw/right_throw_2.png'),
              pygame.image.load('throw/right_throw_3.png')]

left_throw = [pygame.image.load('throw/left_throw_1.png'),
             pygame.image.load('throw/left_throw_2.png'),
             pygame.image.load('throw/left_throw_3.png')]

sasuke_left = [pygame.image.load('enemy/sasuke_left_1.png'),
               pygame.image.load('enemy/sasuke_left_2.png'),
               pygame.image.load('enemy/sasuke_left_3.png'),
               pygame.image.load('enemy/sasuke_left_4.png'),
               pygame.image.load('enemy/sasuke_left_5.png')]

sasuke_right = [pygame.image.load('enemy/sasuke_right_1.png'),
                pygame.image.load('enemy/sasuke_right_2.png'),
                pygame.image.load('enemy/sasuke_right_3.png'),
                pygame.image.load('enemy/sasuke_right_4.png'),
                pygame.image.load('enemy/sasuke_right_5.png')]

# параметры персонажа
width = 80
height = 108
x = 40
y = win_height - height - 45
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

#параметры врага
sasuke_width = 127
sasuke_height = 135
sasuke_x = 1450
sasuke_y = 600
shot = False
sasuke_anim_cnt = 0

# техники
shadow_cloning = False
clon_x = x
clon_y = y
clon_width = width
clon_height = height
clon_anim_cnt = 0
cloning_anim_cnt = 0
throw_anim_cnt = 0
clon_right = False
clon_left = False
clon_last_move = 'right'
clon_speed = 15
throwing = False
bullets = []

right_walk = [pygame.transform.scale(picture, (width, height)) for picture in right_walk]
left_walk = [pygame.transform.scale(picture, (width, height)) for picture in left_walk]
right_stand = [pygame.transform.scale(picture, (width, height)) for picture in right_stand]
left_stand = [pygame.transform.scale(picture, (width, height)) for picture in left_stand]
shadow = [pygame.transform.scale(picture, (140, 122)) for picture in shadow]
left_run = [pygame.transform.scale(picture, (116, 90)) for picture in left_run]
right_run = [pygame.transform.scale(picture, (116, 90)) for picture in right_run]
bg = pygame.transform.scale(bg, (win_width, win_height))
platform_ = pygame.transform.scale(platform, (platform_width, platform_height))
right_throw = [pygame.transform.scale(picture, (104, 100)) for picture in right_throw]
left_throw = [pygame.transform.scale(picture, (104, 100)) for picture in left_throw]
sasuke_right = [pygame.transform.scale(picture, (sasuke_width, sasuke_height)) for picture in sasuke_right]
sasuke_left = [pygame.transform.scale(picture, (sasuke_width, sasuke_height)) for picture in sasuke_left]

def music():
    global play_music
    play_music *= -1
    
    if play_music == 1:
        sound.play(loops=-1)
    else:
        sound.stop()    
    
def start_game():
    global stand, clon_y, anim_cnt, shadow_cloning, run, work, throwing, in_the_air, x, y
    global win_width, win_height, clon_x, xlon_y, jump_count, bullets, right, left, last_move
    global clon_left, clon_right, clon_last_move, sasuke_x, sasuke_y, sasuke_height, sasuke_width
    global shot, health
    while work:
        clock.tick(30)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                work = False
        
        for bullet in bullets:
            if bullet.x < win_width and bullet.x > 0:
                bullet.x += bullet.vel
            else:
                bullets.pop(bullets.index(bullet))
            if bullet.x > sasuke_x and bullet.y > sasuke_y < sasuke_y + sasuke_height and bullet.y < sasuke_y + sasuke_height + 20:
                shot = True
                
        # список клавиш
        keys = pygame.key.get_pressed()
        # отслеживание нажатий и выполнение действий
        
        if not throwing:
            if keys[pygame.K_LCTRL]:
                if len(bullets) == 3:
                    fail.play(loops=1)
                else:
                    throw_sound.play(loops=1)
                throwing = True
                if last_move == 'right':
                    facing = 1
                else:
                    facing = -1
                if len(bullets) < 3:
                    bullets.append(Shuriken(round(x + width // 2), round(y + 25), 5, facing))
            
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

class Button:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.inactive_color = (13, 162, 58)
        self.active_color = (23, 204, 58)
   
    def draw(self, x_btn, y_btn, action=None):
        global show
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        if x_btn < mouse[0] < x_btn + self.w and y_btn < mouse[1] > y_btn - self.h:
            if y_btn < mouse[1] < y_btn + self.h:
                pygame.draw.rect(win, self.active_color, (x_btn, y_btn, self.w, self.h))
                if click[0] == 1:
                    pause.play(loops=1)
                    pygame.time.delay(300)
                    if action is not None:
                        if action == quit:
                            quit()
                            pygame.quit()
                            show = False
                        else:
                            action()
                            show = False
        else:
            pygame.draw.rect(win, self.inactive_color, (x_btn, y_btn, self.w, self.h))
            
def show_menu():
    global show, start_text
    menu_bg = pygame.image.load('menu/menu_image.jpg')
    menu_bg = pygame.transform.scale(menu_bg, (win_width, win_height))
    
    start_btn = Button(300, 70)
    quit_btn = Button(200, 50)
    
    sound.play(loops=-1)
    while show:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        win.blit(menu_bg, (0, 0))
        start_btn.draw(win_width // 2 - 200, win_height // 2 - 70, start_game)
        quit_btn.draw(win_width // 2 - 160, win_height // 2 + 100, quit)
        clock.tick(60)
        win.blit(start_text, (win_width // 2 - 115, win_height // 2 - 60))
        win.blit(quit_text, (win_width // 2 - 105, win_height // 2 + 90))
        pygame.display.update()
        
#класс куная
class Shuriken():
    def __init__(self, x, y, radius, facing):
        self.snaryad_right = pygame.image.load('throw/shuriken_left.png')
        self.snaryad_left = pygame.image.load('throw/shuriken_right.png')
        self.snaryad_left = pygame.transform.scale(self.snaryad_left, (40, 14))
        self.snaryad_right = pygame.transform.scale(self.snaryad_right, (40, 14))
        self.x = x
        self.y = y
        self.radius = radius
        self.facing = facing
        self.vel = 20 * facing
        
    def draw_shur(self, win):
        if self.facing == -1:
            win.blit(self.snaryad_right, (self.x, self.y))
        else:
            win.blit(self.snaryad_left, (self.x, self.y))
            
# рисующая функция
def draw():
    off_sound_btn = Button(50, 50)
    global anim_cnt, clon_anim_cnt, cloning_anim_cnt
    global cloning_anim_cnt, clon_speed, throw_anim_cnt
    global throwing, health, shot, sasuke_anim_cnt
    
    win.blit(bg, (0, 0))
    
    platform_x = 0
    platform_y = 360
    for row in level:
        for col in row:
            if col == '-':
                win.blit(platform, (platform_x, platform_y)) 
            platform_x += platform_width
        platform_y += platform_height
        platform_x = 0
        
    # хитбокс персонажа
    # pygame.draw.rect(win, (0, 255, 0), (x, y, width, height))
    
    for bullet in bullets:
        bullet.draw_shur(win)
    
    if anim_cnt >= 30:
        anim_cnt = 0
    
    if clon_anim_cnt >= 30:
        clon_anim_cnt = 0
    
    if throwing:
        if throw_anim_cnt != 8:    
            if last_move == 'right':
                win.blit(right_throw[throw_anim_cnt // 3], (x, y))
                throw_anim_cnt += 1
            else:
                win.blit(left_throw[throw_anim_cnt // 3], (x, y))
                throw_anim_cnt += 1
        else:
            throwing = False
            throw_anim_cnt = 0
    else:   
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
    off_sound_btn.draw(20, 20, music)
    if not shot:
        win.blit(sasuke_left[0], (sasuke_x, sasuke_y))
    else:
        if sasuke_anim_cnt != 25:
            win.blit(sasuke_left[sasuke_anim_cnt // 5], (sasuke_x, sasuke_y))
            sasuke_anim_cnt += 1
        else:
            win.blit(sasuke_left[4], (sasuke_x, sasuke_y))
    win.blit(music_text, (22, 25))
    pygame.display.update()
        
show_menu()

class Platform(pygame.sprite.Sprite):
    images = ['platform_1.png']
    # Конструктор класса платформ
    def __init__(self, x, y):
        super().__init__
        self.image = pygame.image.load(Platform.images[0].convert_alpha())
        self.rect = self.image.get_rect()
        self.rect.y = y
    
pygame.quit()
    
        