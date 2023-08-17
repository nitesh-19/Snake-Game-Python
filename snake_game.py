from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
segments = []


def up():
    segments[0].setheading(90)
    segments[0].forward(20)
    move_body(segments)
    screen.update()


def move_body():
    for i in range(1, len(segments) - 1):
        x_pos = segments[-i - 1].xcor()
        y_pos = segments[-i - 1].ycor()
        segments[-i].goto(x_pos, y_pos)
        segments[0].forward(20)


for _ in range(0, 3):
    new_turtle = Turtle(shape="square")
    new_turtle.color("white")
    new_turtle.penup()
    # new_turtle.speed("slowest")
    segments.append(new_turtle)

for index in range(0, len(segments)):
    segments[index].setpos((-index * 20, 0))
screen.update()
game_is_on = True
last_position = []
screen.listen()
while game_is_on:
    # screen.onkeypress(fun=up, key="Up")

    move_body()
    # time.sleep(0.08)

    screen.update()

screen.exitonclick()
