from turtle import Turtle
LOC = [(-40,250),(40,250),(0,0)]

class Scoreboard:
    def __init__(self):
        self.create_line()
        self.stamp_id = 0
        self.score_turtle = []
        self.scre_tur()
        self.l_turtle = self.score_turtle[0]
        self.r_turtle = self.score_turtle[1]
        self.go = self.score_turtle[2]

    def create_line(self):
        line = Turtle()
        line.hideturtle()
        line.goto(0, 290)
        line.color("green")
        line.pensize(3)
        for i in range(30):
            line.pendown()
            line.setheading(90)
            line.backward(10)
            line.penup()
            line.backward(10)

    def scre_tur(self):
       for i in LOC:
           self.scores(loc=i)


    def scores(self,loc):
        score = Turtle()
        score.hideturtle()
        score.penup()
        score.pensize(3)
        score.color("blue")
        score.goto(loc)
        score.pendown()
        self.score_turtle.append(score)


    def l_scores(self,num):
        self.l_turtle.clear()
        self.l_turtle.write(arg=num, move=False, font=("Courier", 24, "normal"))

    def r_scores(self,num):
        self.r_turtle.clear()
        self.r_turtle.write(arg=num, move=False, font=("Courier", 24, "normal"))

    def game_over(self,won):
        self.score_turtle[-1].write(f"GAME OVER\n{won} won!", font=("Courier", 24, "normal"))
















