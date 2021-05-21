from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.bgcolor("black")
screen.title("Pong Game")
screen.setup(width=800, height=500)
screen.tracer(0)

r_paddle = Paddle((372, 0))
l_paddle = Paddle((-372, 0))
ball = Ball()
score = Scoreboard()


screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")


game_is_on = True

while game_is_on:
    time.sleep(ball.speed_ball)
    screen.tracer(1)
    ball.move()

    #Detect collisioin with the wall
    if ball.ycor() > 230 or ball.ycor() < -230:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()

    if ball.xcor() > 390:
        ball.reset_position()
        score.l_point()

    if ball.xcor() < -390:
        ball.reset_position()
        score.r_point()






screen.exitonclick()
