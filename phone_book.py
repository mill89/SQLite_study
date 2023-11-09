import sqlite3 as sq

DB_NAME: str = 'phonebook.db'
TABLE_NAME: str = 'phonebook'


def create_db() -> None:
    # создание БД
    with sq.connect(DB_NAME) as con:
        cur = con.cursor()
        cur.execute(f'''CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
            user_id INTEGER PRIMARY KEY,
            fio TEXT,
            specialization TEXT DEFAULT 'worker',
            number TEXT)''')


def add_data_table(fio: str, specialization: str, phone_number: str) -> None:
    # добавляем данные в таблицу
    with sq.connect(DB_NAME) as con:
        cur = con.cursor()
        cur.execute(f'''INSERT INTO {TABLE_NAME}(fio, specialization, number) VALUES(?, ?, ?)''',
                    (fio, specialization, phone_number))


def get_data() -> list:
    with sq.connect(DB_NAME) as con:
        cur = con.cursor()
        cur.execute(f'''SELECT * FROM {TABLE_NAME}''')
        return cur.fetchall()


def change_data(name_col, new_value, condition=''):
    with sq.connect(DB_NAME) as con:
        cur = con.cursor()
        cur.execute(f'''UPDATE {TABLE_NAME} SET {name_col}=? {condition}''',
                    (new_value,))


def remove_record(col, name):
    with sq.connect(DB_NAME) as con:
        cur = con.cursor()
        cur.execute(f'''DELETE FROM {TABLE_NAME} WHERE {col}=?''', (name,))


def show_bd():
    print('~ Phonebook ~\n')
    for s in get_data():  # чтение из БД
        a, b, c = s[1:]
        print(f'Name: {a} \nspec: {b}, \ntel: {c}\n{'-' * 20}')


if __name__ == '__main__':
    # create_db()  # созданние БД

    # add_data_table(*map(str, input().split()))  # добавление записи в БД

    # change_data('number', '548296994', "WHERE fio LIKE 'milan'") # изменение записив таблице
    # change_data('specialization', 'husband', "WHERE fio LIKE 'milan'")

    # remove_record('fio', '1') # удаление записи из БД

    show_bd()  # вывод данных
