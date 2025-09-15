from turtle import Turtle,Screen
from ball import Ball
from brick import Brick
from scorecard import Scoreboard

import time


screen = Screen()
screen.setup(width=600,height=800)
screen.bgcolor("black")
screen.title("Brick and ball game")
screen.tracer(0)


brick = Brick()
ball = Ball()
score = Scoreboard()


screen.listen()
screen.onkey(brick.left_move,"Left")
screen.onkey(brick.right_move,"Right")




game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    score.update_score()
    score.update_lives()



    #Detect the collision with wall
    if ball.xcor() > 280 or ball.xcor() < -280 :
        ball.bounce()
        

    #Detect the collision with brick
    if ball.distance(brick) < 50 and ball.ycor() < -370  :
        ball.opp()
        score.increase_score()

    if ball.ycor() < -380:
        ball.refresh()
        score.lives_decrease()

        

    #Detect upper collision
    if ball.ycor() > 380:
        ball.top_bounce()

    if score.lives == 0:
        score.game_over()
        game_is_on = False




screen.exitonclick()