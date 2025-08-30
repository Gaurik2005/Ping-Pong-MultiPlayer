from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.l_score=0
        self.r_score=0
        self.hideturtle()
        self.penup()
        self.pencolor("white")
        self.goto(-200,260)
        self.write(f"Score = {self.l_score}",align="center",font=("Courier", 25, "bold"))
        self.goto(200,260)
        self.write(f"Score = {self.r_score}",align="center",font=("Courier", 25, "bold"))

    def update_left_score(self):
        self.l_score+=1
        self.clear()
        self.goto(-200,260)
        self.write(f"Score = {self.l_score}",align="center",font=("Courier", 25, "bold"))
        self.goto(200,260)
        self.write(f"Score = {self.r_score}",align="center",font=("Courier", 25, "bold"))

    def update_right_score(self):
        self.r_score+=1
        self.clear()
        self.goto(-200,260)
        self.write(f"Score = {self.l_score}",align="center",font=("Courier", 25, "bold"))
        self.goto(200,260)
        self.write(f"Score = {self.r_score}",align="center",font=("Courier", 25, "bold"))

    def reset_score(self):
        self.l_score=0
        self.r_score=0
        self.clear()
        self.goto(-200,260)
        self.write(f"Score = {self.l_score}",align="center",font=("Courier", 25, "bold"))
        self.goto(200,260)
        self.write(f"Score = {self.r_score}",align="center",font=("Courier", 25, "bold"))

