from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.lt(90)
        self.goto(STARTING_POSITION)



    def up(self):
        y_cor = self.ycor() + MOVE_DISTANCE
        self.goto(0, y_cor)


    def check_finish(self):
        if self.ycor() == FINISH_LINE_Y:
            self.goto(STARTING_POSITION)

