from turtle import Turtle
from snake_body import Snake

import random
class Food:
    def __init__(self,snake_name):
        self.is_locating = True
        while self.is_locating == True:
            self.is_block = False
            self.list_x = []
            for n in range(20, 600,20):
                self.list_x.append(n)
            self.list_y = []
            for n in range(20, 600, 20):
                self.list_y.append(n)
            self.x = random.choice(self.list_x) - 300
            self.y = random.choice(self.list_y) - 300
            for char in snake_name.snake_parts:
                if self.x == round(char.block.xcor()) and \
                        self.y == round(char.block.ycor()):
                    self.is_block = True
                    break
            if self.is_block == False:
                self.is_locating = False

    def locate_food(self):
        self.new_food = Turtle()
        self.new_food.penup()
        self.new_food.shape("square")
        self.new_food.color("red")
        self.new_food.setpos(x=self.x, y=self.y)

