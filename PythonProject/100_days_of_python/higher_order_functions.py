#the function which works with other functions are known as highr order functions
# state and instances
import random
from turtle import Turtle,Screen
#turtel race

is_race_on = False
screen = Screen()
screen.setup(width=500,height=400)
colors = ['red', 'green', 'blue', 'yellow', 'orange', 'purple']
num = 40
turtles = []

for color in range(len(colors)):
    mimi = Turtle(shape='turtle')
    mimi.color(colors[color])
    turtles.append(mimi)
    mimi.penup()
    mimi.goto(-230, -100+num)
    num += 40

user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race? enter a color:")
if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230 and turtle.color() == user_bet.lower():
            print(f"You won. {turtle.pencolor()} turtle won the race")
            is_race_on = False
            break
        elif turtle.xcor() > 230 and turtle.color() != user_bet.lower():
            print(f"You lost. {(turtle.pencolor())} turtle won the race")
            is_race_on = False
            break
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)




screen.exitonclick()