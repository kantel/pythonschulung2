import turtle as t

wn = t.Screen()
wn.colormode(255)
wn.setup(width = 500, height = 500)
wn.title("Bouncing Ball")

ball = t.Turtle()
ball.shape("circle")
ball.color(255, 0, 0)
ball.penup()
speed = 8
angle = 125
ball.setheading(angle)

# Bildschirm-Refresh ausschalten
wn.tracer(0)


def exitGame():
    global keep_going
    keep_going = False

# Auf Tastaturereignisse lauschen
t.listen()
t.onkey(exitGame, "Escape") # Escape beendet das Spiel

keep_going = True
is_corner = False
while keep_going:
    wn.update()   # Bildschirm neuzeichnen
    ball.forward(speed)
    if ball.xcor() <= -240:
        ball.setx(-240)
        is_corner = True
    elif ball.xcor() >= 230:
        ball.setx(230)
        is_corner = True
    elif ball.ycor() <= -230:
        ball.sety(-230)
        is_corner = True
    elif ball.ycor() >= 240:
        ball.sety(240)
        is_corner = True
    if is_corner:
        angle += 90
        angle = angle%360
        ball.setheading(angle)
        is_corner = False
    
    
    