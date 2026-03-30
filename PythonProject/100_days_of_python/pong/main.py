#create the screen
from pong import Pong
from turtle import Screen
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.tracer(0)
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")

pong = Pong()
pong_ball = Ball()
scoreboard = Scoreboard()
scoreboard.create_line()


screen.listen()
screen.onkey(pong.up, "Up")
screen.onkey(pong.down, "Down")
screen.onkey(pong.left_up, "w")
screen.onkey(pong.left_down, "s")

collision = False

l_score = 0
r_score = 0

import time # Add this at the top
from turtle import Screen
# ... your other imports ...

 # Turns off animation for smoothness

while not collision:
    screen.update()
    time.sleep(0.03)# Slows the game down so you can see it
    # Refresh the screen
    pong_ball.move()
    pong_ball.speed(1)

    # 1. Wall Collision (Top/Bottom)
    if pong_ball.ycor() > 280 or pong_ball.ycor() < -280:
        pong_ball.bounce_y()

    # 2. Paddle Collision (Right & Left)
    # Check if ball is far enough right/left AND close to the paddle
    if (pong_ball.distance(pong.right_paddle) < 50 and pong_ball.xcor() > 340) or \
       (pong_ball.distance(pong.left_paddle) < 50 and pong_ball.xcor() < -340):
        pong_ball.bounce_x()

    # 3. Scoring (Right Wall)
    if pong_ball.xcor() > 380:
        pong_ball.goto(0, 0) # Reset ball
        pong_ball.bounce_x() # Start moving toward the other player
        l_score += 1
        scoreboard.l_scores(l_score)

    # 4. Scoring (Left Wall)
    if pong_ball.xcor() < -380:
        pong_ball.goto(0, 0)
        pong_ball.bounce_x()
        r_score += 1
        scoreboard.r_scores(r_score)

    if r_score > 10  :
        collision = True
        scoreboard.game_over("right")
    elif l_score > 10 :
        collision = True
        scoreboard.game_over("left")
    # screen.update()
screen.exitonclick()