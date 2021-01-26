from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=500, height=400)
colours = ["red", "orange", "green", "blue", "yellow", "purple"]
step = [0, 5, 10]

choice = screen.textinput(title="Who will win?", prompt="Pick a turtle, choose a color: ")

def config_turtle(pick, colour):
    pick.color(colours[colour])
    pick.penup()

def random_step(pick):
    pick.speed("fastest")
    move = random.choice(step)
    pick.forward(move)

t0 = Turtle(shape="turtle")
t1 = Turtle(shape="turtle")
t2 = Turtle(shape="turtle")
t3 = Turtle(shape="turtle")
t4 = Turtle(shape="turtle")
t5 = Turtle(shape="turtle")

turtles = [t0, t1, t2, t3, t4, t5]

xcoords = -240
ycoords = -150
for n in range(6):
    config = turtles[n]
    config_turtle(config, n)
    config.goto(x = xcoords, y = ycoords)
    ycoords += 60

trigger_finish = False
while trigger_finish != True:
    for n in range(6):
        config = turtles[n]
        random_step(config)
    if t0.xcor() > 230:
        if choice == "red":
            print("You Win!")
        else:
            print("You Lost!")
        trigger_finish = True
    elif t1.xcor() > 230:
        if choice == "orange":
            print("You Win!")
        else:
            print("You Lost!")
        trigger_finish = True
    elif t2.xcor() > 230:
        if choice == "green":
            print("You Win!")
        else:
            print("You Lost!")
        trigger_finish = True
    elif t3.xcor() > 230:
        if choice == "blue":
            print("You Win!")
        else:
            print("You Lost!")
        trigger_finish = True
    elif t4.xcor() > 230:
        if choice == "yellow":
            print("You Win!")
        else:
            print("You Lost!")
        trigger_finish = True
    elif t5.xcor() > 230:
        if choice == "purple":
            print("You Win!")
        else:
            print("You Lost!")
        trigger_finish = True

screen.exitonclick()