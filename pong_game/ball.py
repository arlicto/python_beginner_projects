from turtle import Turtle
import time
import random

class Ball(Turtle):
    
    def __init__ (self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.move_speed = 2
        self.reset_speed()
        
        
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)
        
    def bounce_y(self):
        self.y_move *= -1
        
    def bounce_x(self):
        self.x_move *= -1
        
    def change_color(self):
        colors = ["red", "blue", "green", "yellow", "purple", "orange", "cyan", "magenta"]
        self.color(random.choice(colors))
        
    def reset_position(self, x_direction=None):
        time.sleep(0.5)
        self.goto(0, 0)
        if x_direction is None:
            x_direction = random.choice([-1, 1])
        self.x_move = self.move_speed * x_direction
        self.y_move = self.move_speed * random.choice([-1, 1])
        
    def reset_speed(self):
        self.move_speed = 2
        self.x_move = self.move_speed * random.choice([-1, 1])
        self.y_move = self.move_speed * random.choice([-1, 1])