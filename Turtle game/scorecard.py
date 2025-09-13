from turtle import Turtle
FONT = ("Courier", 14, "normal")

class Scorecard(Turtle):
  def __init__(self):
    super().__init__()
    self.score_mark = 1
    self.score()


  def score(self):
    self.penup()
    self.hideturtle()
    self.goto(-200,260)
    self.write(f"Level:{self.score_mark}",align="right",font=(FONT))

  def increase_score(self):
    self.score_mark += 1
    self.clear()
    self.score()

  def game_over(self):
    self.goto(0,0)
    self.write("GAME OVER",align="center",font=(FONT))
