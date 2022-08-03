import time
from turtle import Screen
from player import Player, FINISH_LINE_Y, STARTING_POSITION
from car_manager import CarManager, STARTING_MOVE_DISTANCE, Road
from scoreboard import Scoreboard
import random

screen = Screen()
screen.bgcolor("grey")
screen.title("Turtle Crossing")
screen.setup(width=600, height=600)
screen.tracer(0)

'''init turtle & cars'''
tim = Player()
cm = CarManager()
game_is_on = True

'''controls for turtle'''
screen.onkey(fun=tim.move, key="Up")
screen.listen()

'''init scoreboard'''
sb = Scoreboard()
road = Road()


while game_is_on:

    time.sleep(0.1)
    screen.update()

    '''create and move cars'''
    cm.create_car()
    cm.move_cars()

    '''detect turtle collision w/ car'''
    for car in cm.car_park:
        if tim.distance(car) < 15:
            sb.game_over()
            time.sleep(3)
            game_is_on = False


    '''detect if tim reached finish line'''
    if tim.ycor() > FINISH_LINE_Y:
        tim.goto(STARTING_POSITION)
        sb.score()
        cm.speed_up()


