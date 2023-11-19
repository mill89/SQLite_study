import sqlite3 as sq

BASE_NAME = 'meeting schedule.db'


def create_db():
    table_name = input('Enter, table name: \n>>> ')

    with sq.connect(BASE_NAME) as bs:
        cur = bs.cursor()
        cur.execute(f'''CREATE TABLE IF NOT EXISTS {table_name} (
            id_med INTEGER PRIMARY KEY,
            name TEXT,
            rank INTEGER
        )''')


def insert_bd(name: str, rank: int, table: str) -> None:
    with sq.connect(BASE_NAME) as bs:
        cur = bs.cursor()
        cur.execute(f'''INSERT INTO {table}(name, rank) VALUES(?, ?)''',
                    (name, rank))


def enter_data():
    table = input('Enter, name table: \n>>> ')
    while True:
        name = input('<table, name, rank>\nTo exit, press Enter"\n>>> ')
        if name == '':
            break
        else:
            rank = int(input('>>> '))
            insert_bd(name, rank, table)


if __name__ == '__main__':
    enter_data()
