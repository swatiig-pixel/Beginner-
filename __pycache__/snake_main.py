from turtle import Turtle , Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")





game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    snake.move()


    #Detect collision with food.
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    #Detect collision with wall
    if snake.segments[0].xcor() > 290 or snake.segments[0].xcor() <-290 or snake.segments[0].ycor() > 290 or snake.segments[0].ycor() <-290:
        game_is_on= False
        score.game_over()

    #detect collision
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            game_is_on = False
            score.game_over()



screen.exitonclick()