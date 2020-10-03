import turtle

turtle.shape('turtle')
turtle.bgcolor('light blue')
turtle.color('black')
turtle.speed(11)

for i in range(360):
    turtle.circle(i/3 + 1)
    turtle.pensize(i/1000 + 1)
    turtle.forward(i)
    turtle.left(59)

turtle.exitonclick()
