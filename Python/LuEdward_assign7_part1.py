
while True:
    username = input('Enter a username:')

    print('* Length of username:', len(username))
          
    failed_rules = 0

    if len(username) < 8 or len(username) > 15:
        print('  ERROR - username must be between 8 and 15 characters long')

    print("* All characters alpha & numeric:", username.isalnum())
    if username.isalnum() == False:
        print("* ERROR! Username must be all alpha numeric")

    print("* First character is digit:", username[0].isdigit())
    if username[0].isdigit() == True:
        print("* ERROR! First character cannot be a digit")

    print("* Last character is digit:", username[-1].isdigit())
    if username[-1].isdigit() == True:
        print("* ERROR! Last character cannot be a digit")

    uppers = 0
    lowers = 0
    digits = 0

    for character in username:
          if character.isdigit() == True:
              digits += 1

          elif character.isupper() == True:
              uppers += 1

          elif character.islower() == True:
              lowers += 1

    print('* # of uppercase characters:', uppers)
    if uppers == 0:
        print('* ERROR - username must contain at least one uppercase character')
        failed_rules += 1

    print('* # of lowercase characters:', lowers)
    if lowers == 0:
        print('  ERROR - username must contain at least one lowercase character')
        failed_rules += 1

    print('* # of digit characters:', digits)
    if digits == 0:
        print('  ERROR - username must contain at least one digit character')
        failed_rules += 1

    if failed_rules > 0:
        print('Username is not valid, please try again')
    else:
        print('Username is valid!')
        break














while True:
    password = input('Enter a password:')

    failed_rules = 0

    print('* Length of password:', len(password))
    if len(password) < 8:
          print('  ERROR - password must be at least 8 characters long')
    print('* Username is part of password:', username in password)
    if username in password:
          print('  ERROR - username cannot exist within password')

    upper = 0
    lower = 0
    digit = 0
    special_character = 0
    invalid = 0
    special = ["#", "$", "%", "!"]


    for character in password:
          if character.isdigit() == True:
              digit += 1

          elif character.isupper() == True:
              upper += 1

          elif character.islower() == True:
              lower += 1
          elif character in special:
              special_character += 1

          else:
              invalid += 1
            

    print('* # of uppercase characters in the password:', upper)
    if uppers == 0:
        print('* ERROR - password must contain at least one uppercase character')
        failed_rules += 1

    print('* # of lowercase characters in the password:', lower)
    if lowers == 0:
        print('  ERROR - password must contain at least one lowercase character')
        failed_rules += 1

    print('* # of digit characters in the password:', digit)
    if digits == 0:
        print('  ERROR - password must contain at least one digit character')
        failed_rules += 1

    print('* # of special characters in the password:', special_character)
    if special_character == 0:
        print('  ERROR - password must contain at least one special character')
        failed_rules += 1
    print('* # of invalid characters in the password:', invalid)
    if invalid != 0:
        print('  ERROR - password cannot contain any invalid characters')
        failed_rules += 1
        

    if failed_rules > 0:
        print('Password is not valid, please try again')
    else:
        print('Password is valid!')
        break


