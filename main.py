from turtle import Turtle, Screen
from snake_body import Block, Snake
from food import Food
import time

is_on = True
score = 0
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title(f"My snake game\t\t\tscore:{score}")
my_snake = Snake()


def is_alive():
    screen.update()
    screen.tracer(1,0)
    if my_snake.snake_parts[0].block.xcor() >= 300 or my_snake.snake_parts[0].block.ycor() >= 300 \
            or my_snake.snake_parts[0].block.xcor() <= -300 or my_snake.snake_parts[0].block.ycor() <= -300:
        return False
    for char in range(1, len(my_snake.snake_parts)):
        if round(my_snake.snake_parts[0].block.xcor()) == round(my_snake.snake_parts[char].block.xcor())\
                and round(my_snake.snake_parts[0].block.ycor()) == round(my_snake.snake_parts[char].block.ycor()):
            return False

    return True


for n in range(0,10):
    screen.delay(10)
    screen.tracer(0)
    new_block = Block()
    new_block.make_block(-n * 20, 0)
    my_snake.snake_parts.append(new_block)

my_snake.snake_parts[0].block.setheading(0)
screen.listen()
is_food = False
while is_alive() == True:
    screen.title(f"My snake game\t\t\tscore:{score}")
    if is_food==False:
        now_food = Food(my_snake)
        now_food.locate_food()
        is_food = True
    screen.listen()
    screen.update()
    screen.tracer(0)
    my_snake.move_forward()
    if my_snake.snake_parts[0].block.heading() == 0:
        screen.onkeyrelease(fun=None, key="d")
        screen.onkeyrelease(fun=None, key="a")
        screen.onkeyrelease(fun=my_snake.to_up, key="w")
        screen.onkeyrelease(fun=my_snake.to_down, key="s")


    elif my_snake.snake_parts[0].block.heading() == 90:
        screen.onkeyrelease(fun=None, key="w")
        screen.onkeyrelease(fun=None, key="s")
        screen.onkeyrelease(fun=my_snake.to_left, key="a")
        screen.onkeyrelease(fun=my_snake.to_right, key="d")

    elif my_snake.snake_parts[0].block.heading() == 180:
        screen.onkeyrelease(fun=None, key="d")
        screen.onkeyrelease(fun=None, key="a")
        screen.onkeyrelease(fun=my_snake.to_up, key="w")
        screen.onkeyrelease(fun=my_snake.to_down, key="s")

    elif my_snake.snake_parts[0].block.heading() == 270:
        screen.onkeyrelease(fun=None, key="w")
        screen.onkeyrelease(fun=None, key="s")
        screen.onkeyrelease(fun=my_snake.to_left, key="a")
        screen.onkeyrelease(fun=my_snake.to_right, key="d")
    screen.update()
    screen.tracer()
    if is_alive()==False:
        break
    if round(my_snake.snake_parts[0].block.xcor()) == now_food.x and \
            round(my_snake.snake_parts[0].block.ycor()) == now_food.y:
        my_snake.eat(now_food)
        score += 1
        is_food = False
        new_block = Block()
        new_block.make_block(round(my_snake.snake_parts[-1].block.xcor()),\
                             round(my_snake.snake_parts[-1].block.xcor()))
        my_snake.snake_parts.append(new_block)


    time.sleep(0.1)
screen.textinput("you lose","you lose")


screen.exitonclick()
