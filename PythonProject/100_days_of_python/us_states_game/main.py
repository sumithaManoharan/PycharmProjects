from operator import indexOf
from turtle import Screen, Turtle
import pandas as pd

states = pd.read_csv("50_states.csv")

screen = Screen()
mimi = Turtle()
mimi.hideturtle()
mimi.color("black")
screen.title("US States Game")

screen.bgpic("blank_states_img.gif")
end = False
score = 0
correct_guesses = []
while not end:
    guess = screen.textinput("State Name", "Enter a state")

    for index,row in states.iterrows():
        if guess.title() == row["state"]:
            score += 1
            correct_guesses.append(row["state"])
            mimi.penup()
            mimi.goto(row["x"],row["y"])
            mimi.write(arg=guess.title(), font=("courier", 10,"normal"), align="center")
            # mimi.showturtle()

        if guess.title() in correct_guesses:
            pass
        if len(guess)<1:
            mimi.penup()
            mimi.goto(0,0)
            mimi.write(f"GAME OVER\nscore: {score}/50", font=("courier", 20, "bold"), align="center")
            end = True





screen.exitonclick()