from User_Interface import user_choice
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
        return 'Всего доброго'
