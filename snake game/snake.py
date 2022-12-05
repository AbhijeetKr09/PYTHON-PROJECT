from turtle import Turtle


def Movement_direction():
    START = [(0, 0), (-20, 0), (-40, 0)]
    UP = 90
    DOWN = 270
    RIGHT = 0
    LEFT = 180
    return START, UP, DOWN, RIGHT, LEFT

START, UP, DOWN, RIGHT, LEFT = Movement_direction()


class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.segments = []
        self.create_body()
        self.head = self.segments[0]

    def create_body(self):
        for position in START:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape='square')
        new_segment.penup()
        new_segment.color('white')
        new_segment.goto(position)
        self.segments.append(new_segment)


    def extend(self):
        self.add_segment(self.segments[-1].position())


    def move(self):
        segment = self.segments
        for seg_num in range(len(segment) - 1, 0, -1):
            new_x = segment[seg_num - 1].xcor()
            new_y = segment[seg_num - 1].ycor()
            segment[seg_num].goto(new_x, new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)

    def reset(self):
        for segment in self.segments:
            segment.reset()
        self.segments.clear()
        self.create_body()
        self.head = self.segments[0]