import turtle

pg = turtle.Screen()

pg.title("++ Juego Pong en python ++")
pg.bgcolor("lime")
pg.setup(width=800, height=600)
pg.tracer(0)

# raqueta Derecha
raq_d = turtle.Turtle()
raq_d.speed(0)
raq_d.shape("square")
raq_d.color("white")
raq_d.shapesize(stretch_wid=5, stretch_len=1)
raq_d.goto(350, 0)
raq_d.penup()


# raqueta Izquierda
raq_i = turtle.Turtle()
raq_i.speed(0)
raq_i.shape("square")
raq_i.color("white")
raq_i.shapesize(stretch_wid=5, stretch_len=1)
raq_i.goto(-350, 0)
raq_i.penup()

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
pt.write("Jugador Derecha: 0  Jugador Izquierda: 0", align='center', font=('Courier', 24, 'bold'))
pt.hideturtle()

# puntajes / scores
score_d = 0
score_i = 0

def raq_i_up():
    y = raq_i.ycor()
    y += 20
    raq_1.sety(y)

def raq_i_down():
    y = raq_i.ycor()
    y -= -20
    raq_i.sety(y)

def raq_d_up():
    y = raq_d.ycor()
    y += 20
    raq_d.sety(y)

def raq_d_down():
    y = raq_d.ycor()
    y -= -20
    raq_d.sety(y)

pg.listen()

pg.onkey(raq_d_up, 'Up')
pg.onkey(raq_d_down, 'Down')
pg.onkeypress(raq_i_up, 'w')
pg.onkey(raq_i_down, 's')

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
        score_d += 1
        pt.clear()
        pt.write("Jugador A: {} Juagdor B: {}".format(score_d, score_i), align='center', font=('Courier', 24, 'bold'))

    if bola.xcor() < -390:
        bola.goto(0, 0)
        bola.dx *= -1
        score_i += 1
        pt.clear()
        pt.write("Jugador A: {} Juagdor B: {}".format(score_d, score_i), align='center', font=('Courier', 24, 'bold'))

    # golpe a la bola: colision
    if (bola.xcor() > 340 and bola.xcor() < 350)  and (bola.ycor() < raq_i.ycor() + 60 and bola.ycor() > raq_i.ycor() - 60 ):
        bola.setx(340)
        bola.dx *=-1

    if (bola.xcor() < -340 and bola.xcor() > -350)  and (bola.ycor() < raq_d.ycor() + 60 and bola.ycor() > raq_d.ycor() - 60 ):
        bola.setx(-340)
        bola.dx *=-1

