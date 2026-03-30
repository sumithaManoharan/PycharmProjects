from turtle import Screen
from cars import Car
from turtle_cross import Mimi
from scoreboard import Scoreboard
import random, time

screen = Screen()
screen.tracer(0)
screen.setup(width=800, height=600)


turt = Mimi()
cars = Car()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(turt.move,"Up")

end = False
score = 0
speed = 3
while not end:
    cars.initiate_cars()
    screen.update()
    time.sleep(0.1)
    cars.move_cars()
    for car in cars.car_tle:
        if abs(car.ycor() - turt.ycor()) < 20:
            if abs(car.xcor() - turt.xcor()) < 30:
                scoreboard.game_over(score)
                end = True
    if turt.ycor() > 270:
        turt.goto(0,-290)
        score += 1
        scoreboard.increase_level()
        cars.increase_level()
    if turt.ycor() > 270 and score == 3:
        scoreboard.game_over(score)
        end = True

screen.exitonclick()