from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear() # This removes the OLD level text
        self.goto(-280, 260)
        self.write(f"Level: {self.score}", align="left", font=("Courier", 20, "bold"))

    def increase_level(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self,score):
        self.goto(0, 0)
        self.write(f"GAME OVER!\nYour Score : {score}", align="center", font=("Courier", 24, "bold"))