# coding=utf-8

from requests import *
import sqlite3

if __name__ != "__main__":
    exit(0)


def show_res(show_get_template, show_get_res):
    for elem in show_get_template:
        print(elem, end='   ')
    print()
    for elem in show_get_res:
        print(elem)


invite_text = '''Введите команду (напр. "1")
  0 - выход
  1 - показать список шуток
  2 - показать шутки с рейтингом > 90%
  3 - вывести подробности по конкретной шутке
  4 - информация о разыгранных людях\n'''

con = sqlite3.connect('AprilFoolsJokes.db')
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
