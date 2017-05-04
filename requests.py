# coding=utf-8

from exceptions import *


def execute_request(con, cur, request):
    try:
        cur.execute(request)
    except Exception as text:
        raise DBAccessError(text)
    con.commit()
    return cur.fetchall()


def select_all_jokes(con, cur):
    request = """
        SELECT id, title, text, rating, comment
        FROM jokes JOIN results ON jokes.id = results.joke_id
    """
    return ('id', 'Заголовок', 'Описание', 'Рейтинг', 'Отзыв'), execute_request(con, cur, request)


def select_top_jokes(con, cur):
    request = """
        SELECT title, text, rating, comment
        FROM jokes JOIN results ON jokes.id = results.joke_id
        WHERE rating > 90
    """
    return ('Заголовок', 'Описание', 'Рейтинг', 'Отзыв'), execute_request(con, cur, request)


def show_joke_info(con, cur, id):
    request = """
        SELECT title, text, p_from.name, rating, comment
        FROM jokes JOIN results ON jokes.id = results.joke_id
        JOIN people AS p_from ON p_from.id = jokes.from_who
        WHERE jokes.id = {0}
    """.format(id)
    return ('Заголовок', 'Описание', 'Кто разыграл', 'Рейтинг', 'Отзыв'), \
        execute_request(con, cur, request)


def show_people_info(con, cur, id):
    request = """
        SELECT p_give.name, p_get.name, rel
        FROM jokes JOIN people AS p_from ON p_from.id = jokes.from_who
        JOIN people_get_joke ON people_get_joke.joke_id = jokes.id
        JOIN people AS p_give ON p_give.id = p_from.id
        JOIN people AS p_get ON p_get.id = people_get_joke.people_id
        LEFT JOIN relationship ON relationship.person1 = p_from.id AND relationship.person2 = p_get.id
        WHERE jokes.id = {0}
    """.format(id)
    return ('От кого', 'Кому', 'Отношения'), execute_request(con, cur, request)
