import turtle
from turtle import Screen
import time
import food
from Day20.scoreboard import ScoreBoard

from Day20.snake import Snake

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)
game_is_on = True
turtle.color("white")
turtle.hideturtle()
snake = Snake()
food =food.Food()
screen.listen()
score = ScoreBoard()

screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)
while game_is_on:
    screen.update()
    time.sleep(0.1)
    score.show_score()
    snake.move()


    #detect collision with food
    if snake.snake_head.distance(food)<15:
        food.refresh()
        score.increase_score()
        snake.extend()


    # detect collision with wall
    if snake.snake_head.xcor() < -290 or snake.snake_head.xcor() > 290 or snake.snake_head.ycor() < -290 or snake.snake_head.ycor ()>290:
        score.reset()
        snake.reset()


    #detect collision with body
    for segment in snake.segments[1:]:

        # if segment == snake.snake_head:
        #     pass
        #
        # elif snake.snake_head.distance(segment)<10:
        #     game_is_on =False
        #     turtle.write("Game Over.", align="center", font=("Arial", 24, "normal"))


    # first is using conditional checking, under is checking using slicing
        if snake.snake_head.distance(segment) < 10:
            score.reset()
            snake.reset()


screen.exitonclick()