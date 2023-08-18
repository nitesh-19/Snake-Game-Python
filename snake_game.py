from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
segments = []


def up():

    if segments[0].heading() == 270:
        pass
    else:
        segments[0].setheading(90)


def left():
    segments[0].setheading(180)


def right():
    segments[0].setheading(0)


def down():
    segments[0].setheading(270)


def move_body():
    prev_coordinates = []
    for obj in segments:
        prev_coordinates.append((obj.xcor(), obj.ycor()))
    segments[0].forward(20)
    for i in range(0, len(segments) - 1):
        segments[i + 1].goto(prev_coordinates[i])
        # screen.update()


number_of_turtles = 5
for _ in range(0, number_of_turtles):
    new_turtle = Turtle(shape="square")
    new_turtle.color("white")
    new_turtle.penup()
    segments.append(new_turtle)
segments[1].color("green")
segments[2].color("blue")

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
