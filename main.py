from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # collision with food
    if snake.ammu_the_snakes[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()
        screen.update()

    #
    # collision with wall
    if snake.ammu_the_snakes[0].xcor() > 280 or snake.ammu_the_snakes[0].ycor() > 300 or snake.ammu_the_snakes[
       0].xcor() < -300 or snake.ammu_the_snakes[0].ycor() < -300:
        game_is_on = False

    for segment in snake.ammu_the_snakes[1:]:
        if snake.ammu_the_snakes[0].distance(segment) < 10:
            game_is_on = False
            score.game_over()

score.game_over()
screen.exitonclick()
