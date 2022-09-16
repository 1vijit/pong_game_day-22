from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed(0)
        self.color("white")
        self.shape("square")
        self.tiltangle(90)
        self.setheading(90)
        self.shapesize(stretch_wid=5, stretch_len=1)

    def up(self):
        if self.ycor() < 245:
            self.forward(30)

    def down(self):
        if self.ycor() > -240:
            self.backward(30)

