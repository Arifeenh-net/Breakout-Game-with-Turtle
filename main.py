from turtle import Screen
import time
from paddle import Paddle
from wall import Wall
from ball import Ball
from scorecard import Scorecard
from over import Over


# Setting up the screen

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title("Breakout")
screen.tracer(0)

# Setting up the paddle
paddle = Paddle((0, -250))

# Setting up the brick walls
walls = []
for y in range(230, 80, -25):
   for x in range(-365, 361, 45):
       walls.append(Wall((x, y)))

# Setting up the ball
ball = Ball((0, -110))


# Scorecard
scorecard = Scorecard()

# Making the paddle move using arrow keys
screen.listen()
screen.onkey(paddle.go_left, "Left")
screen.onkey(paddle.go_right, "Right")

# Game over function
over = Over()

game_is_on= True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
#     Ball wall collision
    for wall in walls:
        if (wall.xcor() - 30 < ball.xcor() < wall.xcor() + 30
                and wall.ycor() - 20 < ball.ycor() < wall.ycor() + 20):
            ball.bounce_y()
            scorecard.point(wall.points)
            wall.hideturtle()
            walls.remove(wall)
            break

#     Collision with sides
    if ball.xcor() > 360 or ball.xcor() < -360:
        ball.bounce_x()
#       Ball Collision with the paddle
    if ball.distance(paddle) < 50 and ball.ycor() < -225:
        ball.bounce_y()
        ball.sety(-230)

#     Game over logic
    if ball.ycor() < -300:
        over.game_over()
        screen.update()

        time.sleep(2)

        # reset everything
        ball.goto(0, -110)
        ball.x_move = 10
        ball.y_move = 10

        paddle.goto(0, -250)

        for wall in walls:
            wall.hideturtle()

        walls.clear()

        for y in range(230, 80, -25):
            for x in range(-365, 361, 45):
                walls.append(Wall((x, y)))

        over.clear()
        scorecard.score_reset()

screen.exitonclick()