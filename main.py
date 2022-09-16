from turtle import Turtle, Screen
from paddle import Paddle

screen = Screen()
screen.bgcolor("black")
screen.listen()
screen.tracer()
screen.setup(width=800, height=600)

r_paddle = Paddle()
r_paddle.goto(380, 0)

l_paddle = Paddle()
l_paddle.goto(-380, 0)

screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_on = True
while game_on:
    screen.update()

screen.exitonclick()