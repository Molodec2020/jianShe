import sqlite3 as sq


def func_decorator(func):
    def connect_bd(*args, **kwargs):
        with sq.connect('jianShe.db') as con:
            cur = con.cursor()
            cur.execute(func())
            x = [i[0] for i in cur.fetchall()]
        return x
    return connect_bd


@func_decorator
def print_money():
    return 'SELECT zp FROM jianSheTable'


@func_decorator
def print_date():
    return 'SELECT date FROM jianSheTable'

def printmn():
    a = print_money()
    my_sum = 0
    for i in a:
        my_sum += float(i)
        print(i)
    print(round(my_sum - (my_sum * 13 / 100), 2))
    print(my_sum)

printmn()