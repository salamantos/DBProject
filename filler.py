# coding=utf-8

from requests import *
import sqlite3

con = sqlite3.connect('AprilFoolsJokes.db')
cur = con.cursor()

names_list = ['Катя', 'Пётр', 'Александр', 'Марк', 'Георгий', 'Арсений', 'Лиза']
for name in names_list:
    execute_request(con, cur, '''INSERT INTO people (name) VALUES ('{}')'''.format(
        name
    ))

relationship_list = [(1, 2, 'Встречаются'), (3, 4, 'Друзья'), (3, 5, 'Друзья'), (3, 6, 'Друзья'),
                      (3, 7, 'Друзья'), (4, 5, 'Одногруппники')]
for relationship in relationship_list:
    execute_request(con, cur,
                    '''INSERT INTO relationship (person1, person2, rel)
                       VALUES ({0}, {1}, '{2}')'''.format(
                        *relationship
                    ))
    execute_request(con, cur,
                    '''INSERT INTO relationship (person1, person2, rel)
                       VALUES ({1}, {0}, '{2}')'''.format(
                        *relationship
                    ))

jokes_list = [('Белая спина', 1, 'Девушка разыграла своего парня'), ('Почтовая рассылка', 4,
    'Крутой хацкер решил разыграть своих одногруппников, разослав электронные письма')]
for jokes in jokes_list:
    execute_request(con, cur,
                    '''INSERT INTO jokes (title, from_who, text)
                       VALUES ('{0}', {1}, '{2}')'''.format(
                        *jokes
                    ))

people_get_joke_list = [(2, 1), (3, 2), (5, 2), (6, 2), (7, 2)]
for people_get_joke in people_get_joke_list:
    execute_request(con, cur,
                    '''INSERT INTO people_get_joke (people_id, joke_id)
                       VALUES ({0}, {1})'''.format(
                        *people_get_joke
                    ))

results_list = [(1, 95, 'Клёвый розыгрыш!'), (2, 80, 'Не ожидали такого розыгрыша))')]
for results in results_list:
    execute_request(con, cur,
                    '''INSERT INTO results (joke_id, rating, comment)
                       VALUES ({0}, {1}, '{2}')'''.format(
                        *results
                    ))

con.close()
