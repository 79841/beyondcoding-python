import turtle as t

def star(turtle, color, x, y, length):
    turtle.penup()
    turtle.fillcolor(color)
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(5):
        turtle.forward(length)
        turtle.right(144)
    turtle.end_fill()

    

def draw_trapezoid(turtle, color, x, y, width, height):
    
    turtle.penup()
    turtle.pencolor(color)
    turtle.fillcolor(color)
    
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(width)
    turtle.right(60)
    turtle.forward(height)
    turtle.right(120)
    turtle.forward(width+20)
    turtle.right(120)
    turtle.forward(height)
    turtle.right(60)
    turtle.end_fill()

t.pencolor("gold")
t.bgcolor("aliceblue")
star(t, "gold", -300, 250, 100)
t.write("Merry Christmas", font=("Arial", 24, "italic"))
t.exitonclick()
