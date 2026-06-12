from turtle import Turtle, Screen
from random import choice, choices
from infinite_cars import InfiniteCars
from player import Player
from scoreboard import Scoreboard
import time




screen = Screen()
screen.setup(600, 600)
screen.tracer(0)
player = Player()
infinite_cars = InfiniteCars()
scoreboard = Scoreboard()



screen.listen()
screen.onkey(player.move_up, "w")
screen.onkey(player.move_up, "Up")
    
    
games_is_on = True
while games_is_on:
    time.sleep(.01)
    screen.update() 
    
    infinite_cars.create_cars()
    infinite_cars.move_cars()
    
    # detect collison with cars
    for car in infinite_cars.all_cars:
        if car.distance(player) < 20:
            games_is_on = False
            scoreboard.game_over()
            
    # detect successful crossing
    if player.is_at_finish_line():
        player.goto_start()
        infinite_cars.level_up()
        scoreboard.increase_level()
        
    

screen.exitonclick()

