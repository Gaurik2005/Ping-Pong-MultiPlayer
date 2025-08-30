from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
import turtle
from score_board import ScoreBoard
import time

my_screen=Screen()
my_screen.setup(800,600)
my_screen.bgcolor("black")
my_screen.title("PING PONG")
my_screen.tracer(0)


my_paddle=Paddle()
my_ball=Ball()
my_scoreboard=ScoreBoard()

loser_write=Turtle()
loser_write.hideturtle()
loser_write.color("white")


game_on=True
while game_on:

    my_screen.listen()
    my_screen.onkey(my_paddle.r_up,"Up")
    my_screen.onkey(my_paddle.r_down,"Down")
    my_screen.onkey(my_paddle.l_up,"w")
    my_screen.onkey(my_paddle.l_down,"s")

    time.sleep(0.01)
    my_ball.move()
    
    if my_ball.my_turtle.ycor()>280 or my_ball.my_turtle.ycor()< -280:
        my_ball.bounce_y()

    elif my_ball.my_turtle.xcor()>350 and my_ball.my_turtle.distance(my_paddle.my_paddles[1])<50 and my_ball.x_move>0:
        my_ball.bounce_x()
        my_ball.x_move-=0.3
        my_scoreboard.update_right_score()  

    elif my_ball.my_turtle.xcor()<-350 and my_ball.my_turtle.distance(my_paddle.my_paddles[0])<50 and my_ball.x_move<0: 
        my_ball.bounce_x()
        my_ball.x_move+=0.3
        my_scoreboard.update_left_score()

    elif my_ball.my_turtle.xcor()>380 or my_ball.my_turtle.xcor()< -380:
        loser_write.write("WOOPS , YOU LOST",align="center",font=("Courier", 25, "bold"))
        name= turtle.textinput("Play Again Input","Do you want to play another game?")

        if name.lower()=="yes" or name.lower()=="y":
            my_ball.reset_ball()
            my_scoreboard.reset_score()
            loser_write.clear()
            my_paddle.reset_paddles()
            continue
        else:
            loser_write.penup()
            loser_write.goto(loser_write.xcor(),150) 
            loser_write.color("blue")
            loser_write.write("Thanks for playing!!",align="center",font=("Courier", 25, "bold"))
            game_on=False
        
    

    my_screen.update()














my_screen.exitonclick()