import turtle
from turtle import Turtle
import random

COLORS = ['red', 'green', 'blue', 'yellow', 'cyan', 'magenta']
INITIAL_SPEED = 5
INCREASED_SPEED = 10

class Car:
    def __init__(self):
        self.car_tle = []
        self.speed = INITIAL_SPEED


    def initiate_cars(self):
        random_chance = random.randint(1,5)
        if random_chance == 1:
            x= range(-240,240)
            y = random.choice(x)
            self.cars(y)


    def cars(self,y):
        cr = Turtle("square")
        cr.hideturtle()
        cr.shapesize(stretch_wid=1, stretch_len=2)
        cr.color(random.choice(COLORS))
        cr.setheading(180)
        cr.penup()
        cr.goto(420,y)
        cr.showturtle()
        self.car_tle.append(cr)

    def move_cars(self):
        for car in self.car_tle:
            car.forward(self.speed)

    def increase_level(self):
        self.speed += INCREASED_SPEED


