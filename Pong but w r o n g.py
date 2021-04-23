import turtle
import random

from turtle import *
ready = ('Are you ready?')             #Originally set this as an input var, but got tired of typing yes.
#setting the stage and the circle
if ready == (ready):                   #Originally set as if ready == ('yes')
    screen = turtle.Screen()
    turtle.title('Pong but bad')
    color('black')
    turtle.shape('square')
    puckX = 0
    puckY = 0
    setposition(puckX, puckY)
    turtle.bgcolor('grey')
    turtle.penup()

    #setting up the right player
    rightPlayer = turtle.Turtle()
    rightPlayer.penup()
    rightPlayer.color('black')
    rightPlayer.setposition(300, 0)
    rightPlayer.shape('square')
    rightPlayer.shapesize(4, 1)

    #setting up the robo
    robo = turtle.Turtle()
    robo.penup()
    robo.color('black')
    robo.setposition(-300,0)
    robo.shape('square')
    robo.shapesize(4, 1)
else:
    print('Canceled')





#defining functions for movement (player)
playerX = rightPlayer.xcor()
playerY = rightPlayer.ycor()
def right():
    rightPlayer.forward(50)
def left():
    rightPlayer.back(50)
def down():
    playerY = rightPlayer.ycor()
    playerX = rightPlayer.xcor()
    rightPlayer.setposition(playerX, rightPlayer.ycor-50)
def up():
    playerY = rightPlayer.ycor()
    playerX= rightPlayer.xcor()
    rightPlayer.setposition(playerX, playerY+50)

#functions for moving robo 
def roboDown():
    roboY = ycor()
    roboX = robo.xcor()
    robo.setpositionx, (roboX, roboY-50)
def roboUp():
    roboY = ycor()
    roboX = robo.xcor()
    robo.setposition(roboX, roboY+50)




#calling functions for movements and assigning them to keys. Use WASD to move r e c t a g n l e. 
screen.listen()
screen.onkeypress(up, 'w')
screen.onkeypress(left, 'a')
screen.onkeypress(down, 's')
screen.onkeypress(right, 'd')
screen.onkeypress(roboUp, 'w')
screen.onkeypress(roboUp, 's')

# Got the ball to move back and forth infinitely. So that's cool. 
while 0==0:
    currentBorder = 300
    while puckX < currentBorder:
        puckX = puckX+10
        setx(puckX)
    currentBorder = -300
    while puckX >= currentBorder:
        puckX = puckX-10
        setx(puckX)
    

done()
