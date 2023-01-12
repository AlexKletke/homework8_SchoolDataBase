# модуль редактирования данных

def redact_data(table, id_line):
    if table == 1:
        lines = open('student_database.txt', 'r').readlines()
        print(f"данные для корректировки: {lines[id_line-1]}")
        lines[id_line-1] = input('введите новые данные, соблюдая те же знаки препинания: ')
        out = open('student_database.txt', 'w')
        out.writelines(lines)
        out.write(f"\n")
        out.close()
    elif table == 2:
        lines = open('lesson_database.txt', 'r').readlines()
        print(f"данные для корректировки: {lines[id_line-1]}")
        lines[id_line-1] = input('введите новые данные, соблюдая те же знаки препинания: ')
        out = open('lesson_database.txt', 'w')
        out.writelines(lines)
        out.write(f"\n")
        out.close()
    else:
        lines = open('symbolclass_database.txt', 'r').readlines()
        print(f"данные для корректировки: {lines[id_line-1]}")
        lines[id_line-1] = input('введите новые данные, соблюдая те же знаки препинания: ')
        out = open('symbolclass_database.txt', 'w')
        out.writelines(lines)
        out.write(f"\n")
        out.close()