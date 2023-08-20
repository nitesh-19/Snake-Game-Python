from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        self.penup()
        self.color("white")
        self.hideturtle()
        with open("data.txt", "r") as file:
            self.highscore = int(file.read())
        self.goto(0, 280)
        self.refresh()

    def refresh(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align="center")
        if self.score > self.highscore:
            self.highscore = self.score
        self.goto(0, 280)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center")
        with open("data.txt", "w") as file:
            file.write(str(self.highscore))
