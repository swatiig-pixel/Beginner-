import random

class Logic():

  def __init__(self):
    pass

  def result_num(guess):
    random_num = random.randint(1,100)
    if random_num == guess:
      result = "YOU WON!!"
    
    if random_num > guess:
      result = "It's Too Low"

    if random_num < guess:
      result = "It's Too High"

    return result

  