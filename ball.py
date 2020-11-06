from turtle import Turtle
from random import randint
from config import TOP, BOTTOM


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()
        self.move_speed = 0.01

    def create_ball(self):
        self.shape("turtle")
        self.color("sky blue")
        self.penup()
        self.goto(0, 0)
        # self.setheading(0)
        if randint(0, 1) == 1:
            self.setheading(randint(-45, 45))
        else:
            self.setheading(randint(135, 225))

    def move(self):
        self.detect_wall_collision()
        self.forward(5)

    def detect_wall_collision(self):
        x = self.xcor()
        y = self.ycor()

        # hits top or bottom wall
        if y > TOP or y < BOTTOM:
            self.setheading(self.heading() * -1)

    def back_to_origin(self):
        self.goto(0, 0)
        self.move_speed = 0.01
        if randint(0, 1) == 1:
            self.setheading(randint(-45, 45))
        else:
            self.setheading(randint(135, 225))
