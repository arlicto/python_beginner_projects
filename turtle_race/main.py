from turtle import Turtle, Screen
import random


is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="which turtle will win the race?Choose a color: ")
colors = ['red', 'blue', 'green', 'orange', 'purple']
y_positions = [-70,-40, -10, 20, 50, 80]
all_turtles = []

for i in range(5):
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.speed("fast")
    new_turtle.goto(-230, y_positions[i])
    all_turtles.append(new_turtle)
    
if user_bet:
    is_race_on = True
    
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! the {winning_color} turtle is the winner ")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
                
                
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
    

screen.exitonclick()
    