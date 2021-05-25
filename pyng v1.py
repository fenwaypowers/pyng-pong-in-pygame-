import pygame, random, time
import pygame.freetype

pygame.init()
width = 600
height = 600

screen = pygame.display.set_mode([width,height])
white = [255, 255, 255]
red = [255, 0, 0]
green = [100,255,150]
black=[0,0,0]
screen.fill(black)
pygame.display.flip()
key_input = pygame.key.get_pressed()
ball_height=15
clock = pygame.time.Clock()
ball = pygame.draw.rect(screen, white, ((275,random.randint(50,550)),(ball_height,ball_height)))
leftp = pygame.draw.rect(screen, white, ((5,220),(15,60)))
rightp = pygame.draw.rect(screen, white, ((580,220),(15,60)))
leftp_up=False
leftp_down=False
rightp_up=False
rightp_down=False
direction=1
ydirection=random.choice([1,-1])
left_score=0
right_score=0

GAME_FONT = pygame.freetype.Font("Roboto-Bold.ttf", 48)
text_surface, rect = GAME_FONT.render(str(left_score), white)
screen.blit(text_surface, (40, 50))
text_surface, rect = GAME_FONT.render(str(right_score), white)
screen.blit(text_surface, (530, 50))

def movepaddle(paddle,downorup):
    increment=7
    newpaddle = paddle
    newy = paddle.y+(increment*downorup)
    pygame.draw.rect(screen, black, ((paddle.x,paddle.y),(paddle.width,paddle.height)))
    if newy > 540 or newy < 1:
        newpaddle = paddle
    else:
        newpaddle = pygame.draw.rect(screen, white, ((paddle.x,newy),(paddle.width,paddle.height)))
    return newpaddle

def COMmove(ball,paddle):
    increment=5
    newpaddle = paddle
    pygame.draw.rect(screen, black, ((paddle.x,paddle.y),(paddle.width,paddle.height)))

    newy=paddle.y

    if random.randint(1,6) != 1:
        
        if ball.y < paddle.y:
            newy +=(increment*-1)
        elif ball.y > paddle.y:
            newy +=(increment)
            
        if newy > 540 or newy < 1:
            newpaddle = paddle
        else:
            newpaddle = pygame.draw.rect(screen, white, ((paddle.x,newy),(paddle.width,paddle.height)))
          
    newpaddle = pygame.draw.rect(screen, white, ((paddle.x,newy),(paddle.width,paddle.height)))

    return newpaddle

def ball_move(ball,leftp,rightp,direction,ydirection):
    increment=5
    yincrement=5
    
    if (ball.y in range(leftp.y-30,leftp.y + leftp.height+10) and ball.x == leftp.x or ball.x > leftp.x and ball.x < (leftp.x+5)) or (ball.y in range(rightp.y-30,rightp.y + rightp.height+10) and ball.x == (rightp.x)):
        direction*=-1
    newx=(ball.x)+(increment*direction)

    if ball.y in range(leftp.y-30,leftp.y + int((0.5*leftp.height)+10)) and ball.x == leftp.x:
        ydirection=-1
    elif ball.y in range(int(1.5*(leftp.y-20)),leftp.y+leftp.height) and ball.x == leftp.x:
        ydirection=1

    if ball.y in range(rightp.y-30,rightp.y + int((0.5*rightp.height))) and ball.x == rightp.x:
        ydirection=-1
    elif ball.y in range(int(1.5*(rightp.y-20)),rightp.y+rightp.height) and ball.x == rightp.x:
        ydirection=1

    if ball.y > 580 or ball.y < 6:
        ydirection*=-1

    newy=ball.y+((yincrement)*ydirection)

    pygame.draw.rect(screen, black, ((ball.x,ball.y),(ball.width,ball.height)))
    newball = pygame.draw.rect(screen, white, ((newx,newy),(ball.width,ball.height)))
    return newball, direction, ydirection

def gameover(ball):
    time.sleep(0.5)
    screen.fill(black)
    ball = pygame.draw.rect(screen, white, ((275,random.randint(100,400)),(ball_height,ball_height)))
    leftp = pygame.draw.rect(screen, white, ((5,220),(15,60)))
    rightp = pygame.draw.rect(screen, white, ((580,220),(15,60)))
    text_surface, rect = GAME_FONT.render(str(left_score), white)
    screen.blit(text_surface, (40, 50))
    text_surface, rect = GAME_FONT.render(str(right_score), white)
    screen.blit(text_surface, (530, 50))
    leftp_up=False
    leftp_down=False
    direction=random.choice([1,-1])
    ydirection=1
    pygame.display.update()
    time.sleep(0.5)
    return ball, leftp, rightp, leftp_up, leftp_down, direction, ydirection

def title_screen():
    screen.fill(black)
    GAME_FONT=pygame.freetype.Font("Roboto-Bold.ttf", 48)
    
    text_surface, rect = GAME_FONT.render("PYNG", white)
    screen.blit(text_surface, (230, 50))
    
    GAME_FONT=pygame.freetype.Font("Roboto-Bold.ttf", 20)

    text_surface, rect = GAME_FONT.render("Pong in Pygame", white)
    screen.blit(text_surface, (220, 105))

    text_surface, rect = GAME_FONT.render("by Fenway Powers", white)
    screen.blit(text_surface, (210, 135))
    
    text_surface, rect = GAME_FONT.render("1 Player", white)
    screen.blit(text_surface, (230, 300))
    
    text_surface, rect = GAME_FONT.render("2 Player", white)
    screen.blit(text_surface, (230, 330))
    
    text_surface, rect = GAME_FONT.render("Exit Game", white)
    screen.blit(text_surface, (230, 360))
    
    arrow = pygame.draw.rect(screen, white, ((150,300),(20,20)))
    return arrow

arrow=pygame.draw.rect(screen, white, ((150,300),(20,20)))

arrow = title_screen()

pygame.display.update()

PVCOM=False
PVP = False
GameOn = False
Train = False

while True:
    clock.tick(60)

    if PVCOM:
        #singleplayer
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    rightp_down=True
                        
                if event.key == pygame.K_UP:
                    rightp_up=True

                if event.key == pygame.K_ESCAPE:
                    PVCOM = False

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    rightp_down=False
                if event.key == pygame.K_UP:
                    rightp_up=False

        if rightp_down == True:
            rightp = movepaddle(rightp,1)
        if rightp_up == True:
            rightp = movepaddle(rightp,-1)
            
        ball, direction, ydirection=ball_move(ball,leftp,rightp,direction,ydirection)

        if ball.x < leftp.x:
            right_score+=1
            ball, leftp, rightp, leftp_up, leftp_down, direction, ydirection = gameover(ball)
        if ball.x > rightp.x:
            left_score+=1
            ball, leftp, rightp, leftp_up, leftp_down, direction, ydirection = gameover(ball)

        leftp = COMmove(ball,leftp)

        text_surface, rect = GAME_FONT.render(str(left_score), white)
        screen.blit(text_surface, (40, 50))
        text_surface, rect = GAME_FONT.render(str(right_score), white)
        screen.blit(text_surface, (530, 50))

        pygame.draw.rect(screen, white, ((rightp.x,rightp.y),(rightp.width,rightp.height)))
        pygame.draw.rect(screen, white, ((leftp.x,leftp.y),(leftp.width,leftp.height)))

        if PVCOM == False:
            left_score = 0
            right_score = 0
            screen.fill(black)
            arrow = title_screen()
            pygame.display.update()
            
    elif PVP:
        #2 Player
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    rightp_down=True
                        
                if event.key == pygame.K_UP:
                    rightp_up=True
                    
                if event.key == pygame.K_s:
                    leftp_down=True
                        
                if event.key == pygame.K_w:
                    leftp_up=True

                if event.key == pygame.K_ESCAPE:
                    PVP = False

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    rightp_down=False
                if event.key == pygame.K_UP:
                    rightp_up=False
                if event.key == pygame.K_s:
                    leftp_down=False
                if event.key == pygame.K_w:
                    leftp_up=False

        if rightp_down == True:
            rightp = movepaddle(rightp,1)
        if rightp_up == True:
            rightp = movepaddle(rightp,-1)
        if leftp_down == True:
            leftp = movepaddle(leftp,1)
        if leftp_up == True:
            leftp = movepaddle(leftp,-1)

        ball, direction, ydirection=ball_move(ball,leftp,rightp,direction,ydirection)

        if ball.x < leftp.x:
            right_score+=1
            ball, leftp, rightp, leftp_up, leftp_down, direction, ydirection = gameover(ball)
        if ball.x > rightp.x:
            left_score+=1
            ball, leftp, rightp, leftp_up, leftp_down, direction, ydirection = gameover(ball)

        text_surface, rect = GAME_FONT.render(str(left_score), white)
        screen.blit(text_surface, (40, 50))
        text_surface, rect = GAME_FONT.render(str(right_score), white)
        screen.blit(text_surface, (530, 50))

        pygame.draw.rect(screen, white, ((rightp.x,rightp.y),(rightp.width,rightp.height)))
        pygame.draw.rect(screen, white, ((leftp.x,leftp.y),(leftp.width,leftp.height)))

        if PVP == False:
            left_score = 0
            right_score = 0
            screen.fill(black)
            arrow = title_screen()
            pygame.display.update()
    else:
        #Title Screen / Menu
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    if arrow.y != 360:
                        arrow=pygame.draw.rect(screen, black, ((150,arrow.y),(20,20)))
                        arrow=pygame.draw.rect(screen, white, ((150,arrow.y+30),(20,20)))

                if event.key == pygame.K_UP:
                    if arrow.y != 300:
                        arrow=pygame.draw.rect(screen, black, ((150,arrow.y),(20,20)))
                        arrow=pygame.draw.rect(screen, white, ((150,arrow.y-30),(20,20)))

                if event.key == pygame.K_RETURN:
                    if arrow.y == 300:
                        PVCOM = True
                        screen.fill(black)
                        ball, leftp, rightp, leftp_up, leftp_down, direction, ydirection = gameover(ball)
                        time.sleep(0.5)
                    if arrow.y == 330:
                        PVP = True
                        screen.fill(black)
                        ball, leftp, rightp, leftp_up, leftp_down, direction, ydirection = gameover(ball)
                        time.sleep(0.5)
                    if arrow.y == 360:
                        pygame.quit()

                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
            
    pygame.display.update()
