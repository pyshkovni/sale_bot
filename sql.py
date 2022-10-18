import sqlite3
import re

async def add(title, shop_name, price):
    '''Функиция add(item) добавляет товар в базу данных.'''

    conn = sqlite3.connect('database.db')  # соединение с бд
    cursor = conn.cursor()  # установка курсора бд
    sale_items = []
    sale_items.append((title, shop_name, price))  # добавление элемента в список
    cursor.execute('INSERT INTO sales (title, shop_name, price) VALUES(?, ?, ?)', (title, shop_name, price))  # добавление значений в бд
    conn.commit()  # сохранить изменения
    cursor.close()  # закрыть курсор

async def buy(shop_name):
    '''Функция buy(shop) возвращает список товаров магазина shop.
    Вызов функции buy('*') возвращает спосок товаров по всем магазинам.'''

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    if shop_name == '*':  # вывести все
        cursor.execute('SELECT * FROM sales')
    else:  # выполнить по названию магазина
        cursor.execute('SELECT * FROM sales WHERE shop_name = ?', (shop_name,))
    data = cursor.fetchall()  # извлекает все строки результата запроса в виде списка кортежей
    sale_items = []

    for i in list(data):
        sale_items.append(i)

    g = []

    for i in range(len(data)):
        a = re.sub('|\(|\'|\,|\)', '', str(sale_items[i]))
        g.append(a)
    c = []


    for i in g:
        q = i + '\n'
        c.append(q)

    v = '\n'.join(c)
    return v