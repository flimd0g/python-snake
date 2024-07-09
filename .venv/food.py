from turtle import Turtle
import random

# Define grid for food spawn
screen_matrix_x = range(-280, 280, 20)
screen_matrix_y = range(-280, 280, 20)



class Food(Turtle):
    def __init__(self):
        super().__init__() # Take all attributes and methods from turtle class
        self.shape("square")
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.shapesize(stretch_wid=0.9, stretch_len=0.9)
        self.refresh() # Spawn food in random location as defined in method below


    def refresh(self): # Get random value for food location
        random_x = random.choice(screen_matrix_x)
        random_y = random.choice(screen_matrix_y)
        self.goto(random_x, random_y)







