import turtle
import random

from turtle import *

#screen setup
screen = turtle.Screen()
turtle.title('Pong but bad')
color('black')
turtle.shape('square')
turtle.bgcolor('grey')
turtle.penup()

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

#ball
puckX = 0
puckY = 0
while 0==0:
    currentBorder = 300
    while puckX < currentBorder:
        puckX = puckX+10
        setx(puckX)
    currentBorder = -300
    while puckX >= currentBorder:
        puckX = puckX-10
        setx(puckX)
    

#done()
