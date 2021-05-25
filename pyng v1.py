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
clock = pygame.time.Clock()
ball = pygame.draw.rect(screen, white, ((275,random.randint(50,550)),(40,40)))
leftp = pygame.draw.rect(screen, white, ((5,220),(15,60)))
rightp = pygame.draw.rect(screen, white, ((580,220),(15,60)))
leftp_up=False
leftp_down=False
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
    
    if (ball.y in range(leftp.y-30,leftp.y + leftp.height+10) and ball.x == leftp.x or ball.x > leftp.x and ball.x < (leftp.x+5)) or (ball.y in range(rightp.y-30,rightp.y + rightp.height+10) and ball.x == (rightp.x-20)):
        direction*=-1
    newx=(ball.x)+(increment*direction)

    if ball.y in range(leftp.y-30,leftp.y + int((0.5*leftp.height))) and ball.x == leftp.x:
        ydirection=-1
    elif ball.y in range(int(1.5*(leftp.y-20)),leftp.y+leftp.height) and ball.x == leftp.x:
        ydirection=1

    if ball.y in range(rightp.y-30,rightp.y + int((0.5*rightp.height))) and ball.x == rightp.x:
        ydirection=-1
    elif ball.y in range(int(1.5*(rightp.y-20)),rightp.y+rightp.height) and ball.x == rightp.x:
        ydirection=1

    if ball.y > 560 or ball.y < 1:
        ydirection*=-1

    newy=ball.y+((yincrement)*ydirection)

    pygame.draw.rect(screen, black, ((ball.x,ball.y),(ball.width,ball.height)))
    newball = pygame.draw.rect(screen, white, ((newx,newy),(ball.width,ball.height)))
    return newball, direction, ydirection

def gameover():
    time.sleep(0.5)
    screen.fill(black)
    ball = pygame.draw.rect(screen, white, ((275,random.randint(50,550)),(40,40)))
    leftp = pygame.draw.rect(screen, white, ((5,220),(15,60)))
    rightp = pygame.draw.rect(screen, white, ((580,220),(15,60)))
    leftp_up=False
    leftp_down=False
    direction=1
    ydirection=1
    time.sleep(0.5)
    return ball, leftp, rightp, leftp_up, leftp_down, direction, ydirection

pygame.display.update()

time.sleep(1)

while True:
    
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                leftp_down=True
                
            if event.key == pygame.K_UP:
                leftp_up=True

            if event.key == pygame.K_ESCAPE:
                pygame.quit()

        if event.type == pygame.KEYUP:
            leftp_up=False
            leftp_down=False

    if leftp_down == True:
        leftp = movepaddle(leftp,1)
    if leftp_up == True:
        leftp = movepaddle(leftp,-1)

    ball, direction, ydirection=ball_move(ball,leftp,rightp,direction,ydirection)

    if ball.x < leftp.x:
        right_score+=1
        ball, leftp, rightp, leftp_up, leftp_down, direction, ydirection = gameover()
    if ball.x > rightp.x:
        left_score+=1
        ball, leftp, rightp, leftp_up, leftp_down, direction, ydirection = gameover()

    rightp = COMmove(ball,rightp)

    text_surface, rect = GAME_FONT.render(str(left_score), white)
    screen.blit(text_surface, (40, 50))
    text_surface, rect = GAME_FONT.render(str(right_score), white)
    screen.blit(text_surface, (530, 50))


    pygame.draw.rect(screen, white, ((rightp.x,rightp.y),(rightp.width,rightp.height)))
    pygame.draw.rect(screen, white, ((leftp.x,leftp.y),(leftp.width,leftp.height)))
    pygame.display.update()
