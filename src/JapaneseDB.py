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


# Selects all the coloms from a range
def select_all(amount, offset):
    with sqlite3.Connection("src/Japanese.db") as connection:
        cursor = connection.cursor()
        data = cursor.execute(f"SELECT * FROM japanese WHERE id >= {amount} AND id <= {int(amount) + int(offset) - 1}").fetchall()
    return data


# TODO Make a query to sort by category's 

