import turtle
import random

from turtle import *

#screen setup
screen = turtle.Screen()
turtle.title('Pong but bad')
turtle.bgcolor('grey')

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

#global variables
py = player.ycor()
px = player.xcor()
ry = player.ycor()
rx = robo.xcor()

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

#ball
puckX = ball.xcor()
puckY = ball.ycor()
print (ball.distance(player))

#ball velocity on both axis. I want to change these to random numbers in the future. 
ball.velx = 3
ball.vely = 2

while 0==0:

    #puck movement
    ball.setx (ball.xcor() + ball.velx)
    ball.sety (ball.ycor() + ball.vely)

    #Border collision 
    if ball.ycor() > 280:
        ball.velx = -2
        ball.vely = -2
    if ball.ycor() < -280:
        ball.velx = +2
        ball.vely = +2
    if ball.xcor() > 280:
        ball.velx = -2
        ball.vely = 2
    if ball.xcor() < -280:
        ball.velx = 2
        ball.vely = -2

    #Paddle collision
    if ball.distance(player) == 0:
        ball.velx = -2
        ball.vely = -2
    if ball.distance(robo) == 0:
        ball.velx = 2
        ball.vely = 2


#done()