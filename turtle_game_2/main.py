import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car = CarManager()
score = Scoreboard()


def keys(player, screen):
    screen.onkey(player.up, "Up")


keys(player, screen)

game_is_on = True
while game_is_on:

    time.sleep(0.1)
    screen.update()
    car.move()
    car.create_car()

    for cars in car.cars:
        if cars.distance(player) < 20:
            score.game_over()
            game_is_on = False
        
    if player.ycor() == 280:
        score.scored()
        car.increase()
    player.check_finish()


screen.exitonclick()
