from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")  # Set the game background color
screen.title("Snake Game")
screen.tracer(0)

python = Snake(3)
food = Food()
screen.update()

game_on = True
screen.listen()
while game_on:
    # Move the snake and change its heading when respective keys are pressed
    python.move_body()
    screen.onkeypress(fun=python.up, key="Up")
    screen.onkeypress(fun=python.left, key="Left")
    screen.onkeypress(fun=python.right, key="Right")
    screen.onkeypress(fun=python.down, key="Down")
    time.sleep(0.1)
    screen.update()
screen.exitonclick()
