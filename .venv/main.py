from turtle import Turtle, Screen
import time

#Screen setup code.
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("green")
screen.title("Python Snake")
screen.tracer(0) #Turn turtle animation off and set delay for update drawings.

#Initial list setup for snake body segments
starting_positions = [0, -20, -40]
snake_body = []

# Create 3 new Turtle object instances, position them appropriately, and add them to snake_body
for position in starting_positions:
    new_segment = Turtle(shape="square")
    new_segment.penup()
    new_segment.goto(x=position, y=0)
    snake_body.append(new_segment)

screen.update() # Perform a Screen update. To be used when tracer is turned off.

game_is_on = True

while game_is_on:
    screen.update() # Perform a TurtleScreen update. To be used when tracer is turned off.
    time.sleep(0.1) # Timing control. Adjust if required.

    # Move the snake_body segments in reverse order to the previous position's location
    # This helps to make sure that the tail follow the head
    for seg in range(len(snake_body) - 1, 0, -1):
        prev_seg_pos_x = snake_body[seg - 1].xcor()
        prev_seg_pos_y = snake_body[seg - 1].ycor()
        snake_body[seg].goto(prev_seg_pos_x, prev_seg_pos_y)

    # Test code to ensure everything works so far
    snake_body[0].forward(20)
    snake_body[0].left(90)


















screen.exitonclick()