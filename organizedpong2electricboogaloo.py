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
while 0==0:
    rightBorder = 300
    while puckX < rightBorder:
        ball.right(45)
        ball.forward(10)
    leftBorder = -300
    while puckX >= leftBorder:
        ball.back(10)
    

#done()