from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def forward():
    tim.forward(10)


def backward():
    tim.backward(10)


def left():
    tim.left(5)


def right():
    tim.right(5)


screen.listen()
screen.onkey(key="w", fun=forward)
screen.onkey(key="s", fun=backward)
screen.onkey(key="d", fun=right)
screen.onkey(key="a", fun=left)

screen.exitonclick()
