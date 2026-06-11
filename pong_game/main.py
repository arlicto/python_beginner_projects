from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.title("My Pong Game")
screen.bgcolor("black")
screen.tracer(0)

left_paddle = Paddle(-350)
left_paddle.color("blue")
right_paddle = Paddle(350)
right_paddle.color("red")
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.01)
    screen.update()
    ball.move()
    
    # detect collision with north and south wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
     
    # detect collision with paddle
    right_paddle_left = right_paddle.xcor() - 10
    left_paddle_right = left_paddle.xcor() + 10
    ball_radius = 10
    paddle_half_height = 50

    right_collision = (
        ball.x_move > 0
        and ball.xcor() + ball_radius >= right_paddle_left
        and abs(ball.ycor() - right_paddle.ycor()) <= paddle_half_height + ball_radius
    )

    left_collision = (
        ball.x_move < 0
        and ball.xcor() - ball_radius <= left_paddle_right
        and abs(ball.ycor() - left_paddle.ycor()) <= paddle_half_height + ball_radius
    )

    if right_collision:
        ball.bounce_x()
        ball.change_color()
        ball.setx(right_paddle_left - ball_radius)
        ball.x_move *= 1.090
        ball.y_move *= 1.090
        
    elif left_collision:
        ball.bounce_x()
        ball.change_color()
        ball.setx(left_paddle_right + ball_radius)
        ball.x_move *= 1.090
        ball.y_move *= 1.090

    # out of bound logic for scoring and resetting the ball
    elif ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset_speed()
        ball.reset_position(x_direction=1)
        
    elif ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset_speed()
        ball.reset_position(x_direction=-1)
        
       
    





screen.exitonclick()