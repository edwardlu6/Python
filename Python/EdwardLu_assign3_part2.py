month = int(input("Enter a month as an integer:"))
day = int(input("Enter a day as an integer:"))
if month > 0 and month < 13 and day > 0 and day < 32:
    if month == 1:
        if day == 1 or day == 21 or day == 31:
            print("You entered January ", day, "st", sep = "")
            if day == 31:
                print("You do not have class today")
            else:
                print("This date is before the Spring 2023 semester. You do not have class today")
        elif day == 2 or day == 22:
            print("You entered January ", day, "nd", sep = "")
            print("This date is before the Spring 2023 semester. You do not have class today")
        elif day == 3 or day == 23:
            print("You entered January ", day, "rd", sep = "")
            if day == 23:
                print("You have class today")
            else:
                print("This date is before the Spring 2023 semester. You do not have class today")
        else:
            print("You entered January ", day, "th", sep = "")
            if day == 25 or day == 30:
                print("You have class today")
            else:
                print("You do not have class today")

    if month == 2:
        if day >= 29:
            print("This is an invalid date. Program ending")
        else:
            if day == 1 or day == 21:
                print("You entered Febuary ", day, "st", sep = "")
                if day == 1:
                    print("You have class today")
                else:
                    print("You do not have class today")
            elif day == 2 or day == 22:
                print("You entered Febuary ", day, "nd", sep = "")
                if day == 22:
                    print("You have class today")
                else:
                    print("You do not have class today")
            elif day == 3 or day == 23:
                print("You entered Febuary ", day, "rd", sep = "")
                print("You do not have class today")
            else:
                print("You entered Febuary ", day, "th", sep = "")
                if day == 6 or day == 8 or day == 13 or day == 15 or day == 20 or day == 27:
                    print("You have class today")
                else:
                    print("You do not have class today")

    if month == 3:
        if day == 1 or day == 21 or day == 31:
            print("You entered March ", day, "st", sep = "")
            if day == 1:
                print("You have class today")
            else:
                print("You do not have class today")
        elif day == 2 or day == 22:
            print("You entered March ", day, "nd", sep = "")
            if day == 22:
                print("You have class today")
            else:
                print("You do not have class today")
        elif day == 3 or day == 23:
            print("You entered March ", day, "rd", sep = "")
            print("You do not have class today")
        else:
            print("You entered March ", day, "th", sep = "")
            if day == 6 or day == 8 or day == 13 or day == 15 or day == 20 or day == 27 or day == 29:
                print("You have class today")
            else:
                print("You do not have class today")

    if month == 4:
        if day >= 31:
            print("This is an invalid date. Program ending")
        else:
            if day == 1 or day == 21:
                print("You entered April ", day, "st", sep = "")    
                print("You do not have class today")
            elif day == 2 or day == 22:
                print("You entered April ", day, "nd", sep = "")
                print("You do not have class today")
            elif day == 3 or day == 23:
                print("You entered April ", day, "rd", sep = "")
                if day == 3:
                    print("You have class today")
                else:
                    print("You do not have class today")
            else:
                print("You entered April ", day, "th", sep = "")
                if day == 5 or day == 10 or day == 12 or day == 17 or day == 19 or day == 24 or day == 26:
                    print("You have class today")
                else:
                    print("You do not have class today")
    if month == 5:
        if day == 1 or day == 21 or day == 31:
            print("You entered May ", day, "st", sep = "")
            if day == 1:
                print("You have class today")
            else:
                print("This date is after the Spring 2023 semester. You do not have class today")
        elif day == 2 or day == 22:
            print("You entered May ", day, "nd", sep = "")
            if day == 2:
                print("You do not have class today")
            else:
                print("This date is after the Spring 2023 semester. You do not have class today")
        elif day == 3 or day == 23:
            print("You entered May ", day, "rd", sep = "")
            if day == 3:
                print("You have class today")
            else:
                print("This date is after the Spring 2023 semester. You do not have class today")
        else:
            print("You entered April ", day, "th", sep = "")
            if day == 8 and day <= 8:
                print("You have class today")
            else:
                print("You do not have class today")
    if month == 6:
        if day >= 31:
            print("This is an invalid date. Program ending")
        else:
            if day == 1 or day == 21:
                print("You entered June ", day, "st", sep = "")
            elif day == 2 or day == 22:
                print("You entered June ", day, "nd", sep = "")
            elif day == 3 or day == 23:
                print("You entered June ", day, "rd", sep = "")
            else:
                print("You entered June ", day, "th", sep = "")
            print("This date is after the Spring 2023 semester. You do not have class today")
    if month == 7:
        if day == 1 or day == 21 or day == 31:
            print("You entered July ", day, "st", sep = "")
        elif day == 2 or day == 22:
            print("You entered July ", day, "nd", sep = "")
        elif day == 3 or day == 23:
            print("You entered July ", day, "rd", sep = "")
        else:
            print("You entered July ", day, "th", sep = "")
        print("This date is after the Spring 2023 semester. You do not have class today")
    if month == 8:
        if day == 1 or day == 21 or day == 31:
            print("You entered August ", day, "st", sep = "")
        elif day == 2 or day == 22:
            print("You entered August ", day, "nd", sep = "")
        elif day == 3 or day == 23:
            print("You entered August ", day, "rd", sep = "")
        else:
            print("You entered August ", day, "th", sep = "")
        print("This date is after the Spring 2023 semester. You do not have class today")
    if month == 9:
        if day >= 31:
            print("This is an invalid date. Program ending")
        else:
            if day == 1 or day == 21:
                print("You entered September ", day, "st", sep = "")
            elif day == 2 or day == 22:
                print("You entered September ", day, "nd", sep = "")
            elif day == 3 or day == 23:
                print("You entered September ", day, "rd", sep = "")
            else:
                print("You entered September ", day, "th", sep = "")
            print("This date is after the Spring 2023 semester. You do not have class today")

    if month == 10:
        if day == 1 or day == 21 or day == 31:
            print("You entered October ", day, "st", sep = "")
        elif day == 2 or day == 22:
            print("You entered October ", day, "nd", sep = "")
        elif day == 3 or day == 23:
            print("You entered October ", day, "rd", sep = "")
        else:
            print("You entered October ", day, "th", sep = "")
        print("This date is after the Spring 2023 semester. You do not have class today")
    if month == 11:
        if day >= 31:
            print("This is an invalid date. Program ending")
        else:
            if day == 1 or day == 21:
                print("You entered November ", day, "st", sep = "")
            elif day == 2 or day == 22:
                print("You entered November ", day, "nd", sep = "")
            elif day == 3 or day == 23:
                print("You entered November ", day, "rd", sep = "")
            else:
                print("You entered November ", day, "th", sep = "")
                print("This date is after the Spring 2023 semester. You do not have class today")
            
    if month == 12:
        if day == 1 or day == 21 or day == 31:
            print("You entered December ", day, "st", sep = "")
        elif day == 2 or day == 22:
            print("You entered December ", day, "nd", sep = "")
        elif day == 3 or day == 23:
            print("You entered December ", day, "rd", sep = "")
        else:
            print("You entered December ", day, "th", sep = "")
        print("This date is after the Spring 2023 semester. You do not have class today")
else:
    print("This is an invalid date. Program ending")
