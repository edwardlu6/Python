import integer_functions
print('Integer Analysis System')
while True:
    a = str.lower(input('(c)hart numbers or (q)uit:'))
    if a == 'q':
        print('Program ending')
        break
    elif a == 'c':
        value1 = int(input('Enter the first value in your chart:'))
        while True:
            value2 = int(input('Enter the highest value in your chart:'))
            if value2 > value1:
                print('Key:')
                print('* E = Even')
                print('* O = Odd')
                print('* P = Prime')
                print('* R = Perfect')
                print('* A = Abundant')
                print('* % = First & Last Digits the Same')
                print('* D = Greatest Divisor')
                print()
                print('Number E O P R A % D')
                while True:
                    print(format(value1, '<7'), end = '')
                    if value1 % 2 == 0:
                        print('*', end = '')
                    else:
                        print(' ', end = '')
                    if value1 % 2 != 0:
                        print(format('*', '>2s'), end = '')
                    else:
                        print(format(' ', '>2s'), end = '')
                    if integer_functions.is_prime(value1) == True:
                        print(format('*', '>2s'), end = '')
                    else:
                        print(format(' ', '>2s'), end = '')
                    if integer_functions.is_perfect(value1) == True:
                        print(format('*', '>2s'), end = '')
                    else:
                        print(format(' ', '>2s'), end = '')
                    if integer_functions.is_abundant(value1) == True:
                        print(format('*', '>2s'), end = '')
                    else:
                        print(format(' ', '>2s'), end = '')
                    if integer_functions.are_first_and_last_digits_the_same(value1) == True:
                        print(format('*', '>2s'), end = '')
                    else:
                        print(format(' ', '>2s'), end = '')
                    print(format(integer_functions.get_greatest_divisor(value1), '>2'))
                    value1 += 1
                    if value1 > value2:
                        break
            else:
                print('Invalid, please try again')
                continue
            print()
            break
    else:
        print('Unknown command, please try again')
        continue
