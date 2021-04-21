import turtle

from turtle import *
ready = input('Are you ready?')
#setting the stage and the circle
if ready == ('yes'):   
    screen = turtle.Screen()
    turtle.title('Pong but bad')
    color('black')
    turtle.shape('circle')
    setposition(0,0)
    turtle.bgcolor('grey')
else:
    print('Canceled')

#defining functions for movement
def right():
    turtle.forward(50)
def left():
    turtle.back(50)
def down():
    y= ycor()
    x= xcor()
    turtle.setposition(x, y-50)
def up():
    y = ycor()
    x= xcor()
    turtle.setposition(x, y+50)

#calling functions for movements and assigning them to keys
screen.listen()
screen.onkeypress(up, 'w')
screen.onkeypress(left, 'a')
screen.onkeypress(down, 's')
screen.onkeypress(right, 'd')


#position = position()
#while position < 290:
#   turtle.forward(10)

done()