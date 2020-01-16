import turtle; import random
screen=turtle.Screen()
Turtle=turtle.Turtle()
Turtle.shape("turtle")
Turtle.setpos(0,0)
Turtle.speed(0)

def sqr():
	for i in range(4):
		Turtle.fd(100)
		Turtle.rt(90)
def tri():
	for i in range(3):
		Turtle.fd(100)
		Turtle.rt(120)
def pent():
	for i in range(5):
		Turtle.fd(100)
		Turtle.rt(72)
def circ():
	Turtle.circle(100,120)
def penchange():
	r=random.randint(0,255)
	g=random.randint(0,255)
	b=random.randint(0,255)
	Turtle.pencolor(r,g,b)
def fcol():
	r=random.randint(0,255)
	g=random.randint(0,255)
	b=random.randint(0,255)
	Turtle.fillcolor(r,g,b)
def bgchange():
	r=random.randint(0,255)
	b=random.randint(0,255)
	g=random.randint(0,255)
	screen.bgcolor(r,g,b)
bgchange()
for i in range(90):
	Turtle.rt(4)
	Turtle.begin_fill()
	sqr()
	Turtle.end_fill()



