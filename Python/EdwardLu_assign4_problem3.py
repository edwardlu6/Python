num = int(input("Enter size for your pattern (3-9):"))
word = input("Enter a single character for your pattern:")
times = 0

while True:
    print()
    print("Pattern #1")
    print()
    while True:
        print(word * num)    
        times += 1
        if times == num:
            break
    break

while True:
    print()
    print("Pattern #2")
    print()
    print(word * num)
    middle = word + " " * (num - 2) + word + '\n'
    print(middle * (num - 2), end = '')
    print(word * num)
    break

times = 0
if True:
    print()
    print("Pattern #3")
    print()
    while True:
        times += 1
        if times % 2 != 0:
            print(word * num)
        else:
            print(format(word * num, '>' + str(num * 2) + 's'))
        if times == num:
            break
times = 0
if True:
    print()
    print("Pattern #4")
    print()
    while True:
        print(word + str(times) * num + word)
        times += 1
        if times >= num:
            break
times = 0
if True:
    print()
    print("Pattern #5")
    print()
    while True:
        times += 1
        print(format(word * num, '>' + str(num * 2 - times) + 's'))
        if times >= num:
            break
    
        

            




    



    
