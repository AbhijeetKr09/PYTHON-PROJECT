import random
from turtle import Turtle


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.cars = []
        self.move_speed = STARTING_MOVE_DISTANCE



    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            y_cor = random.randint(-200, 230)
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(300, y_cor)
            self.cars.append(new_car)



    def move(self):
        for car in self.cars:
            car.backward(self.move_speed)
    

    def increase(self):
        self.move_speed += MOVE_INCREMENT
            
    

        