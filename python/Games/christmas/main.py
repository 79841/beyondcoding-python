import turtle as t
import random

def prologue(t, color, x, y):
    t.pencolor(color)
    t.penup()
    t.fillcolor(color)
    t.goto(x, y)
    t.pendown()
    t.begin_fill()

def epilogue(t):
    t.end_fill()

def trapezoid(t, color, x, y, width, height):
    prologue(t, color, x, y)
    t.forward(width)
    t.right(60)
    t.forward(height)
    t.right(120)
    t.forward(width + height)
    t.right(120)
    t.forward(height)

    t.right(60)
    
    epilogue(t)

def star(t, color, x, y, length):
    prologue(t, color, x, y)
    for i in range(5):
        t.forward(length)
        t.right(144)
    epilogue(t)

def rectangle(t, color, x, y, width, height):
    prologue(t, color, x, y)
    for i in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    epilogue(t)

def write(t, color, x, y, msg, font):
    t.penup()
    t.pencolor(color)
    t.goto(x, y)
    t.write(msg, font=font)


t.speed(0)
t.bgcolor("aliceblue")

trapezoid(t, "darkgreen", -265, 230, 30, 100)
trapezoid(t, "darkgreen", -315, 130, 130, 100)
trapezoid(t, "darkgreen", -365, 30, 230, 100)
star(t, "gold", -300, 250, 100)
rectangle(t, "saddlebrown", -300, -220, 100, 150)

write(t, "gold", 150, 230, "Merry Christmas", ("Arial", 24, "italic"))

t.exitonclick()