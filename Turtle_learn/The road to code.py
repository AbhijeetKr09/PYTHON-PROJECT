import turtle as t
from turtle import Turtle, Screen
tom = Turtle()
screen = Screen()

screen.listen()

tom.lt(90)

def move_forward():
    tom.forward(5)


def move_right():
    tom.rt(5)


def move_left():
    tom.lt(5)


def move_back():
    tom.backward(5)


def clear():
    tom.clear()
    tom.penup()
    tom.home()
    tom.pendown()
    

screen.onkeypress(key = 'd', fun = move_right)
screen.onkeypress(key = 'a', fun = move_left)
screen.onkeypress(key = 's', fun = move_back)
screen.onkeypress(key = 'w', fun = move_forward)
screen.onkey(key = "c", fun = clear)



screen.exitonclick()
