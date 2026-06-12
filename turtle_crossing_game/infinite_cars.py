from turtle import Turtle
from random import choice, choices, randint
import time

COLORS = ["red", "blue", "green", "yellow", "black", "purple", "orange", "pink", "brown", "gray"]
STARTING_MOVE_DISTANCE = 1
MOVE_INCREMENT = 1.1

y_postions = [-240, -200, -160, -120, -80, -40, 0, 40, 80, 120, 160, 200, 240, 280, 320, 360, 400, 440, 480, 520, 560]


class InfiniteCars():
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE    
                
    def create_cars(self):
        random_chance = randint(1,10)
        if random_chance == 1: 
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(choice(COLORS))
            random_y = choice(y_postions)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)
        
    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
        
    def level_up(self):
        self.car_speed *= MOVE_INCREMENT
    
            
        
        
        
        
    