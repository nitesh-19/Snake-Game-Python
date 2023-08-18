from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()

        self.goto(0, 280)
        self.refresh()

    def refresh(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}")
        self.goto(0, 280)
