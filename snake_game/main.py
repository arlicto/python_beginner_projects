from turtle import Screen
from snake import Snake
import food
from scoreboard import Scoreboard
screen = Screen()
screen.bgcolor("black")
screen.setup(600, 600)
screen.title("My Snake Game")
screen.tracer(0)


game_is_on = True
snake = Snake()
food = food.Food()
scoreboard = Scoreboard()
# initial delay in milliseconds; lower means faster snake
game_speed = 100
screen.listen()
screen.onkeypress(snake.snake_up, "Up")
screen.onkeypress(snake.snake_down, "Down")
screen.onkeypress(snake.snake_left, "Left")
screen.onkeypress(snake.snake_right, "Right")


def move_snake():
    global game_is_on, game_speed
    if not game_is_on:
        return

    screen.update()
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        
        
        # speed up after eating food, with a lower bound
        game_speed = max(30, game_speed - 5)

    # detect collision with wall
    # allow the head to reach the visible edge before game over
    if abs(snake.head.xcor()) > 290 or abs(snake.head.ycor()) > 290:
        game_is_on = False
        scoreboard.game_over()
        return

    # detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
            return

    screen.ontimer(move_snake, game_speed)

move_snake()
screen.exitonclick()