import turtle

t = turtle.Turtle()
t.speed(10)  
def draw_heart():
    t.begin_fill()
    t.color("red")
    t.left(140)
    t.forward(180)
    t.circle(-90, 200)
    t.left(120)
    t.circle(-90, 200)
    t.forward(180)
    t.end_fill()

draw_heart()

t.hideturtle()
turtle.done()
