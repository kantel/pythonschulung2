import turtle as t

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

alex.penup()
alex.goto(-32, -47)  # Polygon im Fenster »einmitten«
alex.pendown()
    
polygon(alex, 5, 70)

wn.mainloop()