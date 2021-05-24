import pygame, random, time
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
leftp = pygame.draw.rect(screen, white, ((5,300),(15,120)))
rightp = pygame.draw.rect(screen, white, ((580,0),(15,600)))
leftp_up=False
leftp_down=False
direction=1
ydirection=1

def movepaddle(paddle,downorup):
    increment=12.5
    newpaddle = paddle
    newy = paddle.y+(increment*downorup)
    pygame.draw.rect(screen, black, ((paddle.x,paddle.y),(15,120)))
    pygame.display.update()
    newpaddle = pygame.draw.rect(screen, white, ((paddle.x,newy),(15,120)))
    if newpaddle.y > 480:
        newpaddle = paddle
    return newpaddle

def ball_move(ball,leftp,rightp,direction,ydirection):
    
    if (ball.y in range(leftp.y-40,leftp.y + leftp.height+20) and ball.x == leftp.x) or (ball.y in range(rightp.y-40,rightp.y + rightp.height+20) and ball.x == (rightp.x-20)):
        direction*=-1
    newx=(ball.x)+(5*direction)

    if ball.y in range(leftp.y-40,leftp.y + int((0.5*leftp.height)+20)) and ball.x == leftp.x:
        print("up")


    
    pygame.draw.rect(screen, black, ((ball.x,ball.y),(40,40)))
    pygame.display.update()
    newball = pygame.draw.rect(screen, white, ((newx,ball.y),(40,40)))
    return newball, direction, ydirection

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
     
    pygame.display.update()
