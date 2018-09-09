import turtle as t
import math

wn = t.Screen()
wn.colormode(255)
wn.bgcolor(43, 62, 80)
wn.setup(width = 600, height = 600)
wn.title("Ein Super-Duper Turtle-Programm")

alex = t.Turtle()
alex.shape("turtle")
alex.pensize(2)
alex.pencolor(253, 141, 60)


# Hier kommt jetzt Euer Programm-Code hin
def polygon(t, n, length):
    angle = 360.0/n
    for i in range(n):
        t.forward(length)
        t.left(angle)

def circle(t, r):
    circum = 2*math.pi*r
    # n = 50
    n = int(circum/3) + 1
    length = circum/n
    polygon(t, n, length)

alex.penup()
alex.goto(-32, -47)  # Polygon im Fenster »einmitten«
alex.pendown()
    
circle(alex, 100)

wn.mainloop()