from turtle import Turtle
import turtle


class Paddle(Turtle):
    def __init__(self, cords):
        super().__init__()
        self.cords = cords
        self.shape('square')
        self.shapesize(5, 1)
        self.color("white")
        self.penup()
        self.goto(self.cords)
    

    def up(self):

        y_cor = self.ycor() + 20
        self.goto(self.xcor(), y_cor)


    def down(self):

        y_cor = self.ycor() - 20
        self.goto(self.xcor(), y_cor)