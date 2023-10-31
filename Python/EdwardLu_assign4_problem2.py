
import random
times = 0
total1 = 0
total2 = 0
high = 0
high_low = 0
even = 0
odd = 0
mixed = 0
sum_value = 0
neighbor = 0
middle = 0
double = 0

while True:
    sides = int(input("How many sides on your dice (4, 6, 8, 10, 12 or 20)?"))
    if sides == 4 or sides == 6 or sides == 8 or sides == 10 or sides == 12 or sides ==20:
        print()
        print("Thanks, here we go!")
        print()

        while sides == 4:
            die1 = random.randint(1,4)
            die2 = random.randint(1,4)
            total1 += die1
            total2 += die2
            times += 1

            if die1 == 1 and die2 == 1:
                print(times, ". die roll is *1* and *1* Odd! Doubles! Snake Eyes!", sep = "")
                odd += 1
                double += 1
                break
                
            elif die1 % 2 == 0 and die2 % 2 == 0:
                if die1 == 4 and die2 == 4:
                    print(times, ". die roll is *", die1, "* and *", die2, "* Even! High! Double!", sep = "")
                    even += 1
                    high += 1
                    double += 1
                elif die1 == 2 and die2 == 2:
                    print(times, ". die roll is *", die1, "* and *", die2, "* Even! Sum Value! Double!", sep = "")
                    even += 1
                    sum_value += 1
                    double += 1
                else:
                    print(times, ". die roll is *", die1, "* and *", die2, "* Even!", sep = "")
                    even += 1
            elif die1 % 2 != 0 and die2 % 2 != 0:
                if die1 + die2 == 4:
                    print(times, ". die roll is *", die1, "* and *", die2, "* Odd! Sum Value!", sep = "")
                    odd += 1
                    sum_value += 1
                elif die1 == die2:
                    print(times, ". die roll is *", die1, "* and *", die2, "* Odd! Double!", sep = "")
                    odd += 1
                    double += 1
            elif die1 % 2 != 0 and die2 % 2 == 0 or die1 % 2 == 0 and die2 % 2 != 0:
                if die1 in [1,2] and die2 in [1,2] :
                    print(times, ". die roll is *", die1, "* and *", die2, "* Mixed! Neighbor! ", sep = "")
                    mixed += 1
                    neighbor += 1
                elif die1 in [1,4] and die2 in [1,4]:
                    print(times, ". die roll is *", die1, "* and *", die2, "* High / Low! Mixed!", sep = "")
                    high_low += 1
                    mixed += 1
                elif die1 in [2,3] and die2 in [2,3]:
                    print(times, ". die roll is *", die1, "* and *", die2, "* Mixed! Neighbor! Middle!", sep = "")
                    mixed += 1
                    neighbor += 1
                    middle += 1
                elif die1 in [3,4] and die2 in [3,4]:
                    print(times, ". die roll is *", die1, "* and *", die2, "* Mixed! Neighbor!", sep = "")
                    mixed += 1
                    neighbor += 1

        while sides == 6:
            die1 = random.randint(1,6)
            die2 = random.randint(1,6)
            total1 += die1
            total2 += die2
            times += 1

            if die1 == 1 and die2 == 1:
                print(times, ". die roll is *1* and *1* Odd! Doubles! Snake Eyes!", sep = "")
                odd += 1
                double += 1
                break
            
            elif die1 % 2 == 0 and die2 % 2 == 0:
                if die1 == die2:
                    if die1 + die2 == 6:
                        print(times, ". die roll is *", die1, "* and *", die2, "* Even! Sum Value! Doubles!", sep = "")
                        even += 1
                        sum_value += 1
                        double += 1
                    elif die1 == die2 == 6:
                        print(times, ". die roll is *", die1, "* and *", die2, "* High! Even! Doubles!", sep = "")
                        high += 1
                        even += 1
                        double += 1
                    else:
                        print(times, ". die roll is *", die1, "* and *", die2, "* Even! Doubles!", sep = "")
                        even += 1
                        double += 1
                elif die1 + die2 == 6:
                    print(times, ". die roll is *", die1, "* and *", die2, "* Even! Sum Value!", sep = "")
                    even += 1
                    sum_value += 1
                else:
                    print(times, ". die roll is *", die1, "* and *", die2, "* Even!", sep = "")
                    even += 1
            elif die1 % 2 != 0 and die2 % 2 != 0:
                if die1 == die2:
                    if die1 + die2 == 6:
                        print(times, ". die roll is *", die1, "* and *", die2, "* Odd! Sum Value! Doubles!", sep = "")
                        odd += 1
                        sum_value += 1
                        double += 1
                    else:
                        print(times, ". die roll is *", die1, "* and *", die2, "* Odd! Doubles!", sep = "")
                        odd += 1
                        double += 1
                elif die1 + die2 == 6:
                    print(times, ". die roll is *", die1, "* and *", die2, "* Odd! Sum Value!", sep = "")
                    odd += 1
                    sum_value += 1
                else:
                    print(times, ". die roll is *", die1, "* and *", die2, "* Odd!", sep = "")
                    odd += 1
            elif die1 % 2 == 0 and die2 % 2 != 0 or die1 % 2 != 0 and die2 % 2 == 0:
                if die1 == die2 + 1 or die2 == die1 + 1:
                    if die1 in [3,4] and die2 in [3,4]:
                        print(times, ". die roll is *", die1, "* and *", die2, "* Mixed! Neighbor! Middle!", sep = "")
                        mixed += 1
                        neighbor += 1
                        middle += 1
                    else:
                        print(times, ". die roll is *", die1, "* and *", die2, "* Mixed! Neighbor!", sep = "")
                        mixed += 1
                        neighbor += 1
                elif die1 in [1,6] and die2 in [1,6]:
                    print(times, ". die roll is *", die1, "* and *", die2, "* High / Low! Mixed!", sep = "")
                    high_low += 1
                    mixed += 1
                else:
                    print(times, ". die roll is *", die1, "* and *", die2, "* Mixed!", sep = "")
                    mixed += 1

        while sides == 8:
            die1 = random.randint(1,8)
            die2 = random.randint(1,8)
            total1 += die1
            total2 += die2
            times += 1

            if die1 == 1 and die2 == 1:
                print(times, ". die roll is *1* and *1* Odd! Doubles! Snake Eyes!", sep = "")
                odd += 1
                double += 1
                break
            
            elif die1 % 2 == 0 and die2 % 2 == 0:
                if die1 == die2:
                    if die1 + die2 == 8:
                        print(times, ". die roll is *", die1, "* and *", die2, "* Even! Sum Value! Doubles!", sep = "")
                        even += 1
                        sum_value += 1
                        double += 1
                    elif die1 == die2 == 8:
                        print(times, ". die roll is *", die1, "* and *", die2, "* High! Even! Doubles!", sep = "")
                        high += 1
                        even += 1
                        double += 1
                    else:
                        print(times, ". die roll is *", die1, "* and *", die2, "* Even! Doubles!", sep = "")
                        even += 1
                        double += 1
                elif die1 + die2 == 8:
                    print(times, ". die roll is *", die1, "* and *", die2, "* Even! Sum Value!", sep = "")
                    even += 1
                    sum_value += 1
                else:
                    print(times, ". die roll is *", die1, "* and *", die2, "* Even!", sep = "")
                    even += 1
            elif die1 % 2 != 0 and die2 % 2 != 0:
                if die1 == die2:
                    if die1 + die2 == 8:
                        print(times, ". die roll is *", die1, "* and *", die2, "* Odd! Sum Value! Doubles!", sep = "")
                        odd += 1
                        sum_value += 1
                        double += 1
                    else:
                        print(times, ". die roll is *", die1, "* and *", die2, "* Odd! Doubles!", sep = "")
                        odd += 1
                        double += 1
                elif die1 + die2 == 8:
                    print(times, ". die roll is *", die1, "* and *", die2, "* Odd! Sum Value!", sep = "")
                    odd += 1
                    sum_value += 1
                else:
                    print(times, ". die roll is *", die1, "* and *", die2, "* Odd!", sep = "")
                    odd += 1
            elif die1 % 2 == 0 and die2 % 2 != 0 or die1 % 2 != 0 and die2 % 2 == 0:
                if die1 == die2 + 1 or die2 == die1 + 1:
                    if die1 in [4,5] and die2 in [4,5]:
                        print(times, ". die roll is *", die1, "* and *", die2, "* Mixed! Neighbor! Middle!", sep = "")
                        mixed += 1
                        neighbor += 1
                        middle += 1
                    else:
                        print(times, ". die roll is *", die1, "* and *", die2, "* Mixed! Neighbor!", sep = "")
                        mixed += 1
                        neighbor += 1
                elif die1 in [1,8] and die2 in [1,8]:
                    print(times, ". die roll is *", die1, "* and *", die2, "* High / Low! Mixed!", sep = "")
                    high_low += 1
                    mixed += 1
                else:
                    print(times, ". die roll is *", die1, "* and *", die2, "* Mixed!", sep = "")
                    mixed += 1

        while sides == 10:
            die1 = random.randint(1,10)
            die2 = random.randint(1,10)
            total1 += die1
            total2 += die2
            times += 1

            if die1 == 1 and die2 == 1:
                print(times, ". die roll is *1* and *1* Odd! Doubles! Snake Eyes!", sep = "")
                odd += 1
                double += 1
                break
            
            elif die1 % 2 == 0 and die2 % 2 == 0:
                if die1 == die2:
                    if die1 + die2 == 10:
                        print(times, ". die roll is *", die1, "* and *", die2, "* Even! Sum Value! Doubles!", sep = "")
                        even += 1
                        sum_value += 1
                        double += 1

                    elif die1 == die2 == 10:
                        print(times, ". die roll is *", die1, "* and *", die2, "* High! Even! Doubles!", sep = "")
                        high += 1
                        even += 1
                        double += 1
                    else:
                        print(times, ". die roll is *", die1, "* and *", die2, "* Even! Doubles!", sep = "")
                        even += 1
                        double += 1
                elif die1 + die2 == 10:
                    print(times, ". die roll is *", die1, "* and *", die2, "* Even! Sum Value!", sep = "")
                    even += 1
                    sum_value += 1
                else:
                    print(times, ". die roll is *", die1, "* and *", die2, "* Even!", sep = "")
                    even += 1
            elif die1 % 2 != 0 and die2 % 2 != 0:
                if die1 == die2:
                    if die1 + die2 == 10:
                        print(times, ". die roll is *", die1, "* and *", die2, "* Odd! Sum Value! Doubles!", sep = "")
                        odd += 1
                        sum_value += 1
                        double += 1
                    else:
                        print(times, ". die roll is *", die1, "* and *", die2, "* Odd! Doubles!", sep = "")
                        odd += 1
                        double += 1
                elif die1 + die2 == 10:
                    print(times, ". die roll is *", die1, "* and *", die2, "* Odd! Sum Value!", sep = "")
                    odd += 1
                    sum_value += 1
                else:
                    print(times, ". die roll is *", die1, "* and *", die2, "* Odd!", sep = "")
                    odd += 1
            elif die1 % 2 == 0 and die2 % 2 != 0 or die1 % 2 != 0 and die2 % 2 == 0:
                if die1 == die2 + 1 or die2 == die1 + 1:
                    if die1 in [5,6] and die2 in [5,6]:
                        print(times, ". die roll is *", die1, "* and *", die2, "* Mixed! Neighbor! Middle!", sep = "")
                        mixed += 1
                        neighbor += 1
                        middle += 1
                    else:
                        print(times, ". die roll is *", die1, "* and *", die2, "* Mixed! Neighbor!", sep = "")
                        mixed += 1
                        neighbor += 1
                elif die1 in [1,10] and die2 in [1,10]:
                    print(times, ". die roll is *", die1, "* and *", die2, "* High / Low! Mixed!", sep = "")
                    high_low += 1
                    mixed += 1
                else:
                    print(times, ". die roll is *", die1, "* and *", die2, "* Mixed!", sep = "")
                    mixed += 1

        while sides == 12:
            die1 = random.randint(1,12)
            die2 = random.randint(1,12)
            total1 += die1
            total2 += die2
            times += 1

            if die1 == 1 and die2 == 1:
                print(times, ". die roll is *1* and *1* Odd! Doubles! Snake Eyes!", sep = "")
                odd += 1
                double += 1
                break
            
            elif die1 % 2 == 0 and die2 % 2 == 0:
                if die1 == die2:
                    if die1 + die2 == 12:
                        print(times, ". die roll is *", die1, "* and *", die2, "* Even! Sum Value! Doubles!", sep = "")
                        even += 1
                        sum_value += 1
                        double += 1
                    elif die1 == die2 == 12:
                        print(times, ". die roll is *", die1, "* and *", die2, "* High! Even! Doubles!", sep = "")
                        high += 1
                        even += 1
                        double += 1
                    else:
                        print(times, ". die roll is *", die1, "* and *", die2, "* Even! Doubles!", sep = "")
                        even += 1
                        double += 1
                elif die1 + die2 == 12:
                    print(times, ". die roll is *", die1, "* and *", die2, "* Even! Sum Value!", sep = "")
                    even += 1
                    sum_value += 1
                else:
                    print(times, ". die roll is *", die1, "* and *", die2, "* Even!", sep = "")
                    even += 1
            elif die1 % 2 != 0 and die2 % 2 != 0:
                if die1 == die2:
                    if die1 + die2 == 12:
                        print(times, ". die roll is *", die1, "* and *", die2, "* Odd! Sum Value! Doubles!", sep = "")
                        odd += 1
                        sum_value += 1
                        double += 1
                    else:
                        print(times, ". die roll is *", die1, "* and *", die2, "* Odd! Doubles!", sep = "")
                        odd += 1
                        double += 1
                elif die1 + die2 == 12:
                    print(times, ". die roll is *", die1, "* and *", die2, "* Odd! Sum Value!", sep = "")
                    odd += 1
                    sum_value += 1
                else:
                    print(times, ". die roll is *", die1, "* and *", die2, "* Odd!", sep = "")
                    odd += 1
            elif die1 % 2 == 0 and die2 % 2 != 0 or die1 % 2 != 0 and die2 % 2 == 0:
                if die1 == die2 + 1 or die2 == die1 + 1:
                    if die1 in [6,7] and die2 in [6,7]:
                        print(times, ". die roll is *", die1, "* and *", die2, "* Mixed! Neighbor! Middle!", sep = "")
                        mixed += 1
                        neighbor += 1
                        middle += 1
                    else:
                        print(times, ". die roll is *", die1, "* and *", die2, "* Mixed! Neighbor!", sep = "")
                        mixed += 1
                        neighbor += 1
                elif die1 in [1,12] and die2 in [1,12]:
                    print(times, ". die roll is *", die1, "* and *", die2, "* High / Low! Mixed!", sep = "")
                    high_low += 1
                    mixed += 1
                else:
                    print(times, ". die roll is *", die1, "* and *", die2, "* Mixed!", sep = "")
                    mixed += 1

        while sides == 20:
            die1 = random.randint(1,20)
            die2 = random.randint(1,20)
            total1 += die1
            total2 += die2
            times += 1

            if die1 == 1 and die2 == 1:
                print(times, ". die roll is *1* and *1* Odd! Doubles! Snake Eyes!", sep = "")
                odd += 1
                double += 1
                break
            
            elif die1 % 2 == 0 and die2 % 2 == 0:
                if die1 == die2:
                    if die1 + die2 == 20:
                        print(times, ". die roll is *", die1, "* and *", die2, "* Even! Sum Value! Doubles!", sep = "")
                        even += 1
                        sum_value += 1
                        double += 1
                    elif die1 == die2 == 20:
                        print(times, ". die roll is *", die1, "* and *", die2, "* High! Even! Doubles!", sep = "")
                        high += 1
                        even += 1
                        double += 1
                    else:
                        print(times, ". die roll is *", die1, "* and *", die2, "* Even! Doubles!", sep = "")
                        even += 1
                        double += 1
                elif die1 + die2 == 20:
                    print(times, ". die roll is *", die1, "* and *", die2, "* Even! Sum Value!", sep = "")
                    even += 1
                    sum_value += 1
                else:
                    print(times, ". die roll is *", die1, "* and *", die2, "* Even!", sep = "")
                    even += 1
            elif die1 % 2 != 0 and die2 % 2 != 0:
                if die1 == die2:
                    if die1 + die2 == 20:
                        print(times, ". die roll is *", die1, "* and *", die2, "* Odd! Sum Value! Doubles!", sep = "")
                        odd += 1
                        sum_value += 1
                        double += 1
                    else:
                        print(times, ". die roll is *", die1, "* and *", die2, "* Odd! Doubles!", sep = "")
                        odd += 1
                        double += 1
                elif die1 + die2 == 20:
                    print(times, ". die roll is *", die1, "* and *", die2, "* Odd! Sum Value!", sep = "")
                    odd += 1
                    sum_value += 1
                else:
                    print(times, ". die roll is *", die1, "* and *", die2, "* Odd!", sep = "")
                    odd += 1
            elif die1 % 2 == 0 and die2 % 2 != 0 or die1 % 2 != 0 and die2 % 2 == 0:
                if die1 == die2 + 1 or die2 == die1 + 1:
                    if die1 in [10,11] and die2 in [10,11]:
                        print(times, ". die roll is *", die1, "* and *", die2, "* Mixed! Neighbor! Middle!", sep = "")
                        mixed += 1
                        neighbor += 1
                        middle += 1
                    else:
                        print(times, ". die roll is *", die1, "* and *", die2, "* Mixed! Neighbor!", sep = "")
                        mixed += 1
                        neighbor += 1
                elif die1 in [1,20] and die2 in [1,20]:
                    print(times, ". die roll is *", die1, "* and *", die2, "* High / Low! Mixed!", sep = "")
                    high_low += 1
                    mixed += 1
                else:
                    print(times, ". die roll is *", die1, "* and *", die2, "* Mixed!", sep = "")
                    mixed += 1

        high_percent = high / times * 100
        high_low_percent = high_low / times * 100
        even_percent = even / times * 100
        odd_percent = odd / times * 100
        mixed_percent = mixed / times * 100
        sum_value_percent = sum_value / times * 100
        neighbor_percent = neighbor / times * 100
        middle_percent = middle / times * 100
        double_percent = double / times * 100

        print()
        print("You finally got snake eyes on roll #", times, sep = "")
        print("Along the way you rolled HIGH ", high, " time(s). (", format(high_percent, '.2f'), "% of all rolls.)", sep = "")
        print("Along the way you rolled HIGH / LOW ",  high_low, " time(s). (", format(high_low_percent, '.2f'), "% of all rolls)", sep = "")
        print("Along the way you rolled EVEN ", even, " time(s). (", format(even_percent, '.2f'), "% of all rolls.)", sep = "")
        print("Along the way you rolled ODD ", odd, " time(s). (", format(odd_percent, '.2f'), "% of all rolls.)", sep = "")
        print("Along the way you rolled MIXED ", mixed, " time(s). (", format(mixed_percent, '.2f'), "% of all rolls.)", sep = "")
        print("Along the way you rolled SUM VALUE ", sum_value, " time(s). (", format(sum_value_percent, '.2f'), "% of all rolls.)", sep = "")
        print("Along the way you rolled NEIGHBOR ", neighbor, " time(s). (", format(neighbor_percent, '.2f'), "% of all rolls.)", sep = "")
        print("Along the way you rolled MIDDLE ", middle, " time(s). (", format(middle_percent, '.2f'), "% of all rolls.)", sep = "")
        print("Along the way you rolled DOUBLE ", double, " time(s). (", format(double_percent, '.2f'), "% of all rolls.)", sep = "")
        print("Along the way you rolled SNAKE EYES 1 time. (", format(1 / times * 100, '.2f'), "% of all rolls.)", sep = "")
        print("Average roll for die #1:", format(total1 / times, '.2f'))
        print("Average roll for die #2:", format(total2 / times, '.2f'))
        break    
    else:
        print("Invalid size, try again.")
        continue
