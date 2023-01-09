# модуль редактирования данных

def redact_data(table, id_line):
    if table == 1:
        lines = open('student_database.csv', 'r').readlines()
        print(f"данные для корректировки: {lines[id_line-1]}")
        lines[id_line-1] = input('введите новые данные, соблюдая те же знаки препинания: ')
        out = open('student_database.csv', 'w')
        out.writelines(lines)
        out.close()
    elif table == 2:
        lines = open('lesson_database.csv', 'r').readlines()
        print(f"данные для корректировки: {lines[id_line-1]}")
        lines[id_line-1] = input('введите новые данные, соблюдая те же знаки препинания: ')
        out = open('lesson_database.csv', 'w')
        out.writelines(lines)
        out.close()
    else:
        lines = open('symbolclass_database.csv', 'r').readlines()
        print(f"данные для корректировки: {lines[id_line-1]}")
        lines[id_line-1] = input('введите новые данные, соблюдая те же знаки препинания: ')
        out = open('symbolclass_database.csv', 'w')
        out.writelines(lines)
        out.close()