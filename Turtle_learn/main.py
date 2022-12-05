
import random
from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=500, height=400)

is_race_on = False

user_bet = screen.textinput(
    title="Make your bet.", prompt="Which colour will win the race? Enter the color: ")

colours = ["red", "blue", "green", "orange", "yellow", "purple"]
location = [-70, -40, -10, 20, 50, 80]
all_turtle = []

for number in range(6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.speed(2)
    new_turtle.color(colours[number])
    new_turtle.penup()
    new_turtle.goto(-230, location[number])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtle:

        if turtle.xcor() > 230:
            winner = turtle.pencolor()
            is_race_on = False

            if winner == user_bet:
                print(f"You've won! {winner} turtle is winner.")
            else:
                print(f"You've lost! {winner} turtle is winner.")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)


screen.exitonclick()
