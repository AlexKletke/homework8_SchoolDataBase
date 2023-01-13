from import_data import import_data
from delete_data import delete_data
from export_data import export_data
from redact_data import redact_data
from Query_Manager import request_processing

def greeting():
    print("Добро пожаловать в информационную систему, позволяющую работать с учениками школы")

def input_data(table):
    #table = choice_table()
    str_dataofstudent = ''
    if table == 1:
        last_name = input("Введите фамилию ученика: ")
        str_dataofstudent += last_name + ' '
        first_name = input("Введите имя ученика: ")
        str_dataofstudent += first_name + ' '
        patronymic_name = input("Введите отчество ученика: ")
        str_dataofstudent += patronymic_name + ' '
        birthday_student = input("Введите дату рождения ученика: ")
        str_dataofstudent += birthday_student + ' '
        academic_performance = input("Успеваемость ученика (удовл, хор, отл): ")
        str_dataofstudent += academic_performance + ' '
        sex_student = input("Введите пол ученика (муж, жен): ")
        str_dataofstudent += sex_student + ' '
        class_number = input("Введите номер класса ученика: ")
        str_dataofstudent += class_number + ' '
        class_letter = input("Введите букву класса ученика: ")
        str_dataofstudent += class_letter
        return str_dataofstudent#[last_name, first_name, patronymic_name, birthday_student, academic_performance, sex_student, class_number, class_letter]
    elif table == 2:
        Lesson_name = input("Введите название урока: ")
        return Lesson_name
    elif table == 3:
        class_number = input("Введите номер класса: ")
        class_letter = input("Введите букву класса: ")
        return [class_number, class_letter]
    else:
        print('введите, пожалуйста, номер таблицы с 1 до 3')
        table = choice_table()

def choice_table():
    table = int(input("Есть 3 таблицы данных: 1 - таблица учеников школы; 2 - таблица всех уроков в школе; 3 - таблица всех классов в школе. Какая таблица вас интересует: "))    
    return table
def choice_id_line():
    id_line = int(input("Введите номер id записи для удаления или корректировки (номер): "))
    return id_line
def school_InfSystem_functionality():
    print("Что вы можете сделать:\n\
    1 - добавление данных;\n\
    2 - удаление данных;\n\
    3 - корректировка данных;\n\
    4 - вывод данных;\n\
    5 - выборка данных, запросы.")
    choice = input(" Что вы хотите сделать - введите цифру: ")
    if choice == '1':
        table = choice_table()        
        import_data(input_data(table), table)
    elif choice == '2':
        table = choice_table()
        id_line = choice_id_line()
        delete_data(table, id_line)
    elif choice == '3':
        table = choice_table()
        id_line = choice_id_line()
        redact_data(table, id_line)
    elif choice == '4':
        table = choice_table()
        #export_data(table)
        #data = export_data(table)
        print(*export_data(table))
    elif choice == '5':
        #result1 = ''
        #request_processing()
        data = request_processing()
        print(data)
        