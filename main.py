from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.colormode(255)
screen.tracer(0)


snake = []

for i in range(3):
    new_segment = Turtle(shape="square")
    new_segment.penup()
    new_segment.speed(1)
    new_segment.color("white")
    new_segment.setx(i * -20)
    snake.append(new_segment)

game_is_on = True

while game_is_on:
    for seg in snake:
        seg.forward(20)
    screen.update()
    time.sleep(0.5)


screen.exitonclick()
