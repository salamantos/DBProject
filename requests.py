# coding=utf-8

from exceptions import *


def execute_request(con, cur, request, *params):
    try:
        cur.execute(request, params)
    except Exception as text:
        raise DBAccessError(text)
    con.commit()
    rows = cur.fetchall()
    key_list = []
    if len(rows) > 0:
        key_list = rows[0].keys()
    return key_list, rows


def select_all_jokes(con, cur):
    request = """
        SELECT id, title AS 'Заголовок', text AS 'Описание', rating AS 'Рейтинг', comment AS 'Отзыв'
        FROM jokes JOIN results ON jokes.id = results.joke_id
    """
    return execute_request(con, cur, request)


def select_top_jokes(con, cur):
    request = """
        SELECT title AS 'Заголовок', text AS 'Описание', rating AS 'Рейтинг', comment AS 'Отзыв'
        FROM jokes JOIN results ON jokes.id = results.joke_id
        WHERE rating > 90
    """
    return execute_request(con, cur, request)


def show_joke_info(con, cur, id):
    request = """
        SELECT title AS 'Заголовок', text AS 'Описание', p_from.name AS 'Кто разыграл',
            rating AS 'Рейтинг', comment AS 'Отзыв'
        FROM jokes JOIN results ON jokes.id = results.joke_id
        JOIN people AS p_from ON p_from.id = jokes.from_who
        WHERE jokes.id = ?
    """
    return execute_request(con, cur, request, id)


def show_people_info(con, cur, id):
    request = """
        SELECT p_give.name AS 'От кого', p_get.name AS 'Кому', rel AS 'Отношения'
        FROM jokes JOIN people AS p_from ON p_from.id = jokes.from_who
        JOIN people_get_joke ON people_get_joke.joke_id = jokes.id
        JOIN people AS p_give ON p_give.id = p_from.id
        JOIN people AS p_get ON p_get.id = people_get_joke.people_id
        LEFT JOIN relationship ON relationship.person1 = p_from.id AND relationship.person2 = p_get.id
        WHERE jokes.id = ?
    """
    return execute_request(con, cur, request, id)
