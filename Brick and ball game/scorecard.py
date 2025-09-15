from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.lives = 10

    def update_score(self):
        self.goto(260,360)
        self.write(f"Score:\n{self.score}",align="right",font=("Arial",14,"normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def update_lives(self):
        self.goto(-260,360)
        self.write(f"Lives:\n{self.lives}",align="left",font=("Arial",14,"normal"))

    def lives_decrease(self):
        self.lives -= 1
        self.clear()
        self.update_lives()


    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER!!!\nYour Score is {self.score}",align="center",font=("Arial",15,"normal"))


    
