import json
from datetime import datetime

def read_file(path=r'../operations.json'):
    """
    :return: считываем файл operations.json
    """
    with open(path, 'r', encoding='UTF-8') as file:
        return json.load(file)


def formated_date(data : list[dict]) -> list[dict]:
    """
    :param data: Передаем словарь operations.json в виде аргумента
    :return: дату в формате ДД.ММ.ГГГГ
    """
    new_list = []
    for item in data:
        if item:
            read_date = item.get('date')
            split_date = (read_date.split('T')[0].split('-'))
            format_date = '.'.join(split_date[::-1])
            item['date'] = format_date
            new_list.append(item)

    return new_list


def sorted_date(data : list[dict]) -> list[dict]:
    """
    сортирует и возвращает дату по убыванию
    """
    data = sorted(data, key=lambda x: datetime.strptime(x['date'], '%d.%m.%Y'), reverse=True)
    return data


def executed_last_five(data : list[dict]) -> list[dict]:
    """
    получаем операции со значением EXECUTED
    :return: последние 5 успешных EXECUTED по времени
    """
    new_list = []
    for item in data:
        get_executed = item.get('state')
        if get_executed == 'EXECUTED':
            new_list.append(item)

    return new_list[:5]


def mask_card(data:str) -> str:
    """
    маскируем номер карты в формате Visa Platinum 7000 79** **** 6361
    """
    info_from = data.rsplit(' ', 1)
    return f'{info_from[0]} {info_from[-1][0:4]} {info_from[-1][4:6]}** **** {info_from[-1][-4:]}'


def mask_bill(data: str) -> str:
    """
    маскируем номер счёта  в формате Счет **9638
    """
    info_from = data.rsplit(' ', 1)
    return f'{info_from[0]} **{info_from[-1][-4:]}'


def mask_numbers_from_and_to(data:list[dict]) -> list[dict]:
    """
    Проходим циклом список, выдёргиваем по ключам ('from' и 'to') данные. Делаем условие, если по ключу 'from'
    в строке нет слова 'Счет' маскируем только карту. Если есть то маскируем счёт. И также для ключа 'to'.
    :return: Возвращаем измененный список
    """
    list_card = []
    for item in data:
        get_from = item.get('from')
        get_to = item.get('to')

        if get_from and 'Счет' not in get_from:
            card_from = mask_card(get_from)
            item['from'] = card_from
        else:
            if get_from:
                bill_from = mask_bill(get_from)
                item['from'] = bill_from

        if 'Счет' not in get_to:
            card_to = mask_card(get_to)
            item['to'] = card_to
        else:
            bill_to = mask_bill(get_to)
            item['to'] = bill_to
        list_card.append(item)

    return list_card