from turtle import Turtle,Screen
import random

screen=Screen()
screen.setup(width=500,height=400)
user=screen.textinput(title="make a pet",prompt="what color you choose")
colors=["red","orange","yellow","green","blue","purple"]
y=[-70,-40,-10,20,50,80]
u=[]


for turtle_index in range(0,6):
    t=Turtle(shape="turtle")
    t.color(colors[turtle_index])
    t.penup()
    t.goto(x=-230,y=y[turtle_index])
    u.append(t)
if user:
    id_race=True
while id_race:
    for turtle in u:
        if turtle.xcor()>230:
            id_race=False
            w=turtle.pencolor()
            if w==user:
                print("Win")
            else:
                print("Lose")

        rand_distance=random.randint(0,10)
        turtle.forward(rand_distance)




screen.exitonclick()
