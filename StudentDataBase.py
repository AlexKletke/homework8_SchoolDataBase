list = [['1', 'Пермин Александр Владимирович', '01.01.2015', 'хор', 'муж', '1', 'А'], ['2', 'Хомяков Борис Глебович', '02.02.2015', 'отл', 'муж', '1', 'А'], 
['3', 'Охлобыстин Павел Рудольфович', '03.03.2015', 'хор', 'муж', '1', 'А'], ['4', 'Ширяев Константин Александрович', '01.01.2014', 'хор', 'муж', '2', 'Б'], 
['5', 'Шмякин Аргентин Семенович', '02.02.2014', 'хор', 'муж', '2', 'Б'], ['6', 'Иванов Дэвид Александрович', '03.03.2014', 'отл', 'муж', '2', 'Б'], 
['7', 'Петров Дмитрий Павлович', '04.04.2013', 'удовл', 'муж', '3', 'В'], ['8', 'Сидоров Олег Борисович', '05.05.2013', 'отл', 'муж', '3', 'В'], 
['9', 'Умаров Владимир Алексеевич', '06.06.2012', 'удовл', 'муж', '4', 'Г'], ['10', 'Юпитин Карл Семенович', '07.07.2012', 'удовл', 'муж', '4', 'Г'], 
['11', 'Разина Людмила Ивановна', '05.04.2012', 'хор', 'жен', '4', 'Г'], ['12', 'Портова Алла Юрьевна', '03.02.2012', 'отл', 'жен', '4', 'Г']]
def read_file(file):
    f = open(file, 'r')
    data = f.read().splitlines()
    list = []
    for line in data:
        line = line.split(';')
        list.append(line)
    f.close()
    return list
# data = 'processing_model.csv'
# print(read_file(data))


def write_file(list, mod):
    f = open('result.csv', mod)
    # for line in list:
    #     f.writelines(line)  ДЛЯ ОБЫЧНОГО СПИСКА
    #     f.writelines(';')
    for i in range(len(list)):
        for j in range(len(list[i])):
            f.writelines(list[i][j])
            f.writelines(';')
        f.writelines('\n')
    f.close()
    if mod == 'a':
        print('Данные записаны')
    if mod == 'w':
        print('Данные перезаписаны')

mod = 'w'
write_file(list, mod)