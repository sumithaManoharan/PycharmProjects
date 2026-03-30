import random
import turtle
from turtle import Turtle, Screen
from itertools import cycle

mimi = Turtle()
sc = turtle.Screen()
mimi.shape("turtle")
mimi.color("blue")
mimi.speed(0)
turtle.colormode(255)
directions = [0,90,180,270]
# mimi.width(5)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

for i in range(360):
    mimi.color(random_color())
    mimi.circle(100)
    mimi.setheading(i*5)
sc.exitonclick()









