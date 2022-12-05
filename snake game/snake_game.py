from food import Food
import time
from turtle import Screen
import turtle
from snake import Snake
from score import Score


def setup():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor('black')
    screen.title("My Snake Game")
    screen.tracer(0)
    screen.listen()
    return screen


screen = setup()

snake = Snake()
food = Food()
score = Score()

def Keys(screen, snake):
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.right, "Right")
    screen.onkey(snake.left, "Left")

Keys(screen, snake)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    #Collision can be detected by using distance method of turtle
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase()
        snake.extend()
    if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 280 or snake.head.ycor() < -290:
        score.reset()
        snake.reset()
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()
        


screen.exitonclick()
