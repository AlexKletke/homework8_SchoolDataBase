# модуль Вывод данных 

def export_data(table):
    if table == 1:
        with open('student_database.csv', 'r') as file1:
            data1 = []
            for line in file1:
                if line != '\n':
                    data1.append(line.strip())
                data = data1
    if table == 2:
        with open('lesson_database.csv', 'r') as file2:
            data2 = []
            for line in file2:
                if line != '\n':
                    data2.append(line.strip())
                data = data2
    else:
        with open('symbolclass_database.csv', 'r') as file3:
            data3 = []
            for line in file3:
                if line != '\n':
                    data3.append(line.strip())
                data = data3
        # t = []
            """for line in file2:
                if ',' in line:
                # temp = line.strip().split(',')
                    temp = line.split(',')
                    data2.append(temp)
                elif ';' in line:
                    temp = line.split(';')
                    data2.append(temp)
                elif '-' in line:
                    temp = line.split('-')
                    data2.append(temp)
                elif '*' in line:
                    temp = line.split('*')
                    data2.append(temp)
                data = data2 """

            """elif line != '':
                if line != '\n':
                    t.append(line.strip())
                else:
                    data.append(t)
                    t= []"""
    return data