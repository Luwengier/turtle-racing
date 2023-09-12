from turtle import Turtle

MOVE_DISTANCE = 20


class Snake:
    def __init__(self) -> None:
        self.segment = []

        for i in range(3):
            new_segment = Turtle(shape="square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.setx(i * -MOVE_DISTANCE)
            self.segment.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[seg_num - 1].xcor()
            new_y = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(new_x, new_y)

        self.segment[0].forward(MOVE_DISTANCE)

    def right(self):
        self.segment[0].setheading(0)

    def up(self):
        self.segment[0].setheading(90)

    def left(self):
        self.segment[0].setheading(180)

    def down(self):
        self.segment[0].setheading(270)
