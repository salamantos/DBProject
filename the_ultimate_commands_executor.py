# coding=utf-8

from requests import *
import sqlite3

if __name__ != "__main__":
    exit(0)


def show_res(show_get_template, show_get_res):
    # Считаем максимальную длину сроки в каждой колонке
    rows_len = []
    columns_count = len(show_get_template)
    for elem in show_get_template:
        rows_len.append(len(str(elem)))
    for elem in show_get_res:
        i = 0
        for member in elem:
            rows_len[i] = max(rows_len[i], len(str(member)))
            i += 1

    table_width = 1 + columns_count * 3
    for elem in rows_len:
        table_width += elem
    print('|', end='')
    for i in range(columns_count):
        print(' {}{}|'.format(show_get_template[i], ' ' * (rows_len[i] - len(str(show_get_template[i])) + 1)), end='')

    print('\n+{}+'.format('-' * (table_width - 2)))
    for elem in show_get_res:
        print('|', end='')
        for i in range(columns_count):
            print(' {}{}|'.format(elem[i], ' ' * (rows_len[i] - len(str(elem[i])) + 1)), end='')
        print()
        print('+{}+'.format('-' * (table_width - 2)))


invite_text = '''Введите команду (напр. "1")
  0 - выход
  1 - показать список шуток
  2 - показать шутки с рейтингом > 90%
  3 - вывести подробности по конкретной шутке
  4 - информация о разыгранных людях\n'''

con = sqlite3.connect('AprilFoolsJokes.db')
con.row_factory = sqlite3.Row
cur = con.cursor()
action = input(invite_text)
while True:
    try:
        if action == '0':
            break
        elif action == '1':
            template, res = select_all_jokes(con, cur)
            show_res(template, res)
        elif action == '2':
            template, res = select_top_jokes(con, cur)
            show_res(template, res)
        elif action == '3':
            print("Выберите id розыгрыша:")
            template, res = select_all_jokes(con, cur)
            show_res(template, res)
            id = input('Ответ --> ')
            template, res = show_joke_info(con, cur, id)
            show_res(template, res)
        elif action == '4':
            print("Выберите id розыгрыша:")
            template, res = select_all_jokes(con, cur)
            show_res(template, res)
            id = input('Ответ --> ')
            template, res = show_people_info(con, cur, id)
            show_res(template, res)
        else:
            print('Неизвестная команда\n')
        action = input()
    except DBAccessError as err:
        print("Произошла ошибка подключения к базе данных: {}\n".format(err))
        action = input("Попробуйте снова\n")

con.close()
