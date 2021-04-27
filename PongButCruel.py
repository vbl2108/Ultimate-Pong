import turtle
import random

from turtle import *

#screen setup
screen = turtle.Screen()
turtle.title('Extreme Pong: Multiplayer Edition')
turtle.bgcolor('grey')

#score setup
lscore = 0
rscore = 0
score = turtle.Turtle()
score.color = ('black')
score.hideturtle()
score.penup()
score.setposition(-330, 270)
score.pendown()
score.write('Controls: W,S left Paddle | Up,Down right Paddle')
score.penup()
score.setposition(0, 240)
score.pendown()
score.write(str(lscore) + ' |Score| ' + str(rscore), False, align="center", font=('Arial', 25))


#ball setup
ball = turtle.Turtle()
ball.shape('square')
ball.color('white')
ball.penup()

#player setup
rightplayer = turtle.Turtle()
rightplayer.penup()
rightplayer.color('black')
rightplayer.setposition(300, 0)
rightplayer.shape('square')
rightplayer.shapesize(1, 1)


#leftplayer setup
leftplayer = turtle.Turtle()
leftplayer.penup()
leftplayer.color('black')
leftplayer.setposition(-300,0)
leftplayer.shape('square')
leftplayer.shapesize(1, 1)


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

#ball velocity on both axis. Random number between 1 and 5
ball.velx = random.randrange(1, 5)
ball.vely = random.randrange(1, 5)

while 0==0:

    #random number for random things
    posNeg = random.randrange(1, 3)

    #puck movement
    ball.setx (ball.xcor() + ball.velx)
    ball.sety (ball.ycor() + ball.vely)


    #Border collision 
    if ball.ycor() > 280:
        #direction change  
        ball.vely = -2

        #velocity change
        ball.velx = random.randrange(3, 5)
        ball.vely = random.randrange(3, 5)
        ball.vely = ball.vely*-1

    if ball.ycor() < -280:
        ball.vely = 3

        ball.velx = random.randrange(3, 5)
        ball.vely = random.randrange(3, 5)

    if ball.xcor() > 320:
        ball.setposition(0, 0)

        ball.velx = random.randrange(3, 5)
        ball.vely = random.randrange(3, 5)

        #trying to make ball change direction after restart
        if posNeg == 1:

            ball.velx = ball.velx*-1
            ball.vely = ball.vely*-1
        else:
            ball.velx = ball.velx*1
            ball.vely= ball.vely*1

        lscore = lscore+1
        score.clear()
        score.write(str(lscore) + ' |Score| ' + str(rscore), False, align="center", font=('Arial', 25))

    if ball.xcor() < -320:
        ball.setposition(0, 0)

        ball.velx = random.randrange(1, 5)
        ball.vely = random.randrange(1, 5)

        if posNeg == 1:

            ball.velx = ball.velx*-1
            ball.vely = ball.vely*-1
        else:
            ball.velx = ball.velx*1
            ball.vely= ball.vely*1


        rscore = rscore+1
        score.clear()
        score.write(str(lscore) + ' |Score| ' + str(rscore), False, align="center", font=('Arial', 25))

    #Paddle collision
    if ball.distance(rightplayer) <= 10 or ball.distance(leftplayer) <= 10:
        ball.velx = ball.velx*-1
        ball.vely = ball.vely*-1
    #if ball.distance(leftplayer) == 0:
        #ball.velx = ball.velx*-1
        #ball.vely = ball.velx*-1



done()