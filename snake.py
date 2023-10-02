from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.ammu_the_snakes = []
        self.snake_position = 0
        self.creating_snakes()

    def creating_snakes(self):
        for i in range(3):
            self.add_segment()

    def add_segment(self):
        ammu = Turtle(shape="square")
        ammu.color("white")
        ammu.penup()
        ammu.goto(x=self.snake_position, y=0)
        self.snake_position -= 20
        self.ammu_the_snakes.append(ammu)

    def extend(self):
        self.add_segment()

    def move(self):
        for i in range((len(self.ammu_the_snakes) - 1), 0, -1):
            new_x_coordinate = self.ammu_the_snakes[i - 1].xcor()
            new_y_coordinate = self.ammu_the_snakes[i - 1].ycor()
            self.ammu_the_snakes[i].goto(new_x_coordinate, new_y_coordinate)

        self.ammu_the_snakes[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.ammu_the_snakes[0].heading() != DOWN:
            self.ammu_the_snakes[0].setheading(UP)

    def down(self):
        if self.ammu_the_snakes[0].heading() != UP:
            self.ammu_the_snakes[0].setheading(DOWN)

    def left(self):
        if self.ammu_the_snakes[0].heading() != RIGHT:
            self.ammu_the_snakes[0].setheading(LEFT)

    def right(self):
        if self.ammu_the_snakes[0].heading() != LEFT:
            self.ammu_the_snakes[0].setheading(RIGHT)
