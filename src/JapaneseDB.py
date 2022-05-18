import sqlite3
import csv


# Creates the database for the the Japanese words. 
def create_db():
    with sqlite3.connect("src/Japanese.db") as connection:
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


# Populates the database with Japanese words
def populate_db():
    with sqlite3.connect("src/Japanese.db") as connection:
        cursor = connection.cursor()

        with open("src/japanese.csv", newline="", encoding="utf8") as csv_file:
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


# ! Need to remember what this is for
def select_multiple_query(amount):
    select_string = f"SELECT jlpt_rating FROM japanese LIMIT {amount}"

    with sqlite3.Connection("src/Japanese.db") as connection:
        cursor = connection.cursor()
        result = cursor.execute(select_string).fetchall()

    return result


# Selects the colum name with the limit of 10.
def select_one(column_name):
    with sqlite3.Connection("src/Japanese.db") as connection:
        cursor = connection.cursor()
        result = cursor.execute(f"SELECT {column_name} FROM japanese LIMIT 10").fetchall()

    return result

# ! need to remember what this does
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

    with sqlite3.Connection("src/Japanese.db") as connection:
        cursor = connection.cursor()
        result = cursor.execute(select_string).fetchall()

    return result


# Selects all the coloms from a range
def select_all(amount, offset):
    with sqlite3.Connection("src/Japanese.db") as connection:
        cursor = connection.cursor()
        data = cursor.execute(f"SELECT * FROM japanese WHERE id >= {amount} AND id <= {int(amount) + int(offset)}").fetchall()
    return data
