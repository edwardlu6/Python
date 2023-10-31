def ascii_shift(String, direction):
    new_string = ''
    if direction == 'up':
        for i in String:
            if ord(i) in range(65, 91):
                if ord(i) == 90:
                    i = chr(65)
                else:
                    i = chr(ord(i) + 1)
                new_string += i
            else:
                new_string += i


    elif direction == 'down':
        for i in String:
            if ord(i) in range(65, 91):
                if ord(i) == 65:
                    i = chr(90)
                else:
                    i = chr(ord(i) - 1) 
                new_string += i
            else:
                new_string += i
    else:
        return String
    return new_string



def shift_right(word):
    last = word[-1]
    beginning = word[0:len(word) - 1]
    together = last + beginning

    return together

def shift_left(word):
    first = word[0]
    beginning = word[1:len(word)]
    together = beginning + first

    return together

def flip(word):
    if len(word) % 2 == 0:
        second_half = word[len(word) // 2: len(word)]
        first_half = word[0 : len(word) // 2]
        together = second_half + first_half
    elif len(word) % 2 != 0:
        second_half = word[(len(word) + 1) // 2: len(word)]
        middle = word[len(word) // 2]
        first_half = word[0 : len(word) // 2]
        together = second_half + middle + first_half

    return together


import random
    
def add_letters(string, integer):
    original = string

    new_word = ''

    for character in original:
        for i in range(integer):
            character += chr(random.randint(65, 90))
        new_word += character
    return new_word
        

def delete_characters(word, integer):
    new_word = ''
    new_word += word[0:len(word):integer+1]
    return new_word
print(delete_characters("HFtRKeivFllRNlUlGTaooYwoH!JpXL", 4))


'''
Part 2c (extra credit)Part 2c (extra credit)
'''
def add_padding(string, integer):
    for i in range(integer):
        string += chr(random.randint(65, 90))
    for i in range(integer):
        string = chr(random.randint(65, 90)) + string
    return string
    



def remove_padding(string, integer):
    string = string[integer:len(string) - integer]
    return string
    


def swap_characters(string):
     new_string = ''
     for i in range(len(string)):
         if i % 2 == 0:
             new_string += string[i + 1]

         elif i % 2 != 0:
             
         if i == len(string):
              
     return string




begin = str.upper(input("Enter an encoding pattern, 'end' to end:"))
if begin == 'END':
    print('')
else:
    word = str.upper(input("Enter a word to encode/decode:"))
    for i in begin:
        if 'A' == i:
            print('* Adding 1 letter between all characters:', add_letters(word, 1))
            word = add_letters(word, 1)

        elif 'X' == i:
            print('* Deleting 1 character:', delete_characters(word, 1))
            word = delete_characters(word, 1)

        elif 'F' == i:
            print('* Flipping:', flip(word))
            word = flip(word)

        elif 'U' == i:
            print('* ASCII shifting up:', ascii_shift(word, 'up'))
            word = ascii_shift(word, 'up')

        elif 'D' == i:
            print('* ASCII shifting down:', ascii_shift(word, 'down'))
            word = ascii_shift(word, 'down')

        elif 'L' == i:
            print('* Shifting left:',shift_left(word))
            word = shift_left(word)

        elif 'R' == i:
            print('* Shifting right:', shift_right(word))
            word = shift_right(word)
        elif 'P' == i:
            print('* Padding with 1 letter:', add_padding(word, integer))
            word = add_padding(string, integer)
        elif 'Q' == i:
            print('* Removing padding of 1 letter:', remove_padding(word, integer))
            word = remove_padding(word, integer)
        else:
            print("* '" + i + "' is an invalid command, ignoring")

    print('Final encoding / decoding:', word)
        
    



