from turtle import Turtle


class Snake:
    def __init__(self):
        self.segments = []
        number_of_snake_segments = 5  # Set the length of the snake at game start
        # Create the snake segments
        for _ in range(0, number_of_snake_segments):
            snake_segment = Turtle(shape="square")
            snake_segment.color("white")
            snake_segment.penup()
            self.segments.append(snake_segment)

        # Place snake at starting position
        for index in range(0, len(self.segments)):
            self.segments[index].setpos((-index * 20, 0))

    # Key press methods to change the direction of the snake's heading
    def up(self):
        if self.segments[0].heading() == 270:
            pass
        else:
            self.segments[0].setheading(90)

    def left(self):
        if self.segments[0].heading() == 0:
            pass
        else:
            self.segments[0].setheading(180)

    def right(self):
        if self.segments[0].heading() == 180:
            pass
        else:
            self.segments[0].setheading(0)

    def down(self):
        if self.segments[0].heading() == 90:
            pass
        else:
            self.segments[0].setheading(270)

    # Continuously moves the head and makes the rest of the body follow it
    def move_body(self):
        prev_coordinates = []
        for obj in self.segments:
            prev_coordinates.append((obj.xcor(), obj.ycor()))
        self.segments[0].forward(20)
        for i in range(0, len(self.segments) - 1):
            self.segments[i + 1].goto(prev_coordinates[i])
