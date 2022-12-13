#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime
import sys
from datetime import date

if __name__ == '__main__':
    persons = []

    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == 'add':
            name = input("Фамилия и Имя? ")
            sign = input("Знак зодиака? ")
            date = input("Дата рождения? ")
            person = {
                'name': name,
                'sign': sign,
                'date': date,
            }
            persons.append(person)

            if len(persons) > 1:
                persons.sort(key=lambda item: item.get('sign', ''))

        elif command == 'list':
            line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 20,
                '-' * 8
            )
            print(line)
            print(
                '| {:^4} | {:^30} | {:^20} | {:^8} |'.format(
                    "No",
                    "Ф.И.О.",
                    "Знак",
                    "Дата рождения"
                )
            )
            print(line)

            for idx, worker in enumerate(persons, 1):
                print(
                    '| {:>4} | {:<30} | {:<20} | {:>8} |'.format(
                        idx,
                        worker.get('name', ''),
                        worker.get('sign', ''),
                        worker.get('date', 0)
                    )
                )

            print(line)

        elif command == 'show sign':
            selected_sign = input("What sign? ")
            date_format = "%d.%m.%Y"

            for person in persons:
                right_person_found = False
                if person['sign'] == selected_sign:
                    print(person['name'], person['sign'], datetime.datetime.strptime(person['date'], date_format))
                    right_person_found = True
                if not right_person_found:
                    print("Нет людей со знаком ", selected_sign)

        elif command == 'help':
            print("Список команд:\n")
            print("add - добавить человека;")
            print("list - вывести список людей;")
            print("show sign - запросить людей с определенным знаком зодиака;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
