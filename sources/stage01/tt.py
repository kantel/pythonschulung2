import turtle as t

wn = t.Screen()
wn.colormode(255)
wn.bgcolor(43, 62, 80)
wn.setup(width = 600, height = 600)
wn.title("Ein Super-Duper Turtle-Programm")

alex = t.Turtle()
alex.shape("turtle")

berta = t.Turtle()
berta.shape("circle")

def quadrat(t):
    for i in range(4):
        t.forward(100)
        t.left(90)
        
alex.pensize(2)
alex.pencolor("red")
quadrat(alex)

berta.pensize(2)
berta.pencolor("white")
berta.goto(-100, 0)
quadrat(berta)


wn.mainloop()