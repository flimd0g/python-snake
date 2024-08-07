from turtle import Turtle

# Constant setup for snake body segments
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]


    def create_snake(self):
        # Create 3 new Turtle object instances, position them appropriately, and add them to snake_body
        for position in STARTING_POSITIONS:
            self.add_segment(position)


    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.goto(position)
        self.snake_body.append(new_segment)


    def extend(self):
        self.add_segment(self.snake_body[-1].position())



    def move(self):
        # Move the snake_body segments in reverse order to the previous position's location
        # This helps to make sure that the tail follow the head
        for seg in range(len(self.snake_body) - 1, 0, -1):
            prev_seg_pos_x = self.snake_body[seg - 1].xcor()
            prev_seg_pos_y = self.snake_body[seg - 1].ycor()
            self.snake_body[seg].goto(prev_seg_pos_x, prev_seg_pos_y)
        self.head.forward(MOVE_DISTANCE)


    # Check current heading. Stops snake from going back on itself
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        for segment in self.snake_body:
            segment.goto(1000, 1000)
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]
