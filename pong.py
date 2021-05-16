import turtle

pg = turtle.Screen()

pg.title("++ Juego Pong en python ++")
pg.bgcolor("lime")
pg.setup(width=800, height=600)
pg.tracer(0)

# raqueta 1
raq_1 = turtle.Turtle()
raq_1.speed(0)
raq_1.shape("square")
raq_1.color("white")
raq_1.shapesize(stretch_wid=5, stretch_len=1)
raq_1.goto(350, 0)
raq_1.penup()


# raqueta 2
raq_2 = turtle.Turtle()
raq_2.speed(0)
raq_2.shape("square")
raq_2.color("white")
raq_2.shapesize(stretch_wid=5, stretch_len=1)
raq_2.goto(-350, 0)
raq_2.penup()

# bola
bola = turtle.Turtle()
bola.speed(0)
bola.shape("circle")
bola.color("white")
bola.penup()
bola.goto(0,0)
bola.dx = 0.15
bola.dy = 0.15

# pantalla
pt = turtle.Turtle()
pt.speed(0)
pt.color('white')
pt.goto(0, 260)
pt.write("Jugador A: 0  Jugador B: 0", align='center', font=('Courier', 24, 'bold'))
pt.hideturtle()

# puntajes / scores
score_1 = 0
score_2 = 0

def raq_1_up():
    y = raq_1.ycor()
    y += 20
    raq_1.sety(y)

def raq_1_down():
    y = raq_1.ycor()
    y += -20
    raq_1.sety(y)

def raq_2_up():
    y = raq_2.ycor()
    y += 20
    raq_2.sety(y)

def raq_2_down():
    y = raq_2.ycor()
    y += -20
    raq_2.sety(y)

pg.listen()

pg.onkey(raq_1_up, 'Up')
pg.onkey(raq_1_down, 'Down')
pg.onkeypress(raq_2_up, 'w')
pg.onkey(raq_2_down, 's')

while True:
    pg.update()

    bola.setx(bola.xcor() + bola.dx)
    bola.sety(bola.ycor() + bola.dy)

    # evitar sobrepasar bordes
    if bola.ycor() > 290 or bola.ycor() < -290:
        bola.dy *= -1

    if bola.xcor() > 390:
        bola.goto(0, 0)
        bola.dx *= -1
        score_1 += 1
        pt.clear()
        pt.write("Jugador A: {} Juagdor B: {}".format(score_1, score_2), align='center', font=('Courier', 24, 'bold'))

    if bola.xcor() < -390:
        bola.goto(0, 0)
        bola.dx *= -1
        score_2 += 1
        pt.clear()
        pt.write("Jugador A: {} Juagdor B: {}".format(score_1, score_2), align='center', font=('Courier', 24, 'bold'))

    # golpe a la bola: colision
    if (bola.xcor() > 340 and bola.xcor() < 350)  and (bola.ycor() < raq_2.ycor() + 60 and bola.ycor() > raq_2.ycor() - 60 ):
        bola.setx(340)
        bola.dx *=-1

    if (bola.xcor() < -340 and bola.xcor() > -350)  and (bola.ycor() < raq_1.ycor() + 60 and bola.ycor() > raq_1.ycor() - 60 
                                                         ):
        bola.setx(-340)
        bola.dx *=-1

