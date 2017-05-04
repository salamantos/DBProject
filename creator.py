import sqlite3


def c():
    request = ''
    with open('creation.sql', 'r') as creation_file:
        for line in creation_file:
            request += line
    cur.executescript(request)
    print(cur.lastrowid)
    con.commit()


def d():
    tables = ['relationship', 'people_get_joke', 'results', 'jokes', 'people']
    for table in tables:
        cur.execute('DROP TABLE {}'.format(table))
    con.commit()


action = input('Enter command (e.g. "d")\n  c - create tables\n  d - delete tables\n  r - '
               'recreate tables\n')

con = sqlite3.connect('AprilFoolsJokes.db')
cur = con.cursor()
if action == 'c':
    c()
elif action == 'd':
    d()
elif action == 'r':
    d()
    c()
else:
    print('WHAT???')

con.close()
