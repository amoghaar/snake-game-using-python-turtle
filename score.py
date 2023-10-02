from turtle import Turtle
from food import Food


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.scored_points = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(x=0, y=270)
        self.update_sore()

    def update_sore(self):
        self.write(f"score: {self.scored_points}", align="center", font=("Arial", 15, "normal"))

    def increase_score(self):
        self.scored_points += 1
        self.clear()
        self.update_sore()
        self.write(f"score: {self.scored_points}", align="center", font=("Arial", 15, "normal"))

    def game_over(self):
        self.clear()
        self.goto(x=0, y=0)
        self.write("Game Over", align="center", font=("Arial", 25, "normal"))
        self.goto(x=0, y=-20)
        self.write(f"score: {self.scored_points}", align="center", font=("Arial", 15, "normal"))
