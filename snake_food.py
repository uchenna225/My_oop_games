from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.refresh()
        self.speed("fastest")

    def refresh(self):
        x_coordinate = random.randint(-278, 278)
        y_coordinate = random.randint(-278, 278)
        self.goto(x_coordinate, y_coordinate)
