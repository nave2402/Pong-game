import time
from turtle import Screen
from paddle import Paddle
from scoreboard import ScoreBoard, Net
from ball import Ball

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
r_scoreboard = ScoreBoard((100, 170))
l_scoreboard = ScoreBoard((-100, 170))
net = Net()
ball = Ball()

screen.listen()
screen.onkey(fun=r_paddle.move_up, key="Up")
screen.onkey(fun=r_paddle.move_down, key="Down")
screen.onkey(fun=l_paddle.move_up, key="w")
screen.onkey(fun=l_paddle.move_down, key="s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    if ball.xcor() > 380:
        l_scoreboard.score_counting()
        ball.reset()
    if ball.xcor() < -380:
        r_scoreboard.score_counting()
        ball.reset()

    if r_scoreboard.score == 6 or l_scoreboard.score == 6:
        game_is_on = False
        net.clear()
        r_scoreboard.clear()
        l_scoreboard.game_over()


screen.exitonclick()
