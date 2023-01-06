# модуль User_Interface
# функция def user_choice
# Обращается к  пользователю для выбора действия

def user_choice():
    while True:
        user_input = input('''
        1 - вывод ID, 2 - вывод ФИО 
        3 - вывод всех дней рождения, 4 - вывод успеваемости
        5 - вывод пола, 6 - вывод всех данных
        0 - выход\n
        Выберите действие: ''')
        try:
            user_input = int(user_input)
        except:
            print('Введите цифру')
            continue
        if user_input >= 0 and user_input <= 6:
            return user_input
        else:
            print('Выбрать нужно от 0 до 6')


if __name__ == '__main__':
    user_choice()