# модуль Добавление данных
 
def import_data(data, table):
    if table == 1:
        #with open('student_database.txt', 'r') as read_object:
           # lines = read_object.readlines()
        with open('student_database.txt', 'a') as f1:
            #f1.write(f'{len(lines)+1}, {data}')
            f1.writelines(f'{data}')
            f1.write(f"\n")            
    elif table == 2:
        with open('lesson_database.txt', 'a') as f2:            
            f2.writelines(f'{data}')
            f2.write(f"\n")       
    else:       
        with open('symbolclass_database.txt', 'a') as f3:
            f3.writelines(f'{data}')
            f3.write(f"\n")


            