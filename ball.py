from turtle import Turtle

class Ball():
    def __init__(self):
        self.create_ball()
        self.x_move=3
        self.y_move=3
        
    def create_ball(self):
        self.my_turtle=Turtle()
        self.my_turtle.shape("circle")
        self.my_turtle.color("blue")
        self.my_turtle.penup()

    def move(self):
        self.y_cor=self.my_turtle.ycor()
        self.x_cor=self.my_turtle.xcor()
        self.my_turtle.goto(self.x_cor+self.x_move,self.y_cor+self.y_move)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_ball(self):
        self.my_turtle.goto(0,0)
        self.x_move=3
        self.y_move=3

    
        
        