from turtle import Turtle
from random import randint


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")

    def refresh(self):
        random_x = randint(0, 298)
        random_y = randint(0, 298)
        self.goto(x=random_x, y=random_y)
        self.speed(0)
