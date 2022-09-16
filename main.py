from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.listen()
screen.tracer(0)
screen.setup(width=800, height=600)
scoreboard = Scoreboard()

score=Scoreboard()

r_paddle = Paddle()
r_paddle.goto(380, 0)

l_paddle = Paddle()
l_paddle.goto(-380, 0)

screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
var = 3
ball = Ball()
game_on = True
while game_on:
    time.sleep(0.001)
    screen.update()

    ball.forward(var)

    if abs(ball.ycor()) >290:
        ball.setheading(-ball.heading())

    if ball.distance(r_paddle)<30 and ball.xcor() >360:
        ball.setheading((180-ball.heading())%360)

    if ball.distance(l_paddle)<30 and ball.xcor() < -360:
        ball.setheading((180-ball.heading())%360)

    if ball.xcor()>450:
        score.l_increase_score()
        ball.reset()
    if ball.xcor()<-450:
        score.r_increase_score()
        ball.reset()
        var+=1
    if score.l_score > 4:
        scoreboard.game_over()
        game_on = False
    if score.r_score > 4:
        scoreboard.win()
        game_on = False


screen.exitonclick()