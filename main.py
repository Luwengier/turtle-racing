from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
rainbow = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle_group = []


def join_turtle(order: int):
    new_tim = Turtle()
    new_tim.penup()
    new_tim.color(rainbow[i])
    new_tim.goto(x=-230, y=(order * 60 - 150))
    turtle_group.append(new_tim)


for i in range(6):
    join_turtle(i)


screen.exitonclick()
