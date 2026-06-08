#!/usr/bin/env python3

# import colorgram

# colors = colorgram.extract('image.jpg', 30)
# rgb_colors = []

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
    
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors[0])

color_list = [(208, 160, 82),
 (54, 89, 131), (146, 91, 40), (140, 26, 48), (222, 206, 108), (132, 177, 203),
 (158, 45, 83), (47, 55, 103), (167, 160, 38), (128, 189, 143), (84, 20, 44),
 (36, 42, 70), (187, 93, 105), (187, 139, 170), (84, 123, 181), (59, 39, 31),
 (78, 153, 165), (88, 157, 91), (195, 79, 72), (45, 74, 78), (161, 202, 220), 
 (80, 73, 44), (57, 131, 121), (218, 176, 188), (220, 183, 166), (166, 207, 165)]


import turtle as t
from turtle import Screen
import random

t.colormode(255)

tim = t.Turtle()
screen = Screen()

tim.speed('fastest')
tim.hideturtle()
tim.penup()


def random_color():
    return random.choice(color_list)

# positions the turtle in lefte
tim.setheading(255)
tim.forward(250)
tim.setheading(0)


def draw_row(no_of_rows):
    for i in range(no_of_rows):
        for j in range(10):
            tim.dot(20, random_color()) 
            tim.forward(50)
            
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)
    
draw_row(10)

screen.exitonclick()