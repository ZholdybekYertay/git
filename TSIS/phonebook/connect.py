import psycopg2
from config import DB_CONFIG  # Импортируем весь словарь целиком

def connect():
    """Подключение к базе данных"""
    # **DB_CONFIG "распаковывает" словарь в аргументы функции
    conn = psycopg2.connect(**DB_CONFIG)
    return conn