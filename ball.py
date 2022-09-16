from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed(2)
        self.color("red")
        self.shape("circle")
        self.goto(0,0)
        self.shapesize(1)
        self.setheading(45)

    def reset(self):
        self.goto(0,0)
        self.setheading((self.heading()+180)%360)