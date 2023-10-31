def is_divisible_by(num, test):
    '''
    function:   is_divisible_by
    input:      two integers (num, test)
    processing: determines if the first integer 'num' is evenly divisible by
                the second integer 'test'
    output:     boolean (True or False)
    '''
    if test == 0:
        return False
    elif num // test - num / test == 0:
        return True
    else:
        return False




def get_sum_of_divisors(a):
    '''
    function:   get_sum_of_divisors
    input:      one integer
    processing: computes the sum of all positive divisors of the supplied integer,
                not including the integer itself.  for example:

                get_sum_of_divisors(10) -> 8
                get_sum_of_divisors(21) -> 11
                get_sum_of_divisors(-21) -> 11

                the function should work with both positive and negative integers.
                you can always assume the function will be called with an integer.
                your function can return a sum of 0 when analyzing the integer 0.
    output:     returns the sum of the divisors (integer)
    '''
    sum = 0
    if a >= 0:
        for b in range(1, int(a/2 + 1)):
            if a % b == 0:
                sum += b
        return sum
    elif a < 0:
        for b in range(1, int(-a/2 + 1)):
            if -a % b == 0:
                sum += b
        return sum    


        

    
def get_greatest_divisor(a):
          
    '''
    function:   get_greatest_divisor
    input:      one integer
    processing: computes the greatest (largest) positive divisor of the supplied integer,
                not including the integer itself. for example:

                get_greatest_divisor(10) -> 5
                get_greatest_divisor(21) -> 7
                get_greatest_divisor(-21) -> 7

                the function should work with both positive and negative integers.
                you can always assume the function will be called with an integer.
    output:     returns the greatest (largest) divisor (integer) or False if the
                integer being analyzed is 0, 1 or -1 (Boolean)
    '''
    if abs(a) in [0, 1]:
        return False
    for b in range(2, abs(a)):
        if abs(a) % b == 0:
            return abs(a) // b
    return 1

























'''
function:   is_prime
input:      one integer
processing: determines if the supplied integer is prime. a prime integer
            only has two factors - the integer 1 and itself.
            for example, 17 is prime because it only has two factors (1 and 17).
            the integers 0 and 1 should not be considered to be prime.
            negative integers should not be considered prime
output:     boolean
'''
def is_prime(a):
    if a > 1:
        for i in range(2, int(a/2)+1):
            if (a % i) == 0:
                return False
        else:
            return True
    else:
        return False


'''
function:   is_perfect
input:      one integer
processing: determines if the supplied integer is perfect. a perfect integer
            is a positive integer that is equal to the sum of its factors (i.e. the
            integer 6 is perfect because 6 = 1 + 2 + 3)
            1 is not considered a perfect integer
output:     boolean
'''
def is_perfect(a):
    sum = 0
    for i in range(1, int(a/2)+1):
        if a % i == 0:
            sum += i
    if a == sum:
        if a == 0:
            return False
        else:
            return True
    else:
        return False
        

'''
function:   is_abundant
input:      one integer
processing: determines if the supplied integer is abundant. an abundant integer
            is an integer that is less than the sum of its proper factors (i.e. the
            integer 12 is abundant because 12 < 1 + 2 + 3 + 4 + 6)
            for the purpose of this function you should treat all integers <= 0 as
            not abundant.
output:     boolean
'''
def is_abundant(a):
    sum = 0
    for i in range(1, int(a/2)+1):
        if a % i == 0:
            sum += i
    if a < sum:
        if a <= 0:
            return False
        else:
            return True
    else:
        return False
    


























'''
function:   get_least_significant_digit
input:      one integer
processing: extracts the least significant digit from the integer 
            (the value in the 'ones' place, the right-most value)
output:     returns the value in the 'ones' place (integer)
'''
def get_least_significant_digit(a):
    if a >= 0:
        return(a % 10)
    elif a < 0:
        return(-a % 10)
    


'''
function:   get_most_significant_digit
input:      one integer
processing: extracts the most significant digit from the integer.
            this value is the left-most value in the integer.
            its place value varies based on the size of the integer.

            hint 1: your function will need to 'reduce' the integer
            multiple times in order to extract this value. 

            hint 2: to perform this reduction you will need to continually
            shift the place values down.  for example:

            137 -> 13 -> 1

            hint 3: division and a 'while' loop may be very useful here!
output:     returns the value in the most significant place (integer)
'''
def get_most_significant_digit(a):
    if a < 0:
        a = -a
    b = 0 
    while a != 0:
        b = get_least_significant_digit(a)
        a //= 10 
    return b 





'''
function:   are_first_and_last_digits_the_same
input:      one integer
processing: determines if the first and last place value in the integer are the same
            
            101 -> True
            35 -> False
            1983343491 -> True
            7 -> True
            -707 -> True
output:     boolean

'''
def are_first_and_last_digits_the_same(a):
    if get_most_significant_digit(a) == get_least_significant_digit(a):
        return True
    else:
        return False
