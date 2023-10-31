
while True:
    print('NYU Quizzing System - Main Menu')
    option = input('(q)uiz info, (s)core a file or (e)xit:')
    if option == 'e':
        print('Goodbye!')
        break
    elif option == 'q':
        file_handle = open("quizzes.txt")
        data = file_handle.read()
        file_handle.close()
        lines = data.split("\n")
        for item in lines:
            info = item.split(",")
            print(info[0], 'has', len(info[1]), 'questions')
    elif option == 's':
        filename = input('Enter a filename to score:')
        try:
            file_handle = open(filename, 'r')
        except:
            print('File does not exist')
        else:
            data = file_handle.read()
            file_handle.close()

            lines = data.split("\n")
            print('This file contains', len(lines[1:]) - 1, 'student entries for the test "' + lines[0] + '"')
        try:
            file_handle = open("quizzes.txt", "r")
            data = file_handle.read()
            file_handle.close()
        except:
            print("Can't open quizzes file")
        else:
            quiz_lines = data.split('\n')
            for l in quiz_lines:
                items = l.split(',')
                if items[0] == lines[0]:
                    answerkey = items[1]
            print('The answer key for this test is:', answerkey)


        sum = 0
        list = []
        unique = []
        count = []
        
        for j in range(len(lines[1:]) - 1):
            correct = 0
            percent = 0

            
            for k in range(len(lines[j + 1].split(',')[1])):
                if lines[j + 1].split(',')[1][k] == answerkey[k]:
                    correct += 1
                    sum += 1
            
                percent = format(float(correct / len(answerkey) * 100), '.2f')
            list += [correct]
            print(lines[j + 1].split(',')[0], 'earned', correct, 'out of', len(answerkey), '(' + percent + '%)' )

        for t in list:
            if t not in unique:
                unique.append( t )
                count.append(1)
            else:
                position = unique.index( t )
                count[ position ] += 1

        highest_score = []
        highest = max(count)
        for m in range(len(unique)):
            if count[m] == highest:
                highest_score.append(unique[m])
               
        print()
        print('*** Class Report ***')
        print('Average score:', format(float(sum / (len(lines[1:]) - 1)), '.2f'))
        print('Highest score:', max(list))
        print('Lowest score:', min(list))
        print('Range of scores:', max(list) - min(list))
        print('Mode(s):', end = ' ' )
        for i in range(len(highest_score)):
            print(highest_score[i], end = ' ')
        print()
        
        for k in range(len(lines[j + 1].split(',')[1]) + 1):
            print(format(k, '>2'), end = ' ')
            for t in unique:
                if k == t:
                    print('*' * count[unique.index(t)], end = '')
            print()

        print()
        class_scored = open(filename[0:len(filename) - 4] + '_scored.txt', 'w')
        for j in range(len(lines[1:]) - 1):
            correct = 0
            percent = 0

            
            for k in range(len(lines[j + 1].split(',')[1])):
                if lines[j + 1].split(',')[1][k] == answerkey[k]:
                    correct += 1
            
                percent = format(float(correct / len(answerkey) * 100), '.2f')
            list += [correct]
            
            class_scored.write(lines[j + 1].split(',')[0] + ',' + percent + '\n')

        class_scored.close()
                  


