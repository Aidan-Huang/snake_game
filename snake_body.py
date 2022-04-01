from turtle import Turtle

class Block:
    def __init__(self):
        self.block = Turtle()

    # def __str__(self):
    #     return str(self.block.pos())


    def make_block(self, x, y):
        self.block.penup()
        self.block.color("white")
        self.block.shape("square")
        self.block.setpos(x=x, y=y)
        self.block.speed(100000)


class Snake:
    def __init__(self):
        self.snake_parts = []


    # def __str__(self):
    #     r = "snake: "
    #     for block in self.snake_parts:
    #         r += str(block) + ", "
    #     return r

    def move_forward(self):
        for char in range(len(self.snake_parts)-1, -1, -1):
            if char == 0:
                self.snake_parts[0].block.forward(20)
            else:
                self.snake_parts[char].block.setpos(self.snake_parts[char-1].block.pos())

    def to_up(self):
        self.snake_parts[0].block.setheading(90)

    def to_left(self):
        self.snake_parts[0].block.setheading(180)

    def to_down(self):
        self.snake_parts[0].block.setheading(270)

    def to_right(self):
        self.snake_parts[0].block.setheading(0)

    def eat(self,food_name):
        food_name.new_food.setpos(900,900)







