from turtle import Turtle
import random
gamestart = True

COLORS = ["red", "pink", "LightSkyBlue", "Orchid3", "PaleGreen3", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.ht()
        self.car_park = []
        self.startspeed = STARTING_MOVE_DISTANCE
        self.increase_speed = MOVE_INCREMENT

    def create_car(self):
        dice = random.randint(1,6)
        if dice == 1:
            car = Turtle("square")
            car.pu()
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.setheading(180)
            x = random.randint(300, 350)
            y = random.randint(-250, 250)
            car.color(random.choice(COLORS))
            car.goto(x, y)
            self.car_park.append(car)


    def move_cars(self):
        for car in self.car_park:
            car.fd(self.startspeed)

    def speed_up(self):
        self.startspeed += self.increase_speed

class Road(Turtle):

    def __init__(self):
        super().__init__()
        self.pu()
        self.ht()
        self.speed("fastest")
        self.color("white")
        self.setheading(180)
        self.goto(300, 0)
        self.draw()

    def draw(self):
        while self.xcor() > -300:
            self.pd()
            self.fd(10)
            self.pu()
            self.fd(10)


