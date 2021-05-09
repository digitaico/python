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
raq_1.goto(-350, 0)
raq_1.penup()


# raqueta 2
raq_2 = turtle.Turtle()
raq_2.speed(0)
raq_2.shape("square")
raq_2.color("white")
raq_2.shapesize(stretch_wid=5, stretch_len=1)
raq_2.goto(350, 0)
raq_2.penup()

# bola
bola = turtle.Turtle()
bola.speed(0)
bola.shape("circle")
bola.color("white")
bola.penup()
bola.goto(0,0)

# puntahes / scores
score_a = 0
score_b = 0

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
pg.onkey(raq_2_up, 'Up')
pg.onkey(raq_2_down, 'Down')


while True:
    pg.update()

    
