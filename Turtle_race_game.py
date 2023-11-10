# from turtle import Turtle, Screen
# tim = Turtle()
# screen = Screen()
#
#
# def forward():
#     tim.fd(10)
#
#
# def backward():
#     tim.bk(10)
#
#
#
# def clear():
#     tim.clear()
#
# def anticlock():
#     tim.left(30)
#
# def clockwise():
#     tim.right(30)
#
# screen.listen()
# screen.onkey(forward, "w")
# screen.onkey(backward, "s")
# screen.onkey(clear, "c")
# screen.onkey(anticlock, "d")
# screen.onkey(clockwise, "a")
# screen.exitonclick()
import random
from turtle import Turtle, Screen
import random
screen = Screen()

screen.setup(width=500, height=400)
User = screen.textinput(prompt="Place your bet on a color",title="bet")
Color = ["red", "blue", "orange", "purple", "green", "black"]
Cordinates_of_y = [40, 70, 100, 10, -20, -50]
Turtle_list = []
for i in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.color(Color[i])
    tim.penup()
    tim.goto(x=-230, y=Cordinates_of_y[i])
    Turtle_list.append(tim)

if User:
    Game_on = True

while Game_on:
    for i in Turtle_list:
        if i.xcor() > 230:
            Game_on = False
            if i == User:
                print(f"{User} wins")
            else:
                print(f"{i.pencolor()} wins. u lost")
        movement = random.randint(0, 10)
        i.fd(movement)






screen.exitonclick()



