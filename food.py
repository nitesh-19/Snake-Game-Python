from turtle import Turtle
from random import randrange


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("green")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.speed("fastest")
        self.goto(randrange(-280, 280, 10), randrange(-280, 280, 10))
