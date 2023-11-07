import sqlite3 as sq

# 26.10.2023 | День/ночь | До скольки рабочий день/ночь | Наименование | кол-во | примечание | примерная зп


class JianShe:
    def __init__(self):
        self.planjianshe = 40910
        self.planpechat = 20455
        self.count = 0



    def agregat(self, kakoy: str):
        '''Функция, которая возвращает на каком агрегате работал'''
        if kakoy[0].lower() == 'к':
            return self.planjianshe
        elif kakoy[0].lower() == 'п':
            return self.planpechat


    def createtable(self):
        '''Функция создания новой таблицы'''
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



    def updatetable(self):
        '''Функция обновления таблицы'''
        data = input('Введите дату: ')
        smena = input('День/ночь: ')
        doskolkismena = input('До скольки смена: ')
        name = input('Наименование заказа: ')
        count = int(input('Количество сделанного: '))
        prim = input('Примечание: ')
        myday = [data, smena, doskolkismena, name, count, prim, self.zp(prim, count), self.planjianshe, None]

        with sq.connect('jianShe.db') as con:
            cur = con.cursor()
            cur.execute('INSERT INTO jianSheTable VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', myday)

        print(f'Примерная зп за день: {round(self.zp(prim, count))}')
        print("Обновлено")



    def readtable(self, date: str):
        '''Функция чтения данных из таблицы'''
        with sq.connect('jianShe.db') as con:
            cur = con.cursor()
            cur.execute(f'SELECT * FROM jianSheTable WHERE date = "{date}"')
            x = cur.fetchall()
            for i in x:
                print(i)



    def zp(self, prim:str, count):
        '''Функция, которая возвращает подсчет з/п'''
        if prim[0].lower() == 'к':
            return float(count) * 0.02 + 1364 if count != 0 else 1364
        elif prim[0].lower() == 'п':
            return self.planpechat * 0.02 + (count - self.planpechat) * 0.05 + 1818 if count != 0 else 1818
        return None



    def money(self):
        '''Функция примерного подсчета з/п'''
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



    def deletetable(self):
        '''Функция удаления последней строки из таблицы'''
        with sq.connect('jianShe.db') as con:
            cur = con.cursor()
            vsl = input("Введите дату: ")
            cur.execute('DELETE FROM jianSheTable WHERE date = ?', (vsl,))
            print('Удалено')

js = JianShe()

dannie = input('''Выберите действие: 
д - Добавить данные, 
п - Прочитать данные, 
с - Создать таблицу, 
в - Выход, 
у - Удалить, 
зп: ''')


# Основной цикл программы
while dannie != "в":
    if dannie == "д":
        js.updatetable()
        break
    elif dannie == "п":
        date = str(input('Введите дату: '))
        js.readtable(date)
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
        print("Вы ввели неверное значение", '********************************', sep='\n')

    dannie = input('''Выберите действие: 
д - Добавить данные, 
п - Прочитать данные, 
с - Создать таблицу, 
в - Выход, 
у - Удалить, 
зп: ''')


