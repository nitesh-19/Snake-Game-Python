from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()

        self.goto(0, 280)
        self.refresh(0)

    def refresh(self, score):
        self.clear()
        self.write(f"Score: {score}")
        self.goto(0, 280)
