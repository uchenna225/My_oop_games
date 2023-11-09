from turtle import Screen, Turtle
X_COORDINATES = [0, -20, -40]
DISTANCE_TO_BE_COVERED = 20

class Snake:
    def __init__(self):
        self.Snake_length = []
        self.create_snake()
        self.head = self.Snake_length[0]
    def create_snake(self):
        for i in range(0, 3):
            tim = Turtle(shape="square")
            tim.color("white")
            tim.penup()
            tim.goto(y=0, x=X_COORDINATES[i])
            self.Snake_length.append(tim)

    def movement(self):
        for length in range(len(self.Snake_length) - 1, 0, -1):
            new_x_coordinates = self.Snake_length[length - 1].xcor()
            new_y_coordinates = self.Snake_length[length - 1].ycor()
            self.Snake_length[length].goto(new_x_coordinates, new_y_coordinates)

        self.head.fd(DISTANCE_TO_BE_COVERED)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)