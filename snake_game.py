from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
segments = []


# Key press methods to change the direction of the snake's heading
def up():
    if segments[0].heading() == 270:
        pass
    else:
        segments[0].setheading(90)


def left():
    if segments[0].heading() == 0:
        pass
    else:
        segments[0].setheading(180)


def right():
    if segments[0].heading() == 180:
        pass
    else:
        segments[0].setheading(0)


def down():
    if segments[0].heading() == 90:
        pass
    else:
        segments[0].setheading(270)


# Continuously moves the head and makes the rest of the body follow it
def move_body():
    prev_coordinates = []
    for obj in segments:
        prev_coordinates.append((obj.xcor(), obj.ycor()))
    segments[0].forward(20)
    for i in range(0, len(segments) - 1):
        segments[i + 1].goto(prev_coordinates[i])


number_of_snake_segments = 5  # Set the length of the snake at game start

# Create the snake segments
for _ in range(0, number_of_snake_segments):
    snake_segment = Turtle(shape="square")
    snake_segment.color("white")
    snake_segment.penup()
    segments.append(snake_segment)

# Place snake at starting position
for index in range(0, len(segments)):
    segments[index].setpos((-index * 20, 0))
    screen.update()

game_on = True
screen.listen()
while game_on:
    move_body()
    screen.onkeypress(fun=up, key="Up")
    screen.onkeypress(fun=left, key="Left")
    screen.onkeypress(fun=right, key="Right")
    screen.onkeypress(fun=down, key="Down")
    time.sleep(0.08)
    screen.update()
screen.exitonclick()
