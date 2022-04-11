import turtle
import random
import time

screen = turtle.Screen()
screen.screensize(1000, 500)
screen.bgcolor("black")

sleep_time = 0.5

pen = turtle.Turtle()

rect_height = [i for i in range(1, 500)]

def get_rect_height():
    random.shuffle(rect_height)

def draw_rectangles():
    
    pen.speed(0)
    pen.shape("square")
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(-500, -250)
    pen.left(90)
    
    for i in rect_height:
        pen.shapesize(2.0, i, 1)
        pen.forward(i)
        pen.stamp()
        pen.right(90)
        pen.forward(2)
        pen.right(90)
        pen.forward(i)
        pen.left(180)

        
# Sorting algorithms
def bubble_sort():
    swap = True

    while swap:
        swap = False
        
        for i in range(len(rect_height) - 1):
            if rect_height[i] > rect_height[i + 1]:
                temp = rect_height[i]
                rect_height[i] = rect_height[i + 1]
                rect_height[i + 1] = temp
                swap = True
                time.sleep(sleep_time)


draw_rectangles()
screen.mainloop()
