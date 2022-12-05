from pickle import FALSE
from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Arial", 14, "bold")
MOVE = False

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        with open("snake game/data.txt", mode='r') as data:
            self.high_score = int(data.read())
        self.goto(0, 260)
        self.hideturtle()
        self.color("white")
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f'Score: {self.score } |  High Score: {self.high_score}', move=MOVE, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            with open("snake game/data.txt", mode='w') as data:
                data.write(f"{self.high_score}")
            
        self.score = 0
        self.update_score()


    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg='Game Over', move=MOVE, align=ALIGNMENT, font=FONT)


    def increase(self):
        self.score += 1
        self.update_score()
    