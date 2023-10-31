import math
import random
import time

while True:
    number = int(input('Number of throws:'))
    if number >= 1:
        break
    else:
        print('Invalid, try again!')
        continue
time1 = time.time()
red = 0
green = 0
yellow = 0
blue = 0
grey = 0
overlap = 0
misses = 0
for i in range(number):
    x = random.uniform(0, 800)
    y = random.uniform(0, 500)
    if x < 500 and y > 50 and y < 150:
        red += 1
    elif math.sqrt((x - 150) ** 2 + (y - 300) ** 2) < 150:
        green += 1
    elif x > 350 and x < 550 and y > 250 and y < 500:
        if x > 400 and x < 500 and y > 300 and y < 400:
            misses += 1
        else:
            yellow += 1
    elif math.sqrt((x - 700) ** 2 + (y - 200) ** 2) < 100 or math.sqrt((x - 700) ** 2 + (y - 350) ** 2) < 100:
        if math.sqrt((x - 700) ** 2 + (y - 200) ** 2) < 100 and math.sqrt((x - 700) ** 2 + (y - 350) ** 2) < 100:
            overlap += 1
        elif math.sqrt((x - 700) ** 2 + (y - 200) ** 2) < 100:
            blue += 1
        elif math.sqrt((x - 700) ** 2 + (y - 350) ** 2) < 100:
            grey += 1
    else:
        misses += 1
        
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
