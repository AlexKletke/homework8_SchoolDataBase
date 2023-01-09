"""from User_Interface import user_choice
from Student_DataBase import read_file

def request_processing(list, n):
    a = []
    if n == 8:
        return list
    elif 0 < n < 8:
        for i in list:
            a.append(i[n-1])
        return a
    else:
        return 'Всего доброго' """

def request_processing():
    choice_query = input("Выберите запрос:\n\
    1 - вывод всех ФИО учеников первых классов;\n\
    2 - вывод всех дней рождения учеников;\n\
    3 - вывод плохой успеваемости учеников;\n\
    4 - вывод мальчиков учеников;\n\
    5 - вывод номеров класса, где есть девочки;\n\
    6 - вывод учеников 2Б класса. Введите цифру:")
    if choice_query == 1:
        with open('student_database.csv', 'r') as file1:
            data1 = []
            for line in file1:
                if line != '\n':
                    data1.append(line.strip())
            res1 = []
            temp = []
            for i in range(len(data1)):
                temp = data1[i].split(',')
                res1.append(temp)
                #res1.append(list(data1[i].split()))
            result1 = []
            for i in range(len(res1)):
                if res1[i[7]] == 1:
                    result1.append(res1[i[1]], res1[i[2]], res1[i[3]])
                    result = result1
    return result

