import turtle
import random

from turtle import *

#screen setup
screen = turtle.Screen()
screen.setup(width=800, height=600)
turtle.title('Pong but bad')
color('black')
turtle.bgcolor('grey')
turtle.penup()

#ball setup
ball = turtle.Turtle()
ball.shape('square')
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
ballX = 0
ballY = 0
#    currentBorder = 300
#    while ballX < currentBorder:
#        ballX = ballX+10
#        setx(ballX)
#    currentBorder = -300
#    while ballX >= currentBorder:
#        ballX = ballX-10
#        setx(ballX)

velX = 2
velY = 2
true = 1

#game loop
while true == 1:
    ballX = ballX + velX
    ballY = ballY + velY

    #border control
    if -290 < ball.xcor() < 290 and -290 < ball.ycor() <290:
        ball.setx(ballX)
        ball.sety(ballY)
        print("if loop ran")
        
    elif ball.ycor() >= 290:
        velY = velY*-1
        ball.sety(290)
        print("1")

    elif ball.xcor() >= 290:
        velX = velX*-1
        ball.setx(290)
        print("2")

    elif ball.ycor() <= -290:
        velY = velY*-1
        ball.sety(-290)
        print("3")

    elif ball.xcor() <= -290:
        velX = velX*-1
        ball.setx(-290)
        print("4")
    print(str(ball.xcor()))
    

        

#done()
