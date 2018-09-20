import turtle as t
import random as r

wn = t.Screen()
wn.colormode(255)
wn.setup(width = 500, height = 500)
wn.title("Bouncing Balls")


# Bildschirm-Refresh ausschalten
wn.tracer(0)


def exitGame():
    global keep_going
    keep_going = False

# Auf Tastaturereignisse lauschen
t.listen()
t.onkey(exitGame, "Escape") # Escape beendet das Spiel

balls = []
speed = 8

for i in range(10):
    balls.append(t.Turtle())
    balls[i].shape("circle")
    balls[i].color(255, 0, 0)
    balls[i].penup()
    angle = r.randint(90, 270)
    balls[i].setheading(angle)
    

keep_going = True
is_corner = False
while keep_going:
    wn.update()   # Bildschirm neuzeichnen
    for ball in balls:
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
