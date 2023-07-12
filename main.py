# turtle
from turtle import Screen
# time for stopping
import time
# importing classes
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")



game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)
    snake.move()


    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.add_score()

     #Detect collision with wall.
    xcor = snake.head.xcor()
    ycor = snake.head.ycor()

    if xcor > 300 or xcor < -300 or ycor > 300 or ycor < -300:
        scoreboard.reset()
        snake.reset()

    #Detect collision with tail.
    for segment in snake.segments[1:]:

        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


screen.exitonclick()





