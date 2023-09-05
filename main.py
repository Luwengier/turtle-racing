from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.colormode(255)

snake = []

for i in range(3):
    newPoint = Turtle(shape="square")
    newPoint.color(255, 255, 255)
    newPoint.setx(i * 20)
    snake.append(newPoint)


screen.exitonclick()
