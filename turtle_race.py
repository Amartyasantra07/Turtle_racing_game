from turtle import Turtle, Screen
import random
is_race_on = True

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race?Enter a colour: ")
colors = ["red", "orange", "black", "blue", "green", "purple"]
y_position = [-70, -40, -10, 20, 50, 80]
all_turtle = []
# initializing 6 turtle charecter
for turtle_position in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_position])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_position])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in all_turtle:
        # To stop the turtles and choose the winner by stopping at 230 is 250 - half the width of the turtle
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                print(f"You have won. The {winning_color} turtle is the winner .")
            else:
                print(f"You have lost. The {winning_color} turtle is the winner ")
        # Make each turtle move a random amount
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()







