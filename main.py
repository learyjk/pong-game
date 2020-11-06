from turtle import Screen
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
from config import RIGHT, LEFT
import time


def setup_screen():
    s = Screen()
    s.setup(width=800, height=400)
    s.bgcolor("black")
    s.tracer(0)
    s.title("Pong!")
    return s


screen = setup_screen()

# create entities
ball = Ball()
paddle1 = Paddle(RIGHT)
paddle2 = Paddle(LEFT)
scoreboard = Scoreboard()

# listen for key presses
screen.listen()
screen.onkey(paddle1.up, "Up")
screen.onkey(paddle1.down, "Down")
screen.onkey(paddle2.up, "w")
screen.onkey(paddle2.down, "s")

# main game loop
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)

    # detect collision with right paddle
    if ball.distance(paddle1) < 50 and ball.xcor() > RIGHT - 20:
        ball.setheading(180 - ball.heading())
        ball.move_speed *= 0.09

    # detect collision with left paddle
    if paddle2.distance(ball) < 50 and ball.xcor() < LEFT + 20:
        ball.setheading(180 - ball.heading())
        ball.move_speed *= 0.09

    # detect miss / score / game
    if ball.xcor() > RIGHT + 30:
        scoreboard.increase_score(2)
        ball.back_to_origin()
        screen.delay(5)

    if ball.xcor() < LEFT - 30:
        scoreboard.increase_score(1)
        ball.back_to_origin()
        screen.delay(5)

    ball.move()

screen.exitonclick()
