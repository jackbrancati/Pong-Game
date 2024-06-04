from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor('black')
screen.title('Pong')
#Need tracer set to 0 so game doesn't show animations like the paddles
#moving to its position at the start of the game
#However this needs to be continously refreshed or no animations will be shown
#at all
#See game_is_on variable and while loop below
screen.tracer(0)

scoreboard = Scoreboard()


r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

ball = Ball()


screen.listen()

screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')

screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')



#Continous refreshing to make the tracer(0) work
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()


    #Detect when right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    #Detect left paddle misses:
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()






screen.exitonclick()