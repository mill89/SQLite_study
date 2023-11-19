import sqlite3 as sq

BASE_NAME = 'meeting schedule.db'
TABLE_NAME = 'media'


def create_db():
    with sq.connect(BASE_NAME) as bs:
        cur = bs.cursor()
        cur.execute(f'''CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
            id_med INTEGER PRIMARY KEY,
            name TEXT,
            rank INTEGER
        )''')


def enter_data(name: str, rank: int, table: str) -> None:
    with sq.connect(BASE_NAME) as bs:
        cur = bs.cursor()
        cur.execute(f'''INSERT INTO {table}(name, rank) VALUES(?, ?)''',
                    (name, rank))


def enter_text():
    table = input('Enter, name table: \n>>> ')
    while True:
        name = input('<table, name, rank>\nTo exit, press Enter"\n>>> ')
        if name == '':
            break
        else:
            rank = int(input('>>> '))
            enter_data(name, rank, table)


if __name__ == '__main__':
    enter_text()
