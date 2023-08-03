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


