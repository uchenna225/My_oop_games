import turtle
from turtle import Turtle





class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.highest_score= int(file.read())
        self.ht()
        self.color("white")
        self.penup()
        self.goto(x=0, y=270)
        self.count()

    def count(self):
        self.clear()
        self.write(f"score: {self.score}  high score: {self.highest_score}", align="center", font=("Arial", 16, "normal"))

    def reset(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open("data.txt", mode= "w") as file:
                file.write(f"{self.score}")
        self.score = 0
        self.count()

    # def game(self):
    #     self.penup()
    #     self.color("white")
    #     self.goto(0, 0)
    #     self.write(f"game over", align="center", font=("Arial", 16, "normal"))

    def increase_count(self):
        self.score += 1
        self.count()



