from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.point = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.color("white")
        self.write(f"score: {self.point}", False, "center", ("Arial", 20, "bold"))

    def gotcha(self):
        self.clear()
        self.point += 1
        self.write(f"score: {self.point}", False, "center", ("Arial", 20, "bold"))
