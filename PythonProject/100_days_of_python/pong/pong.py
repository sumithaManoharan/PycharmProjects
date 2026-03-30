from turtle import Turtle
PADDLE_POSITIONS = [(-370,0),(370,0)]

class Pong:
    def __init__(self):
        self.paddles = []
        self.create_paddles()
        self.right_paddle = self.paddles[1]
        self.left_paddle = self.paddles[0]

    def create_paddles(self):
        for i in PADDLE_POSITIONS:
            self.paddle(i)

    def paddle(self, position):
        paddle = Turtle("square")
        paddle.hideturtle()
        paddle.penup()
        paddle.color("yellow")
        # stretch_wid makes it TALL (5 * 20px = 100px)
        # stretch_len makes it THIN (1 * 20px = 20px)
        paddle.shapesize(stretch_wid=5, stretch_len=1)
        paddle.goto(position)
        paddle.showturtle()
        paddle.speed(3)
        self.paddles.append(paddle)

    def up(self):
        # Only move up if the paddle is below the top edge (250)
        if self.right_paddle.ycor() < 250:
            new_y = self.right_paddle.ycor() + 30
            self.right_paddle.sety(new_y)

    def down(self):
        # Only move down if the paddle is above the bottom edge (-250)
        if self.right_paddle.ycor() > -250:
            new_y = self.right_paddle.ycor() - 30
            self.right_paddle.sety(new_y)

    def left_up(self):
        if self.left_paddle.ycor() < 250:
            new_y = self.left_paddle.ycor() + 20
            self.left_paddle.sety(new_y)

    def left_down(self):
        if self.left_paddle.ycor() > -250:
            new_y = self.left_paddle.ycor() - 20
            self.left_paddle.sety(new_y)

