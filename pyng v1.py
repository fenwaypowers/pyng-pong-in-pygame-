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
ball = pygame.draw.rect(screen, white, ((275,275),(40,40)))
leftp = pygame.draw.rect(screen, white, ((5,220),(15,120)))
rightp = pygame.draw.rect(screen, white, ((580,0),(15,600)))
leftp_up=False
leftp_down=False
direction=1
ydirection=random.choice([1,-1])

left_score=0
right_score=0

GAME_FONT = pygame.freetype.Font("Roboto-Bold.ttf", 48)
text_surface, rect = GAME_FONT.render("Hello World!", white)
screen.blit(text_surface, (40, 250))



def movepaddle(paddle,downorup):
    increment=12.5
    newpaddle = paddle
    newy = paddle.y+(increment*downorup)
    pygame.draw.rect(screen, black, ((paddle.x,paddle.y),(15,120)))
    pygame.display.update()
    if newy > 490:
        newpaddle = paddle
    else:
        newpaddle = pygame.draw.rect(screen, white, ((paddle.x,newy),(15,120)))
    return newpaddle

def ball_move(ball,leftp,rightp,direction,ydirection):
    increment=5
    
    if (ball.y in range(leftp.y-40,leftp.y + leftp.height+20) and ball.x == leftp.x or ball.x > leftp.x and ball.x < (leftp.x+5)) or (ball.y in range(rightp.y-40,rightp.y + rightp.height+20) and ball.x == (rightp.x-20)):
        direction*=-1
    newx=(ball.x)+(increment*direction)

    if ball.y in range(leftp.y-40,leftp.y + int((0.5*leftp.height))) and ball.x == leftp.x:
        ydirection=-1
    elif ball.y in range(int(1.5*(leftp.y-40)),leftp.y+leftp.height) and ball.x == leftp.x:
        ydirection=1

    if ball.y in range(rightp.y-40,rightp.y + int((0.5*rightp.height))) and ball.x == rightp.x:
        ydirection=-1
    elif ball.y in range(int(1.5*(rightp.y-40)),rightp.y+rightp.height) and ball.x == rightp.x:
        ydirection=1

    if ball.y == 560 or ball.y == 0:
        ydirection*=-1

    newy=ball.y+((increment)*ydirection)

    pygame.draw.rect(screen, black, ((ball.x,ball.y),(40,40)))
    pygame.display.update()
    newball = pygame.draw.rect(screen, white, ((newx,newy),(40,40)))
    return newball, direction, ydirection

def gameover():
    time.sleep(0.5)
    screen.fill(black)
    ball = pygame.draw.rect(screen, white, ((275,275),(40,40)))
    leftp = pygame.draw.rect(screen, white, ((5,300),(15,120)))
    rightp = pygame.draw.rect(screen, white, ((580,0),(15,600)))
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

    pygame.draw.rect(screen, white, ((580,rightp.y),(15,600)))
    pygame.draw.rect(screen, white, ((leftp.x,leftp.y),(15,120)))

    if ball.x < leftp.x:
        right_score+=1
        ball, leftp, rightp, leftp_up, leftp_down, direction, ydirection = gameover()
    if ball.x > rightp.x:
        ball, leftp, rightp, leftp_up, leftp_down, direction, ydirection = gameover()
     
    pygame.display.update()
