import turtle as t

wn = t.Screen()
wn.colormode(255)
wn.setup(width = 500, height = 500)
wn.title("Bouncing Ball")

ball = t.Turtle()
ball.shape("circle")
ball.color(255, 0, 0)
ball.penup()

wn.mainloop()