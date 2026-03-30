from turtle import Turtle


class Mimi(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.goto(-0,-290)
        self.showturtle()

    def move(self):
        self.speed("fastest")
        self.forward(20)


