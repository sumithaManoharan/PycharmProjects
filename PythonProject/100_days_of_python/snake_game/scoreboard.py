from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = self.read_highscore()
        self.goto(0, 270)
        self.color("white")
        self.write(arg=f"score :{self.score}",align="center", font=("Arial", 12, "normal"))
        self.hideturtle()
        self.penup()


    def increase_score(self):
        self.clear()
        self.score += 1
        self.high_score()
        self.write(arg=f"score :{self.score} high_score: {self.highscore}", align="center", font=("Courier", 12, "normal"))

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(arg=f"Game over.\nfinal_score:{self.score}\nHigh_score: {self.highscore}", align="center", font=("Courier", 12, "normal"))

    def high_score(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("highscores.txt", "w") as file:
                file.write(f"{self.highscore}")


    def read_highscore(self):
        with open("highscores.txt", "r") as file:
            content = file.read()
            return int(content)
