from turtle import Turtle,Screen
positions=[(-380,0),(380,0)]

class Paddle():
    
    def __init__(self):
        self.my_paddles=[]
        self.create_paddles()
        self.l_paddle=self.my_paddles[0]
        self.r_paddle=self.my_paddles[1]

    def create_paddles(self):
        for i in range(2):
            my_turtle=Turtle()
            my_turtle.shape("square")
            my_turtle.color("white")
            my_turtle.shapesize(5,1)
            my_turtle.penup()
            my_turtle.goto(positions[i])
            self.my_paddles.append(my_turtle)
    
    def r_up(self):
        y_cor=self.my_paddles[1].ycor()
        self.my_paddles[1].goto(self.my_paddles[1].xcor(),y_cor+60)

    def r_down(self):
        y_cor=self.my_paddles[1].ycor()
        self.my_paddles[1].goto(self.my_paddles[1].xcor(),y_cor-60)

    def l_up(self):
        y_cor=self.my_paddles[0].ycor()
        self.my_paddles[0].goto(self.my_paddles[0].xcor(),y_cor+60)

    def l_down(self):
        y_cor=self.my_paddles[0].ycor()
        self.my_paddles[0].goto(self.my_paddles[0].xcor(),y_cor-60)

    def reset_paddles(self):
        self.l_paddle.goto(-380,0)
        self.r_paddle.goto(380,0)