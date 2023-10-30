import sqlite3 as sq

# 26.10.2023 | День/ночь | До скольки рабочий день/ночь | Наименование | кол-во | примечание | примерная зп

class JianShe:
    def __init__(self):
        self.planjianshe = 40910
        self.planpechat = 20455
        self.count = 0


    # Функция которая возвращает на каком агрегате работал
    def agregat(self, kakoy:str):
        if kakoy[0].lower() == 'к':
            return self.planjianshe
        elif kakoy[0].lower() == 'п':
            return self.planpechat

    # Функция создания новой таблицы
    def createtable(self):
        with sq.connect('jianShe.db') as con:
            cur = con.cursor()
            cur.execute('''CREATE TABLE jianSheTable(
                date TEXT,
                smena TEXT,
                doskolkismena TEXT,
                name TEXT,
                count INTEGER,
                prim TEXT,
                zp TEXT
                )''')

        print('Create table')


    # Функция обновления таблицы
    def updatetable(self):
        data = input('Введите дату: ')
        smena = input('День/ночь: ')
        doskolkismena = input('До скольки смена: ')
        name = input('Наименование заказа: ')
        count = input('Количество сделанного: ')
        prim = input('Примечание: ')
        myday = [data, smena, doskolkismena, name, count, prim, self.zp(prim, count), ]

        with sq.connect('jianShe.db') as con:
            cur = con.cursor()
            cur.execute('INSERT INTO jianSheTable VALUES (?, ?, ?, ?, ?, ?, ?, ?)', myday)
        print("Обновлено")


    # Функция чтения данных из таблицы
    def readtable(self):
        with sq.connect('jianShe.db') as con:
            cur = con.cursor()
            cur.execute('SELECT * FROM jianSheTable')
            x = cur.fetchall()
            for i in x:
                print(i)


    # Функция которая возвращает подсчет з/п
    def zp(self, prim:str, count):
        if prim[0].lower() == 'к':
            return float(count) * 0.02 + 1364
        elif prim[0].lower() == 'п':
            return self.planpechat * 0.02 + (count - self.planpechat) * 0.05 + 1818
        return None


    # Функция примерного подсчета з/п
    def money(self):
        with sq.connect('jianShe.db') as con:
            cur = con.cursor()
            cur.execute('SELECT count FROM jianSheTable')
            x = cur.fetchall()
            self.count = int(x[-1][0])

        mon = input("На каком агрегате работал? Китай - к, Печать - п.: ")
        if mon == 'к':
            a = self.planjianshe * 0.02 + (self.count - self.planjianshe) * 0.02 + 1364
            print(a)
        elif mon == 'п':
            a = self.planpechat * 0.02 + (self.count - self.planpechat) * 0.05 + 1818
            print(a)


    # Функция удаления строки из таблицы
    def deletetable(self):
        with sq.connect('jianShe.db') as con:
            cur = con.cursor()
            vsl = input("Введите дату: ")
            cur.execute('DELETE FROM jianSheTable WHERE date = ?', (vsl,))
            print('Удалено')

js = JianShe()

dannie = input('Выберите действие: д - Добавить данные, п - Прочитать данные, с - Создать таблицу, в - Выход, у - Удалить, зп: ')

# Основной цикл программы
while dannie != "в":
    if dannie == "д":
        js.updatetable()
        break
    elif dannie == "п":
        js.readtable()
        break
    elif dannie == "с":
        js.createtable()
        break
    elif dannie == "у":
        js.deletetable()
        break
    elif dannie == "зп":
        js.money()
        break
    else:
        print("Вы ввели неверное значение")
        dannie = input('''Выберите действие: д - Добавить данные, 
        п - Прочитать данные, с - Создать таблицу, в - Выход: ''')