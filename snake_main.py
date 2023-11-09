from turtle import Screen, Turtle
from snake import Snake
import time
from snake_food import Food
Screen = Screen()
Screen.setup(width=600, height=600)
Screen.title("My first snake game")
Screen.bgcolor("black")
Screen.tracer(0)

Game_on = True

snake = Snake()
food = Food()

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


Screen.exitonclick()

