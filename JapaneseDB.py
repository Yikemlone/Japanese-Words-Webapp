import sqlite3
import csv


def create_db():
    with sqlite3.connect("Japanese.db") as connection:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE japanese(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                jlpt_rating nvarchar(5),
                kanji nvarchar(60),
                kana nvarchar(50),
                meaning varchar(70),
                sound_file nvarchar(50),
                vocab_type nvarchar(30), 
                expression_kanji nvarchar(200),
                expression_kana nvarchar(200),
                expression_meaning nvarchar(200),
                expression_sound_file nvarchar(60),
                furigana nvarchar(200),
                expression_furigana varchar(350))
            """)


def populate_db():
    with sqlite3.connect("Japanese.db") as connection:
        cursor = connection.cursor()

        with open("japanese.csv", newline="", encoding="utf8") as csv_file:
            spam_reader = csv.reader(csv_file, delimiter=',')
            next(spam_reader)
            count = 0
            for row in spam_reader:
                count += 1
                cursor.execute(f"""
                INSERT INTO japanese values (
                    {count},
                    '{row[0]}',
                    '{row[1]}',
                    '{row[2]}',
                    '{row[3]}',
                    '{row[4]}',
                    '{row[5]}',
                    '{row[6]}',
                    '{row[7]}',
                    '{row[8]}',
                    '{row[9]}',
                    '{row[11]}',
                    '{row[12]}'
                )""")


def select_multiple_query(amount):
    select_string = f"SELECT jlpt_rating FROM japanese LIMIT {amount}"

    with sqlite3.Connection("Japanese.db") as connection:
        cursor = connection.cursor()
        result = cursor.execute(select_string).fetchall()

    return result


def select_one(column_name):
    with sqlite3.Connection("Japanese.db") as connection:
        cursor = connection.cursor()
        result = cursor.execute(f"SELECT {column_name} FROM japanese LIMIT 10").fetchall()

    return result


def select_partial(amount, selected_array):
    select_string = "SELECT "
    last_index = len(selected_array)
    index = 0

    for selected in selected_array:
        index += 1
        if index == last_index:
            select_string += selected + " "
            continue

        select_string += selected + ","

    select_string += f"FROM japanese LIMIT {amount}"

    with sqlite3.Connection("Japanese.db") as connection:
        cursor = connection.cursor()
        result = cursor.execute(select_string).fetchall()

    return result


def select_all(amount, offset):
    with sqlite3.Connection("Japanese.db") as connection:
        cursor = connection.cursor()
        data = cursor.execute(f"SELECT * FROM japanese WHERE id >= {offset} AND id <= {amount}").fetchall()
    return data
