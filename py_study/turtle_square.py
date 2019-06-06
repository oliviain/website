import turtle
turtle.goto(0,0)
turtle.pendown()
turtle.pensize(2)
turtle.pencolor('blue')
for i in range(4):
    turtle.penup()
    turtle.goto(i*20,i*20)
    turtle.pendown()
    for j in range(4):
        turtle.forward(300-i*40)
        turtle.left(90)
