from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.shape("turtle")
        self.color("white")
        self.seth(90.00)
        self.goto(STARTING_POSITION)

    def move(self):
        self.fd(10)

