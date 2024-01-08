# используется для сортировки
from operator import itemgetter


class Det:
    """Деталь"""
    def __init__(self, id, size, cost, Sup_id):
        self.id = id
        self.size = size
        self.cost = cost
        self.Sup_id = Sup_id


class Sup:
    """Поставщик"""
    def __init__(self, id, name):
        self.id = id
        self.name = name


class DetSup:
    """
    'Деталь от поставщика' для реализации
    связи многие-ко-многим
    """
    def __init__(self, Sup_id, Det_id):
        self.Sup_id = Sup_id
        self.Det_id = Det_id


# Отделы
Sups = [
    Sup(1, 'Ротбанд'),
    Sup(2, 'Петрович'),
    Sup(3, '100+'),


    Sup(11, 'Пемолюкс'),
    Sup(22, 'Кнауф'),
    Sup(33, 'Все смеси'),
]


# Сотрудники
Dets = [
    Det(1, '25x30x96', 250, 1),
    Det(2, '25x32x96', 350, 2),
    Det(3, '25x36x96', 450, 3),
    Det(4, '32x30x66', 350, 3),
    Det(5, '35x30x80', 200, 3),
]


Dets_Sups = [
    DetSup(1,1),
    DetSup(2,2),
    DetSup(3,3),
    DetSup(3,4),
    DetSup(3,5),


    DetSup(11,1),
    DetSup(22,2),
    DetSup(33,3),
    DetSup(33,4),
    DetSup(33,5),
]


def main():
    """Основная функция"""


    # Соединение данных один-ко-многим
    one_to_many = [(e.size, e.cost, d.name)
        for d in Sups
        for e in Dets
        if e.Sup_id==d.id]

    # Соединение данных многие-ко-многим
    many_to_many_tDet = [(d.name, ed.Sup_id, ed.Det_id)
        for d in Sups
        for ed in Dets_Sups
        if d.id==ed.Sup_id]

    many_to_many = [(e.size, e.cost, Sup_name)
        for Sup_name, Sup_id, Det_id in many_to_many_tDet
        for e in Dets if e.id==Det_id]


    print('Задание А1')
    res_11 = sorted(one_to_many, key=itemgetter(2))
    print(res_11)

    print('\nЗадание А2')
    res_12_unsorted = []
    # Перебираем все отделы
    for d in Sups:
        # Список сотрудников отдела
        d_Dets = list(filter(lambda i: i[2]==d.name, one_to_many))
        # Если отдел не пустой
        if len(d_Dets) > 0:
            # Зарплаты сотрудников отдела
            d_sals = [sal for _,sal,_ in d_Dets]
            # Суммарная зарплата сотрудников отдела
            d_sals_sum = sum(d_sals)
            res_12_unsorted.append((d.name, d_sals_sum))


    # Сортировка по суммарной зарплате
    res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=True)
    print(res_12)


    print('\nЗадание А3')
    res_13 = {}
    # Перебираем все отделы
    for d in Sups:
        if 'отдел' in d.name:
            # Список сотрудников отдела
            d_Dets = list(filter(lambda i: i[2]==d.name, many_to_many))
            # Только ФИО сотрудников
            d_Dets_names = [x for x,_,_ in d_Dets]
            # Добавляем результат в словарь
            # ключ - отдел, значение - список фамилий
            res_13[d.name] = d_Dets_names


    print(res_13)


if __name__ == '__main__':
    main()
