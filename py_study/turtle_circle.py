import turtle
turtle.goto(0,0)
turtle.pendown()
turtle.pensize(2)
turtle.pencolor('blue')
for i in range(40,-1,-5):#i分别为40,35,30,25,20,15,10,5,0，半径慢慢减小到0的圆，画图纵坐标相应变大
    turtle.penup()
    turtle.goto(0,i)
    turtle.pendown()
    turtle.circle(-i)
for i in range(4):
    #turtle.penup()
    turtle.pendown()
    turtle.forward(300)
    turtle.left(90)


