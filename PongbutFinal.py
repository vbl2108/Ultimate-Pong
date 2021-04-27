# Made in collaboration between Carys Crewse and Vincent LeBaron
# Turtle documentation found here:  https://docs.python.org/3/library/turtle.html#module-turtle
# Random documentation found here: https://docs.python.org/3/library/random.html

import turtle
import random

from turtle import *

#screen setup
screen = turtle.Screen()
turtle.title('Extreme Pong: Multiplayer Edition')
turtle.bgcolor('black')

#score setup
lscore = 0
rscore = 0
score = turtle.Turtle()
score.color = ('black')
score.hideturtle()
score.penup()
score.setposition(-330, 270)
score.pendown()
score.pencolor('yellow')
score.write('Controls: W,S left Paddle | Up,Down right Paddle')
score.penup()
score.setposition(0, 240)
score.pendown()
score.write(str(lscore) + ' |Score| ' + str(rscore), False, align="center", font=('Arial', 25))


#ball setup
ball = turtle.Turtle()
ball.shape('circle')
ball.color('white')
ball.penup()

#rightplayer setup
rightplayer = turtle.Turtle()
rightplayer.penup()
rightplayer.color('purple')
rightplayer.setposition(300, 0)
rightplayer.shape('square')
rightplayer.shapesize(5, 1)


#leftplayer setup
leftplayer = turtle.Turtle()
leftplayer.penup()
leftplayer.color('green')
leftplayer.setposition(-300,0)
leftplayer.shape('square')
leftplayer.shapesize(5, 1)


#move functions
def rightplayerDown():
    ry = rightplayer.ycor()
    ry = ry-20
    rightplayer.sety(ry)

def rightplayerUp():
    ry = rightplayer.ycor()
    ry = ry+20
    rightplayer.sety(ry)

def leftplayerDown():
    ly = leftplayer.ycor()
    ly = ly-20
    leftplayer.sety(ly)

def leftplayerUp():
    ly = leftplayer.ycor()
    ly = ly+20
    leftplayer.sety(ly)

#key bindings 
screen.listen()
screen.onkeypress(leftplayerUp, 'w')
screen.onkeypress(leftplayerDown, 's')

screen.onkeypress(rightplayerUp, 'Up')
screen.onkeypress(rightplayerDown, 'Down')

#ball velocity on both axis. Random number between 6 and 8
ball.velx = random.randrange(6, 8)
ball.vely = random.randrange(6, 8)

while 0==0:

    #ball movement
    ball.setx (ball.xcor() + ball.velx)
    ball.sety (ball.ycor() + ball.vely)


    #Border collision 
    if ball.ycor() > 280:
        #velocity change

        ball.vely = random.randrange(6, 8)
        ball.vely = ball.vely*-1
        ball.velx = ball.velx*1

    if ball.ycor() < -280:

        ball.vely = random.randrange(6, 8)
        ball.vely = ball.vely*1
        ball.velx = ball.velx*1

    if ball.xcor() > 320:
        ball.setposition(0, 0)

        ball.velx = random.randrange(6, 8)
        ball.vely = random.randrange(6, 8)

        lscore = lscore+1
        score.clear()
        score.write(str(lscore) + ' |Score| ' + str(rscore), False, align="center", font=('Arial', 25))

    if ball.xcor() < -320:
        ball.setposition(0, 0)

        ball.velx = random.randrange(6, 8)
        ball.vely = random.randrange(6, 8)

        rscore = rscore+1
        score.clear()
        score.write(str(lscore) + ' |Score| ' + str(rscore), False, align="center", font=('Arial', 25))

        

    #Paddle collision
    def collideTrue():
        ball.ycor() >= (rightplayer.ycor() - 45) and ball.ycor() <= (rightplayer.ycor() + 45)

    if ball.xcor() >= 300 and ball.ycor() >= (rightplayer.ycor() - 45) and ball.ycor() <= (rightplayer.ycor() + 45):
        ball.velx = ball.velx *-1

    if ball.xcor() <= -300 and ball.ycor() >= (leftplayer.ycor() - 45) and ball.ycor() <= (leftplayer.ycor() + 45):
        ball.velx = ball.velx *-1

    




done()