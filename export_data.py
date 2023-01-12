# модуль Вывод данных 

def export_data(table):
    if table == 1:
        with open('student_database.txt', 'r') as f1:
            data1 = []
            for line in f1:
                if line != '\n':
                    data1.append(line.strip())
        data = data1
    if table == 2:
        with open('lesson_database.txt', 'r') as file2:
            data2 = []
            for line in file2:
                if line != '\n':
                    data2.append(line.strip())
        data = data2
    else:
        with open('symbolclass_database.txt', 'r') as file3:
            data3 = []
            for line in file3:
                if line != '\n':
                    data3.append(line.strip())
        data = data3       
    return data