import turtle
import math
import random
turtle.tracer(0)


turtle.setup(800,800)

turtle.fillcolor(1.0, 0.87, 0)
turtle.begin_fill()
turtle.penup()
turtle.goto(-400,-400)
turtle.goto(-400,400)
turtle.goto(400,400)
turtle.goto(400,-400)
turtle.goto(-400,-400)
turtle.end_fill()

turtle.fillcolor("dark green")
turtle.begin_fill()
turtle.penup()
turtle.goto(-400,-100)

turtle.forward(800)
turtle.right(90)
turtle.forward(300)
turtle.right(90)
turtle.forward(800)
turtle.right(90)
turtle.forward(300)
turtle.right(90)

turtle.end_fill()

x = 0
y = 0

def sunset(x, y):
    '''
    input: x and y coordinates (integers)
    processing: draws a sun at the x, y coordinates specified using turtle.circle().
    output: a red circle appears.
    '''
    
    turtle.fillcolor('Red')
    turtle.begin_fill()
    turtle.penup()
    turtle.goto(00,-200)
    turtle.circle(100,360)
    turtle.end_fill()

def river(x, y):
    '''
    input: x and y coordinates (integers)
    processing: draws a river at the x, y coordinates specified
    output: a blue river appears
    '''
    turtle.fillcolor('Blue')
    turtle.begin_fill()
    turtle.penup()
    turtle.goto(-100, -400)
    turtle.goto(-100, -100)
    turtle.goto(100, -100)
    turtle.goto(100, -400)
    turtle.goto(-100,-400)
    turtle.end_fill()


def tree(x, y):
    '''
    input: x and y coordinates (integers)
    processing: draws a tree at the random x, y coordinates
    output: a tree appears
    '''
    num =  int(turtle.textinput('Number', 'How many trees will you draw?'))
    for i in range(num // 2):
        x = random.randint(-400, -180)
        y = random.randint(-225, -100)
        turtle.fillcolor('light green')
        turtle.begin_fill()
        turtle.penup()
        turtle.goto(x, y)
        turtle.goto(x, y + 75)
        turtle.goto(x + 70, y + 75)
        turtle.goto(x + 70, y)
        turtle.goto(x, y)
        turtle.end_fill()
        turtle.fillcolor('brown')
        turtle.begin_fill()
        turtle.penup()
        turtle.goto(x + 20, y - 100)
        turtle.goto(x + 20, y)
        turtle.goto(x + 50, y)
        turtle.goto(x + 50, y - 100)
        turtle.goto(x + 20, y - 100)

        turtle.end_fill()

    for i in range(num - num // 2):
        x = random.randint(140, 400)
        y = random.randint(-225, -100)
        turtle.fillcolor('light green')
        turtle.begin_fill()
        turtle.penup()
        turtle.goto(x, y)
        turtle.goto(x, y + 75)
        turtle.goto(x + 70, y + 75)
        turtle.goto(x + 70, y)
        turtle.goto(x, y)
        turtle.end_fill()
        turtle.fillcolor('brown')
        turtle.begin_fill()
        turtle.penup()
        turtle.goto(x + 20, y - 100)
        turtle.goto(x + 20, y)
        turtle.goto(x + 50, y)
        turtle.goto(x + 50, y - 100)
        turtle.goto(x + 20, y - 100)

        turtle.end_fill()

def cloud(x,y):
    '''
    input: x and y coordinates (integers)
    processing: draws a cloud at the random x, y coordinates 
    output: a white cloud appears
    '''
    num1 =  int(turtle.textinput('Number', 'How many clouds will you draw?(At lease 5)'))
    for i in range(num1):
        x = random.randint(-350, 350)
        y = random.randint(150, 400)
        turtle.fillcolor('white')
        turtle.begin_fill()
        turtle.penup()
        turtle.goto(x, y)
        turtle.goto(x - 100, y)
        turtle.goto(x - 100, y - 80)
        turtle.goto(x, y -80)
        turtle.goto(x, y)
        turtle.end_fill()

def steve(x, y):
    '''
    input: x and y coordinates (integers)
    processing: draws a steve at the x, y coordinates specified
    output: a steve from Minecraft appears.
    '''
    turtle.fillcolor('black')
    turtle.begin_fill()
    turtle.penup()
    turtle.goto(-200, -260)
    turtle.goto(-160, -260)
    turtle.goto(-160, -250)
    turtle.goto(-200, -250)
    turtle.goto(-200, -260)
    turtle.end_fill()
    turtle.fillcolor('brown')
    turtle.begin_fill()
    turtle.penup()
    turtle.goto(-200, -290)
    turtle.goto(-160, -290)
    turtle.goto(-160, -260)
    turtle.goto(-200, -260)
    turtle.end_fill()

    turtle.fillcolor(0, 0.7, 0.8)
    turtle.begin_fill()
    turtle.penup()
    turtle.goto(-220, -290)
    turtle.goto(-140, -290)
    turtle.goto(-140, -300)
    turtle.goto(-160, -300)
    turtle.goto(-160, -340)
    turtle.goto(-200, -340)
    turtle.goto(-200, -300)
    turtle.goto(-220, -300)
    turtle.goto(-220, -290)
    turtle.end_fill()

    turtle.fillcolor('brown')
    turtle.begin_fill()
    turtle.penup()
    turtle.goto(-220, -300)
    turtle.goto(-220, -340)
    turtle.goto(-200, -340)
    turtle.goto(-200, -300)
    turtle.goto(-220, -300)
    turtle.end_fill()

    turtle.fillcolor('brown')
    turtle.begin_fill()
    turtle.penup()
    turtle.goto(-160, -300)
    turtle.goto(-160, -340)
    turtle.goto(-140, -340)
    turtle.goto(-140, -300)
    turtle.goto(-160, -300)
    turtle.end_fill()

    turtle.fillcolor('blue')
    turtle.begin_fill()
    turtle.penup()
    turtle.goto(-200, -340)
    turtle.goto(-160, -340)
    turtle.goto(-160, -380)
    turtle.goto(-200, -380)
    turtle.goto(-200, -340)
    turtle.end_fill()

    turtle.fillcolor('grey')
    turtle.begin_fill()
    turtle.penup()
    turtle.goto(-200, -380)
    turtle.goto(-160, -380)
    turtle.goto(-160, -390)
    turtle.goto(-200, -390)
    turtle.goto(-200, -380)
    turtle.end_fill()
    






sunset(x, y)
river(x, y)
tree(x, y)
cloud(x, y)
steve(x, y)
