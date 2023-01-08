from import_data import import_data
from export_data import export_data
from print_data import print_data

def greeting():
    print("Добро пожаловать в информационную систему, позволяющую работать с учениками школы")

def input_data():
    last_name = input("Введите фамилию ученика: ")
    first_name = input("Введите имя ученика: ")
    patronymic_name = input("Введите отчество ученика: ")
    birthday_student = input("Введите дату рождения ученика: ")
    academic_performance = input("Успеваемость ученика (удовл, хор, отл): ")
    sex_student = input("Введите пол ученика (муж, жен): ")
    class_number = input("Введите номер класса ученика: ")
    class_letter = input("Введите букву класса ученика: ")
    return [last_name, first_name, patronymic_name, birthday_student, academic_performance, sex_student, class_number, class_letter]

def choice_separator():
    separator = input("Есть 2 варианта записи. Введите разделитель: ")
    if separator == "":
        separator = None
    return separator

def school_InfSystem_functionality():
    print("Что вы можете сделать:\n\
    1 - добавление данных;\n\
    2 - удаление данных;\n\
    3 - корректировка данных;\n\
    4 - вывод всех данных;\n\
    5 - вывод всех ФИО учеников первых классов;\n\
    6 - вывод всех дней рождения учеников;\n\
    7 - вывод плохой успеваемости учеников;\n\
    8 - вывод мальчиков учеников;\n\
    9 - вывод номеров класса, где есть девочки;\n\
    10 - вывод учеников 2Б класса.")
    choice = input(" Что вы хотите сделать - введите цифру: ")
    if choice == '1':
        separator = choice_separator()
        import_data(input_data(), separator)
    elif choice == '2':
        separator = choice_separator()
        export_data(separator)
        data = export_data(separator)
        print_data(data, separator)