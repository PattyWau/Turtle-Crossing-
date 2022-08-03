from turtle import Turtle

FONT = ("Courier", 15, "normal")


class Scoreboard(Turtle):

    Level = 1

    def __init__(self):
        super().__init__()
        self.pu()
        self.ht()
        self.color("black")
        self.goto(-230, 260)
        self.write(arg=f"Level: {self.Level}", move=False, align="center", font=FONT)

    def score(self):
        self.Level += 1
        self.clear()
        self.write(arg=f"Level: {self.Level}", move=False, align="center", font=FONT)

    def game_over(self):
        self.pu()
        self.goto(0, 0)
        self.color("black")
        self.write(arg="Game Over X/", move=False, align="center", font=FONT)

