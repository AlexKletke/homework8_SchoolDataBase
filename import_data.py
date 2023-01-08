# модуль Добавление данных
 
"""def import_data(data, table = None):
    with open('phone_book.csv', 'a+') as file:
        if table == None:
            for i in data:
                file.write(f"{i}\n")
            file.write(f"\n")
        else:
            file.write(table.join(data))
            file.write(f"\n")"""

def import_data(data, table):
    for id in enumerate(data, start=1):
        if table == 1:
            with open('student_database.csv', 'a+') as f1:
                f1.write(id.join(data))
                f1.write(f"\n")
            """f1.write(f"{data[0]}\n")
            f1.write(f"{data[1]}\n")
            f1.write(f"{data[2]}\n")
            f1.write(f"{data[3]}\n")"""
            """for i in data:
                f1.write(f"{i[0]}\n")
                f1.write(f"{i[1]}\n")
                f1.write(f"{i[2]}\n")
                f1.write(f"{i[3]}\n")
            f1.write(f"\n")"""
        elif table == 2:
            with open('lesson_database.csv', 'a+') as f2:
                f2.write(id.join(data))
                f2.write(f"\n")
        else:
            with open('symbolclass_database.csv', 'a+') as f3:
                f3.write(id.join(data))
                f3.write(f"\n")