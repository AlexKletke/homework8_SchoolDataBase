# модуль Удаления данных

def delete_data(table, id_line):
    if table == 1:
        lines = open('student_database.txt', 'r').readlines()
        lines[id_line-1] = ''
        out = open('student_database.txt', 'w')
        out.writelines(lines)
        out.close()
    elif table == 2:
        lines = open('lesson_database.txt', 'r').readlines()
        lines[id_line-1] = ''
        out = open('lesson_database.txt', 'w')
        out.writelines(lines)
        out.close()
    else:
        lines = open('symbolclass_database.txt', 'r').readlines()
        lines[id_line-1] = ''
        out = open('symbolclass_database.txt', 'w')
        out.writelines(lines)
        out.close()
