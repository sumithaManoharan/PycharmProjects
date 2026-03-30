from turtle import Turtle

class Ball(Turtle): # Inherit from Turtle
    def __init__(self):
        super().__init__() # Initialize the Turtle features
        self.shape("circle")
        self.color("red")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        # Helps control the speed later

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_x(self):
        self.x_move *= -1

    def bounce_y(self):
        self.y_move *= -1



