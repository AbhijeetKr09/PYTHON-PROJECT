
from turtle import Turtle, Screen
import random
import turtle

screen = Screen()
kim = Turtle()
kim.color("purple")
turtle.colormode(255)
kim.speed(0)
kim.penup()
kim.hideturtle()


rgb_colour = [
    (139, 168, 195), (206, 154, 121), (192, 140, 150), 
    (25, 36, 55), (58, 105, 140), (145, 178, 162), 
    (151, 68, 58), (137, 68, 76), (229, 212, 107), 
    (47, 36, 41), (145, 29, 36), (28, 53, 47), 
    (55, 108, 89), (228, 167, 173), (189, 99, 107), 
    (139, 33, 28), (194, 92, 79), (49, 40, 36), 
    (228, 173, 166), (20, 92, 69), (177, 189, 212), 
    (29, 62, 107), (113, 123, 155), (172, 202, 190), 
    (51, 149, 193), (166, 200, 213)
]

kim.setheading(225)
kim.forward(300)
kim.setheading(0)
x = kim.xcor()
y = kim.ycor()
for _ in range(10):
    kim.setx(x)
    kim.sety(y)
    for _ in range(10):
        kim.dot(20, random.choice(rgb_colour))
        kim.fd(50)
    
    y+=50




screen.exitonclick()


