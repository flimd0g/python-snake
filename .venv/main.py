from turtle import Turtle, Screen
import time
from snake import Snake

#Screen setup code.
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("green")
screen.title("Python Snake")
screen.tracer(0) #Turn turtle animation off and set delay for update drawings.

snake = Snake() # Create snake instance from class
screen.listen()
screen.onkey(fun=snake.up, key="w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

screen.update() # Perform a Screen update. To be used when tracer is turned off.

game_is_on = True

while game_is_on:
    screen.update() # Perform a TurtleScreen update
    time.sleep(0.1) # Timing control. Adjust if required
    snake.move()




















screen.exitonclick()