# Telegram-бот для работы с базой данных

## Команды бота
/add - добавить товар в базу данных,<br>
/buy - показать список товаров.

## Настройка базы данных SQLite
1. Установить SQLite [по ссылке](https://sqlitestudio.pl)
2. Создать базу данных database.db в папке проекта
3. Добавить таблицу sales
4. Добавим следующие колонки
   * sale_id (INTEGER AUTOINCREMENT PRIMARY KEY) - идентификатор продажи
   * title (VARCHAR(80)) – название магазина
   * shop_name (VARCHAR(40))– название магазина
   * price (REAL) – цена товара
5. Добавить данные:
   * Рубашка тип 10 - Nike  Магазин №7  14.2
   * Штаны тип 6 - Reebok   Магазин №7  47.28
   * Штаны тип 7 - Nike     Магазин №6  95.38

## Запуск бота
1. В Telegram создайте бота с помощью @botfather
2. В файле config.py вставьте полученный токен. 
3. В среду проекта скачайте фреймворк aiogram
   
    pip install aiogram
    
4. Запустить файл main.py
