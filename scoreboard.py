import turtle
from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.ht()
        self.color("white")
        self.penup()
        self.goto(x=0, y=270)
        self.count()

    def count(self):
        self.write(f"score: {self.score}", align="center", font=("Arial", 16, "normal"))

    def game(self):
        self.penup()
        self.color("white")
        self.goto(0, 0)
        self.write(f"game over", align="center", font=("Arial", 16, "normal"))

    def increase_count(self):
        self.score += 1
        self.clear()
        self.count()



