from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
paddle = Turtle()
scoreboard = Scoreboard()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong Game')
screen.tracer(0)

ball = Ball()

right_paddle = Paddle(350)
left_paddle = Paddle(-350)



screen.listen()
screen.onkeypress(right_paddle.paddle_up, "Up")
screen.onkeypress(right_paddle.paddle_down, "Down")
screen.onkeypress(left_paddle.paddle_up, "w")
screen.onkeypress(left_paddle.paddle_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #detect collison with t paddle
    if ball.distance(right_paddle.paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle.paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #detect when paddle misses R
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()


    #L
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()