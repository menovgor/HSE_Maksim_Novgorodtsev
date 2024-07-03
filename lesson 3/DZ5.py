"""
1. Найдите информацию об организациях.
"""

import json
import csv

with open('traders.txt', 'r') as file:
    inn_list = [line.strip() for line in file]

with open('traders.json', 'r') as file:
    traders_data = json.load(file)

data_to_write = []

for trader in traders_data:
    if trader['inn'] in inn_list:
        data_to_write.append({
            'inn': trader['inn'],
            'ogrn': trader['ogrn'],
            'address': trader['address']
        })

# Сохранение в файл
with open('traders.csv', 'w', newline='') as csvfile:
    fieldnames = ['inn', 'ogrn', 'address']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for row in data_to_write:
        writer.writerow(row)

"""
2. Напишите регулярное выражение для поиска email-адресов в тексте.
"""
import re
def find_emails(text):
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, text)
    return emails


import json

with open('1000_efrsb_messages.json', 'r') as file:
    dataset = json.load(file)

# Словарь для хранения email
email_dict = {}

# Обработка каждого сообщения
for record in dataset:
    inn = record['publisher_inn']
    message = record['msg_text']
    emails = find_emails(message)

    if emails:
        if inn not in email_dict:
            email_dict[inn] = set()
        email_dict[inn].update(emails)

# Сохранение в файл
with open('emails.json', 'w') as file:
    json.dump({inn: list(emails) for inn, emails in email_dict.items()}, file, indent=4)
