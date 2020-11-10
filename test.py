import csv
import re

class Dataset:

    def __init__(self, date, order_status, company, courier_name, courier_phone, client_address, to_restaurant, to_client, delivery_status):
        self.date = date
        self.order_status = order_status
        self.company = company
        self.courier_name = courier_name
        self.courier_phone = courier_phone
        self.client_address = client_address
        self.to_restaurant = to_restaurant
        self.to_client = to_client
        self.delivery_status = delivery_status


    def __repr__(self):
        return f'{self.date, self.order_status, self.company, self.courier_name, self.courier_phone, self.client_address, self.to_restaurant, self.to_client, self.delivery_status}'

my_str = """smdelivery, [Oct 31, 2020 at 2:49:37 PM]:
Зміни у замовленні: Magic_Bowls ⇾ NazarKaiser 0931841898 ⇾ Городоцька 226а :: До закладу 14:55 :: До клієнта  :: зайнята

smdelivery, [Oct 31, 2020 at 2:49:50 PM]:
Зміни у замовленні: Magic_Bowls ⇾ NazarKaiser 0931841898 ⇾ Кульпарківська 226 Л, кв.17 :: До закладу 14:55 :: До клієнта  :: зайнята

smdelivery, [Oct 31, 2020 at 2:51:23 PM]:
Зміни у замовленні: Magic_Bowls ⇾ NazarKaiser 0931841898 ⇾ Кульпарківська 226 Л, кв.17 :: До закладу 15:05 :: До клієнта  :: зайнята

smdelivery, [Oct 31, 2020 at 2:51:35 PM]:
Зміни у замовленні: Magic_Bowls ⇾ NazarKaiser 0931841898 ⇾ Городоцька 226а :: До закладу 15:05 :: До клієнта  :: зайнята"""

def converter(message: str):
    res = re.findall(r'smdelivery, \[(.*)\]:\n(.*): (.*) ⇾ (.*) (.*) ⇾ (.*) :: До закладу (.*) :: До клієнта (.*) :: (.*)', message)
    output_list = []
    for line in res:
        data = Dataset(*line)
        output_list.append(data)

    return output_list


headers = Dataset('Дата', 'Статус замовлення', 'Компанія' , 'Ім\'я кур\'єра', 'Номер кур\'єра', 'Адреса клієнта', 'До закладу', 'До клієнта', 'Статус доставки')


def csv_writer():
    message = converter(my_str)
    with open('message.csv', 'w') as file_csv:
        f = (headers.date, headers.order_status, headers.company, headers.courier_name, headers.courier_phone, headers.client_address, headers.to_restaurant, headers.to_client, headers.delivery_status)
        writer = csv.DictWriter(file_csv, fieldnames=f)
        writer.writeheader()
        for line in message:
            file_csv.write(str(line))


csv_writer()



