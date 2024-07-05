from turtle import Turtle

# Constant setup for snake body segments
STARTING_POSITIONS = [0, -20, -40]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()


    def create_snake(self):
        # Create 3 new Turtle object instances, position them appropriately, and add them to snake_body
        for position in STARTING_POSITIONS:
            new_segment = Turtle(shape="square")
            new_segment.penup()
            new_segment.goto(x=position, y=0)
            self.snake_body.append(new_segment)


    def move(self):
        # Move the snake_body segments in reverse order to the previous position's location
        # This helps to make sure that the tail follow the head
        for seg in range(len(self.snake_body) - 1, 0, -1):
            prev_seg_pos_x = self.snake_body[seg - 1].xcor()
            prev_seg_pos_y = self.snake_body[seg - 1].ycor()
            self.snake_body[seg].goto(prev_seg_pos_x, prev_seg_pos_y)
        self.snake_body[0].forward(MOVE_DISTANCE)

    def up(self):
        self.snake_body[0].setheading(90)

    def down(self):
        self.snake_body[0].setheading(270)

    def left(self):
        self.snake_body[0].setheading(180)

    def right(self):
        self.snake_body[0].setheading(0)

