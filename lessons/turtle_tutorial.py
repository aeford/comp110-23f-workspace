from turtle import Turtle, colormode, done
leo: Turtle = Turtle()

leo.penup()
leo.goto(-80, -60)
leo.pendown()
# Simplified drawing
i: int = 0
while (i<3):
    leo.forward(300)
    leo.left(120)
    i = i + 1
done()