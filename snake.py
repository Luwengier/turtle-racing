from turtle import Turtle


class Snake:
    def __init__(self) -> None:
        self.snake = []

        for i in range(3):
            new_segment = Turtle(shape="square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.setx(i * -20)
            self.snake.append(new_segment)

    def move(self):
        for seg_num in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[seg_num - 1].xcor()
            new_y = self.snake[seg_num - 1].ycor()
            self.snake[seg_num].goto(new_x, new_y)

        self.snake[0].forward(20)
        # snake[0].left(90)
        # snake[0].forward(20)
        # snake[0].right(90)
