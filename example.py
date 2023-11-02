import sqlite3 as sq


def func_decorator(func):
    # декоратор, который подключается к базе и выполняет принимаемую функцию func.
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
    # Печатает примерную зп за весь месяц
    a = print_money()
    my_sum = 0
    for i in a:
        my_sum += float(i)
    print(round(my_sum - (my_sum * 13 / 100), 2))
    print('До вычета налога:', round(my_sum, 2))

@func_decorator
def create_table():
    return input('Введи SQL команду: ')


val = input('Узнать зп за месяц - зп, SQL запрос - sql: ')

if val[0].lower() == 'з':
    printmn()
elif val[0].lower() == 's':
    create_table()

# INSERT INTO nachisleniya(mounth, dateAvans, avans) VALUES ('октябрь', '25,10,2023', 13841.09)
# INSERT INTO nachisleniya(dateOficial, oficial) VALUES ('25,10,2023', 13841.09)
# INSERT INTO nachisleniya(dateNeOficial, neOficial) VALUES ('25,10,2023', 13841.09)
