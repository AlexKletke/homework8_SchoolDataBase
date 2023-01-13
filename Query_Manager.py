def request_processing():
    choice_query = int(input("Выберите запрос:\n\
    1 - вывод всех ФИО учеников первых классов;\n\
    2 - вывод всех дней рождения учеников;\n\
    3 - вывод плохой успеваемости учеников;\n\
    4 - вывод мальчиков учеников;\n\
    5 - вывод номеров класса, где есть девочки;\n\
    6 - вывод всех учеников нужного класса: "))
    with open('student_database.txt', 'r') as file1:
        data1 = []
        temp = []
        for line in file1:
            if line != '\n':
                data1.append(line.strip()) #
        #print(data1)
        result = ''
        for i in range(len(data1)):
            temp = data1[i].split()
            #print(temp)
            
            #print(type(temp[6]))
            if choice_query == 1:
                temp[6] = int(temp[6])                
                if temp[6] == 1:
                    #print(f"{temp[0]} {temp[1]} {temp[2]} \n")
                    result += temp[0] + ' ' + temp[1] + ' ' + temp[2] + '\n'
            #print(result)
            if choice_query == 2:
                result += temp[3] + ' ' + temp[0] + ' ' + temp[1] + ' ' + temp[2] + '\n'
            if choice_query == 3:
                if temp[4] == 'удовл':
                    result += temp[4] + ' ' + temp[0] + ' ' + temp[1] + ' ' + temp[2] + ' ' + temp[6] + temp[7] + '\n'
            if choice_query == 4:
                if temp[5] == 'муж':
                    result += temp[0] + ' ' + temp[1] + ' ' + temp[2] + '\n'
            if choice_query == 5:
                if temp[5] == 'жен':
                    result += temp[6] + temp[7] + '\n'
            if choice_query == 6:
                a = input("введите номер интересующего класса (только цифру): ")
                b = input("введите букву интересующего класса: ")
                b.lower()
                if temp[6] == a and temp[7] == b.lower():
                    result += temp[0] + ' ' + temp[1] + ' ' + temp[2] + '\n'
        return result


        #if choice_query == 1:

        """res1 = []
        temp = []
        for i in range(len(data1)):
            temp = data1[i].split(',')
            res1.append(temp)
        print(*f'{temp}\n  {res1}\n')
    if choice_query == 1:                
        result = [[]]
        for i in range(len(res1)):
            if res1[i[6]] == "   ' 1 ' ":
                result.append(res1[i[0]]) #, res1[i[1]], res1[i[2]], res1[i[3]]
        #result = result
        return result
    if choice_query == 2:
        result2 = []
        for i in range(len(res1)):
            result2.append(res1[i[0]], res1[i[1]], res1[i[2]], res1[i[3]], res1[i[4]])
        #result = result2
        return result2
    if choice_query == 3:                
        result3 = []
        for i in range(len(res1)):
            if res1[i[5]] == 'удовл':
                result3.append(res1[i[0]], res1[i[1]], res1[i[2]], res1[i[3]], res1[i[5]], res1[i[7]], res1[i[8]])
        result = result3
    if choice_query == 4:                
        result4 = []
        for i in range(len(res1)):
            if res1[i[6]] == 'муж':
                result4.append(res1[i[0]], res1[i[1]], res1[i[2]], res1[i[3]])
        result = result4
    if choice_query == 5:                
        result5 = []
        for i in range(len(res1)):
            if res1[i[6]] == 'жен':
                result5.append(res1[i[7]], res1[i[8]])
        result = result5
    if choice_query == 6:                
        result6 = []
        a = input("введите номер интересующего класса (только цифру): ")
        b = input("введите букву интересующего класса: ")
        for i in range(len(res1)):
            if res1[i[7]] == a and res1[i[8]] == b:
                result6.append(res1[i[0]], res1[i[1]], res1[i[2]], res1[i[3]])
        result = result6       """
    #return result

