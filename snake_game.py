from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")  # Set the game background color
screen.title("Snake Game")
screen.tracer(0)

python = Snake(3)
food = Food()
screen.update()
scoreboard = Scoreboard()

game_on = True
screen.listen()
screen.onkeypress(fun=python.up, key="Up")
screen.onkeypress(fun=python.left, key="Left")
screen.onkeypress(fun=python.right, key="Right")
screen.onkeypress(fun=python.down, key="Down")
while game_on:
    # Move the snake and change its heading when respective keys are pressed
    python.move_body()
    time.sleep(0.1)
    if python.head.distance(food) <= 10:
        food.spawn_again()
        python.grow_snake()
        # time.sleep(0.1)

        screen.update()

        scoreboard.refresh()
    if python.head.xcor() > 280 or python.head.xcor() < -280 or python.head.ycor() > 280 or python.head.ycor() < -280:
        scoreboard.game_over()

        game_on = False

    # Detect collision with tail.
    for segment in python.segments[1:]:
        screen.update()

        if python.head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()

screen.update()
screen.exitonclick()
