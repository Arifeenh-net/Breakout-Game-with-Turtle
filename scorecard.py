from turtle import Turtle
class Scorecard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_scorecard()

    def update_scorecard(self):
        self.clear()
        self.goto(0, 250)
        self.write(f"Score:{self.score}", align="center", font=("courier", 30, "normal"))

    def point(self, points):
        self.score += points
        self.update_scorecard()
    def score_reset(self):
        self.score = 0
        self.update_scorecard()