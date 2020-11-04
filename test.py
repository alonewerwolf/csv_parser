import csv
import re

my_str = 'Зміни у замовленні: SalalatKr ⇾ Кактус 0995405779 ⇾ Городоцька 315 :: До закладу 11:20 :: До клієнта 11:45 :: в дорозі '


def converter(message: str):
    res = re.findall(r'(.*): (.*) ⇾ (.*) (.*) ⇾ (.*) :: До закладу (.*) :: До клієнта (.*) :: (.*)', message)
    if len(res) > 0:
        res = res[0]
    else:
        res = None

    return res


def csv_writer():
    message = converter(my_str)
    with open('message.csv', 'w') as file_csv:
        field_name = ['Статус замовлення', 'Компанія', 'Імʼя курʼєра', 'Номер курʼєра', 'Адрес клієнта', 'До закладу',
                      'До клієнта', 'Статус доставки']
        writer = csv.DictWriter(file_csv, fieldnames=field_name)
        writer.writeheader()
        writer.writerow({'Статус замовлення': f'{message[0]}',
                         'Компанія': f'{message[1]}',
                         'Імʼя курʼєра': f'{message[2]}',
                         'Номер курʼєра': f'{message[3]}',
                         'Адрес клієнта': f'{message[4]}',
                         'До закладу': f'{message[5]}',
                         'До клієнта': f'{message[6]}',
                         'Статус доставки': f'{message[7]}'})


csv_writer()
