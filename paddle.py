from turtle import Turtle
from config import TOP, BOTTOM, UP, PADDLE_SPEED


class Paddle(Turtle):
    def __init__(self, x):
        super().__init__()
        self.create_paddle(x)

    def create_paddle(self, x):
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.color("coral")
        self.penup()
        self.goto(x, 0)
        self.setheading(UP)

    def up(self):
        if not self.ycor() > TOP - 40:
            self.forward(PADDLE_SPEED)
            # self.paddle.goto(self.paddle.xcor(), self.paddle.ycor() + 10)

    def down(self):
        if not self.ycor() < BOTTOM + 50:
            self.forward(-PADDLE_SPEED)
            # self.paddle.goto(self.paddle.xcor(), self.paddle.ycor() - 10)
