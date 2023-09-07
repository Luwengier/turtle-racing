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
    new_segment.color("white")
    new_segment.setx(i * -20)
    snake.append(new_segment)

screen.update()
game_is_on = True

while game_is_on:
    snake[0].forward(20)

    for seg_num in range(len(snake) - 1, 0, -1):
        new_x = snake[seg_num - 1].xcor()
        new_y = snake[seg_num - 1].ycor()
        snake[seg_num].goto(new_x, new_y)

    screen.update()
    time.sleep(0.2)


screen.exitonclick()
