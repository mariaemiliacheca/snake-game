from turtle import Turtle


STARTING_POSITIONS = [(-40,0),(0,0),(20,0)]
MOVE_DISTANCE= 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.segments = []
        self.create_body()
        self.head = self.segments[0]


    #TODO: Create snake body
    def create_body(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    #TODO: Move the snake
    def move(self):
        # Loop from segments going from last to first
        # range(start=, stop= , step= )
        for snake_num in range(len(self.segments) - 1, 0, -1):
            # get x and y coordinates of snake segment in front of curr
            new_x = self.segments[snake_num - 1].xcor()
            new_y = self.segments[snake_num - 1].ycor()
            self.segments[snake_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def add_segment(self, position):
        new_snake = Turtle("square")
        new_snake.color("white")
        new_snake.penup()
        new_snake.goto(position)
        self.segments.append(new_snake)

    def grow(self):
        self.add_segment(self.segments[-1].position())

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_body()
        self.head = self.segments[0]

    #TODO: Control the snake

    # North: 90
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    #South: 270
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    #West: 180
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    #East: 0
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
