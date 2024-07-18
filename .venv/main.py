from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

#Screen setup code.
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("green")
screen.title("Python Snake")
screen.tracer(0) #Turn turtle animation off and set delay for update drawings.

snake = Snake() # Create snake instance from class
food = Food() # Create food instance from class
scoreboard = Scoreboard()

screen.listen() # Create keypress events for snake control
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

screen.update() # Perform a Screen update. To be used when tracer is turned off.

game_is_on = True

while game_is_on:
    screen.update() # Perform a TurtleScreen update
    time.sleep(0.1) # Timing control. Adjust if required
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 10:
        food.refresh()
        snake.extend()
        scoreboard.add_point()

    # Detect collision with border
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for segment in snake.snake_body[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()