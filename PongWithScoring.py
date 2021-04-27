import turtle
import random

from turtle import *

#screen setup
screen = turtle.Screen()
turtle.title('Pong but bad')
turtle.bgcolor('grey')

#score setup
ls = 0
rs = 0
score = turtle.Turtle()
score.color = ('black')
score.hideturtle()
score.penup()
score.setposition(0, 240)
score.pendown()
score.write(str(ls) + ' |Score| ' + str(rs), False, align="center", font=('Arial', 25))


#ball setup
ball = turtle.Turtle()
ball.shape('square')
ball.penup()

#player setup
player = turtle.Turtle()
player.penup()
player.color('black')
player.setposition(300, 0)
player.shape('square')
player.shapesize(4, 1)

#robo setup
robo = turtle.Turtle()
robo.penup()
robo.color('black')
robo.setposition(-300,0)
robo.shape('square')
robo.shapesize(4, 1)


#move functions
def playerDown():
    py = player.ycor()
    py = py-50
    player.sety(py)

def playerUp():
    py = player.ycor()
    py = py+50
    player.sety(py)

def roboDown():
    ry = robo.ycor()
    ry = ry-50
    robo.sety(ry)

def roboUp():
    ry = robo.ycor()
    ry = ry+50
    robo.sety(ry)

#key bindings 
screen.listen()
screen.onkeypress(playerUp, 'w')
screen.onkeypress(playerDown, 's')

screen.onkeypress(roboUp, 'Up')
screen.onkeypress(roboDown, 'Down')

#ball velocity on both axis. Random number between 1 and 5
ball.velx = random.randrange(1, 5)
ball.vely = random.randrange(1, 5)

while 0==0:

    #puck movement
    ball.setx (ball.xcor() + ball.velx)
    ball.sety (ball.ycor() + ball.vely)


    #Border collision 
    if ball.ycor() > 280:
        #direction change
        ball.velx = ball.velx*1
        ball.vely = ball.vely*-1

        #velocity change
        ball.velx = random.randrange(1, 5)
        ball.vely = random.randrange(1, 5)

    if ball.ycor() < -280:
        ball.velx = ball.velx*1
        ball.vely = ball.vely*-1

        ball.velx = random.randrange(1, 5)
        ball.vely = random.randrange(1, 5)

    if ball.xcor() > 320:
        ball.setposition(0, 0)
        ball.velx = ball.velx*-1
        ball.vely = ball.vely*-1

        ball.velx = random.randrange(1, 5)
        ball.vely = random.randrange(1, 5)

        ls = ls+1
        score.clear()
        score.write(str(ls) + ' |Score| ' + str(rs), False, align="center", font=('Arial', 25))

    if ball.xcor() < -320:
        ball.setposition(0, 0)
        ball.velx = ball.velx*-1
        ball.vely = ball.vely*-1

        ball.velx = random.randrange(1, 5)
        ball.vely = random.randrange(1, 5)

        rs = rs+1
        score.clear()
        score.write(str(ls) + ' |Score| ' + str(rs), False, align="center", font=('Arial', 25))

    #Paddle collision
    if ball.distance(player) == 0 or ball.distance(robo) == 0:
        ball.velx = ball.velx*-1
        ball.vely = ball.vely*-1
    if ball.distance(robo) == 0:
        ball.velx = ball.velx*-1
        ball.vely = ball.velx*-1


done()