from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(position)

    # Duplicate paddle for screen wrapping
        self.wrap_paddle = Turtle()
        self.wrap_paddle.shape('square')
        self.wrap_paddle.color('white')
        self.wrap_paddle.shapesize(stretch_wid=1, stretch_len=5)
        self.wrap_paddle.penup()
        self.wrap_paddle.hideturtle()

    def update_wrap(self):
        x = self.xcor()
        y = self.ycor()

        # Paddle going through the RIGHT edge
        if x > 350:
            self.wrap_paddle.goto(x - 800, y)
            self.wrap_paddle.showturtle()

        # Paddle going through the LEFT edge
        elif x < -350:
            self.wrap_paddle.goto(x + 800, y)
            self.wrap_paddle.showturtle()

        else:
            self.wrap_paddle.hideturtle()

    def go_left(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())
        self.update_wrap()

    def go_right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())
        self.update_wrap()