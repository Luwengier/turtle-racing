from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(
    title="Make your bet", prompt="Which turtle will win the race? Enter a color: "
)
rainbow = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle_group = []


def join_turtle(order: int):
    new_tim = Turtle(shape="turtle")
    new_tim.speed("fastest")
    new_tim.penup()
    new_tim.color(rainbow[i])
    new_tim.goto(x=-230, y=(order * 60 - 150))
    turtle_group.append(new_tim)


for i in range(6):
    join_turtle(i)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtle_group:
        turtle.forward(random.randint(0, 10))

        if turtle.xcor() > 240:
            is_race_on = False


screen.exitonclick()
