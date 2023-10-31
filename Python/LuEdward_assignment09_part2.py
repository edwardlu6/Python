import turtle

def square(x, y, size, r, g, b):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.fillcolor(r,g,b)
    turtle.pencolor(r,g,b)
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(size)
        turtle.right(90)
    turtle.end_fill()
    
while True:
    choice = str.lower(input('(l)oad image or (q)uit:'))
    if choice == 'l':
        file = input('Enter a filename:')
        try:
            name = open(file, 'r')
        except:
            print('Invalid')
        else:
            turtle.tracer(0)
            alldata = name.read()
            name.close()
            turtle.setup(500, 500)
            

            
            size = int(alldata.split(',')[3])
            x = int(alldata.split(',')[1]) // -2 
            y = int(alldata.split(',')[2]) // 2 
            x0 = int(alldata.split(',')[1]) // 2
            y0 = int(alldata.split(',')[2]) // 2
            for i in range(4, (len(alldata.split(',')) - 1), 3):


                
                r = int(alldata.split(',')[int(i)]) / 255
                g = int(alldata.split(',')[int(i) + 1]) / 255
                b = int(alldata.split(',')[int(i) + 2]) / 255

                    
                
                if x0 > x and x < int(alldata.split(',')[1]) // 2:
                    x += size
                    
                else:
                    y -= size
                    x = int(alldata.split(',')[1]) // -2 + size
                square(x, y, size, r, g, b)
                
        turtle.update()
    elif choice == 'q':
        break
    else:
        print('Invalid command, try again')
