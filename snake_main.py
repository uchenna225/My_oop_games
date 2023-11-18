from turtle import Screen, Turtle
from snake import Snake
import time
from scoreboard import Score
from snake_food import Food
Screen = Screen()
Screen.setup(width=600, height=600)
Screen.title("My first snake game")
Screen.bgcolor("black")
Screen.tracer(0)

Game_on = True

snake = Snake()
food = Food()
score = Score()

Screen.listen()


while Game_on:
    # updates the screen and slows down the time
    Screen.update()
    time.sleep(0.1)

    # keyboard movement
    Screen.onkey(snake.up, "Up")
    Screen.onkey(snake.down, "Down")
    Screen.onkey(snake.left, "Left")
    Screen.onkey(snake.right, "Right")
    snake.movement()

    # checks for contact with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_count()

    # Game_over
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()

    # BODY_COLLISION
        for body in snake.Snake_length[1:]:
            if body == snake.head:
                pass
            elif snake.head.distance(body) < 15:
                score.reset()

Screen.exitonclick()

