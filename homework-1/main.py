"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv

connect_db = psycopg2.connect(
    host='localhost',
    database='north',
    user='postgres',
    password=''
)
# Данные для подключение к БД

try:
    with connect_db:
        with connect_db.cursor() as cursor_db:
            with open('north_data/employees_data.csv', encoding='UTF-8') as f:
                file_dict = csv.DictReader(f, delimiter=',')
                for id, line in enumerate(file_dict, 1):
                    cursor_db.execute('INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)',
                                      (id, line['first_name'], line['last_name'], line['title'], line['birth_date'],
                                       line['notes']))
        cursor_db.close()
        # Заполнение таблицы employees

        with connect_db.cursor() as cursor_db:
            with open('north_data/customers_data.csv', encoding='UTF-8') as f:
                file_dict = csv.DictReader(f, delimiter=',')
                for line in file_dict:
                    cursor_db.execute('INSERT INTO customers VALUES (%s, %s, %s)',
                                (line['customer_id'], line['company_name'], line['contact_name']))
        cursor_db.close()
        # Заполнение таблицы customers

