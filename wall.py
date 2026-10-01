from turtle import Turtle
import random

class Wall(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.goto(position)

        colors = {
            "red": 200,
            "orange": 350,
            "yellow": 100,
            "green": 500,
            "blue": 425
        }
        self.wall_color = random.choice(list(colors.keys()))
        self.points = colors[self.wall_color]
        self.fillcolor(self.wall_color)

