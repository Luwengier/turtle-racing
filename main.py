from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def forward():
    tim.forward(10)


screen.listen()
screen.onkey(key="space", fun=forward)
screen.exitonclick()
