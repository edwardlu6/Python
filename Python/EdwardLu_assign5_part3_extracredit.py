import math
import random
import time
import turtle

while True:
    number = int(input('Number of throws:'))
    if number >= 1:
        break
    else:
        print('Invalid, try again!')
        continue
while True:
    graphics = str.lower(input('Would you like to draw your results with turtle graphics? (yes/no):'))
    if graphics == 'yes':
        turtle.tracer(0)
        turtle.setup(800,500)
        time1 = time.time()
        red = 0
        green = 0
        yellow = 0
        blue = 0
        grey = 0
        overlap = 0
        misses = 0
        for i in range(number):
            x = random.uniform(-400, 400)
            y = random.uniform(-250, 250)
            if x < 100 and x > -400 and y > 100 and y < 200:
                turtle.penup()
                turtle.goto(x-3, y+3)
                turtle.pendown()
                turtle.pencolor("red")
                turtle.pensize(2)
                turtle.setheading(225)
                turtle.goto(x, y)
                red += 1
            elif math.sqrt((x + 250) ** 2 + (y + 50) ** 2) < 150:
                turtle.penup()
                turtle.goto(x-3, y+3)
                turtle.pendown()
                turtle.pencolor("green")
                turtle.pensize(2)
                turtle.setheading(225)
                turtle.goto(x, y)
                green += 1
            elif x > -50 and x < 150 and y > -250 and y < 0:
                if x > 0 and x < 100 and y > -150 and y < -50:
                    misses += 1
                else:
                    turtle.penup()
                    turtle.goto(x-3, y+3)
                    turtle.pendown()
                    turtle.pencolor("yellow")
                    turtle.pensize(2)
                    turtle.setheading(225)
                    turtle.goto(x, y)
                    yellow += 1
            elif math.sqrt((x - 300) ** 2 + (y - 50) ** 2) < 100 or math.sqrt((x - 300) ** 2 + (y + 100) ** 2) < 100:
                if math.sqrt((x - 300) ** 2 + (y - 50) ** 2) < 100 and math.sqrt((x - 300) ** 2 + (y + 100) ** 2) < 100:
                    turtle.penup()
                    turtle.goto(x-3, y+3)
                    turtle.pendown()
                    turtle.pencolor("black")
                    turtle.pensize(2)
                    turtle.setheading(225)
                    turtle.goto(x, y)
                    overlap += 1
                elif math.sqrt((x - 300) ** 2 + (y - 50) ** 2) < 100:
                    turtle.penup()
                    turtle.goto(x-3, y+3)
                    turtle.pendown()
                    turtle.pencolor("blue")
                    turtle.pensize(2)
                    turtle.setheading(225)
                    turtle.goto(x, y)
                    blue += 1
                elif math.sqrt((x - 300) ** 2 + (y + 100) ** 2) < 100:
                    turtle.penup()
                    turtle.goto(x-3, y+3)
                    turtle.pendown()
                    turtle.pencolor("grey")
                    turtle.pensize(2)
                    turtle.setheading(225)
                    turtle.goto(x, y)
                    grey += 1
            else:
                misses += 1
        break
    elif graphics == 'no':
        time1 = time.time()
        red = 0
        green = 0
        yellow = 0
        blue = 0
        grey = 0
        overlap = 0
        misses = 0
        for i in range(number):
            x = random.uniform(-400, 400)
            y = random.uniform(-250, 250)
            if x < 100 and x > -400 and y > 100 and y < 200:
                red += 1
            elif math.sqrt((x + 250) ** 2 + (y + 50) ** 2) < 150:
                green += 1
            elif x > -50 and x < 150 and y > -250 and y < 0:
                if x > 0 and x < 100 and y > -150 and y < -50:
                    misses += 1
                else:
                    yellow += 1
            elif math.sqrt((x - 300) ** 2 + (y - 50) ** 2) < 100 or math.sqrt((x - 300) ** 2 + (y + 100) ** 2) < 100:
                if math.sqrt((x - 300) ** 2 + (y - 50) ** 2) < 100 and math.sqrt((x - 300) ** 2 + (y + 100) ** 2) < 100:
                    overlap += 1
                elif math.sqrt((x - 300) ** 2 + (y - 50) ** 2) < 100:
                    blue += 1
                elif math.sqrt((x - 300) ** 2 + (y + 100) ** 2) < 100:
                    grey += 1
            else:
                misses += 1
        break
    else:
        print('Invalid choice, please try again')
        continue

        
time2 = time.time()
print('Total time elapsed:', time2 - time1, 'seconds')
print()
print('Red:', format(red, '>15,'), '(' + format(red / number * 100, '.2f') + '%)')
print('Green:', format(green, '>13,'), '(' + format(green / number * 100, '.2f') + '%)')
print('Yellow:', format(yellow, '>12,'),  '(' + format(yellow / number * 100, '.2f') + '%)')
print('Blue:', format(blue, '>14,'),  '(' + format(blue / number * 100, '.2f') + '%)')
print('Grey:', format(grey, '>14,'),  '(' + format(grey / number * 100, '.2f') + '%)')
print('Overlap:', format(overlap, '>11,'), '(' + format(overlap / number * 100, '.2f') + '%)')
print('Misses:', format(misses, '>12,'),  '(' + format(misses / number * 100, '.2f') + '%)')


