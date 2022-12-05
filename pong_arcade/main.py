
import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


def setup():
    screen = Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    screen.title('Pong Game')
    screen.listen()
    screen.tracer(0)
    return screen


screen = setup()
paddle_r = Paddle((350, 0))
paddle_l = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


def key_for_paddle_1(screen, paddle_r, paddle_l):
    screen.onkeypress(paddle_r.up, "Up")
    screen.onkeypress(paddle_r.down, "Down")
    screen.onkeypress(paddle_l.up, "w")
    screen.onkeypress(paddle_l.down, "s")


key_for_paddle_1(screen, paddle_r, paddle_l)


def playground_setup():
    border = Turtle()
    border.color('black')
    border.pencolor('white')
    border.speed(6)
    border.penup()
    border.goto(0, -300)
    border.setheading(90)
    return border


border = playground_setup()


def draw(border):
    border.pendown()
    border.fd(10)
    border.penup()
    border.fd(10)


for _ in range(600):
    draw(border)

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(paddle_r) < 50 and ball.xcor() > 320 or ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 400:
        ball.reset_ball()
        scoreboard.l_point()
        

    if ball.xcor() < -400:
        ball.reset_ball()
        scoreboard.r_point()


screen.exitonclick()
