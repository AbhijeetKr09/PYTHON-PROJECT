
from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        self.level = 1
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-250, 250)
        self.update()


    def update(self):
        self.write(f"LEVEL: {self.level}", False, font=FONT)
    

    def scored(self):
        self.level += 1
        self.clear()
        self.update()


    def game_over(self):
        self.goto(0, 0)
        self.write(arg='Game Over',move= False, align='center', font=FONT)
