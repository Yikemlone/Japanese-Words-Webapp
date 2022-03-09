from flask import Flask, render_template, url_for, request, redirect, make_response
from os.path import exists
from datetime import datetime
import os
import JapaneseDB as jpd
import re
import json

app = Flask(__name__)

SOUNDS = os.path.join('static', 'sounds')
OPTIONS = {
    "jlpt_rating": "JLPT",
    "kanji": "Kanji",
    "kana": "Kana",
    "meaning": "Meaning",
    "sound_file": "Sound",
    "vocab_type": "Word Type",
    "expression_kanji": "Expression Kanji",
    "expression_kana": "Expression Kana",
    "expression_meaning": "Expression Meaning",
    "expression_sound_file": "Expression Sound",
    "furigana": "Furigana",
    "expression_furigana": "Expression Furigana"
}

app.config['UPLOAD_FOLDER'] = SOUNDS

if not exists("Japanese.db"):
    jpd.create_db()
    jpd.populate_db()


@app.route("/", methods=["POST", "GET"])
def index():
    if "data" in request.cookies:
        return words()

    if request.method == "POST":
        amount = request.form.get("words-a-day")
        date = request.form.get("date-to-finish")
        print(date)
        print(amount)
        return set_cookie_data("2", "1")
    else:
        return render_template("index.html")


@app.route("/words", methods=["POST", "GET"])
def words():
    current_words, date, words_per_day = request.cookies.get("data")[1:-1].replace(" ", "").replace("\"", "").split(",")

    if int(current_words) - int(words_per_day) > 6000:
        # We will need to figure out the difference left over to make sure we get the last words
        return render_template("completed.html")

    words_data = jpd.select_all(current_words, words_per_day)
    words_page = make_response(render_template('words.html', words_data=words_data))
    date_last_used = datetime.strptime(date, '%Y-%m-%d').date()

    if date_last_used == datetime.utcnow().date():
        return words_page

    current_words = str(int(current_words) + int(words_per_day))
    data = [current_words, date, words_per_day]
    words_page.set_cookie("data", json.dumps(data))

    return words_page


def valid_amount(amount):
    if amount is None:
        return False
    return 51 > int(amount) > 0


def valid_data(content, amount):
    if not content:
        return False
    if re.match(r'^([\s\d]+)$', amount) is None:
        return False
    return True


def set_cookie_data(time_frame, total_words):
    """
        MATH
        Figure out how many days are from goal
        Figure out the months
        Figure out how many weeks - subtract 2 for each weekend of total days
        Divide days by amount of words
    """
    webpage = make_response(render_template("index.html"))

    future_date = datetime.strptime("2022-03-22", '%Y-%m-%d').date()
    total_days = datetime.utcnow().date()

    days_remaining = (future_date - total_days).days

    weeks = int(days_remaining / 7)
    total_months = future_date.month

    lists = ["21", f"{total_days}", "1"]
    webpage.set_cookie("data", json.dumps(lists))

    return webpage









# def get_data():
#     # content = request.form.getlist("options")
#     amount = request.form.get("words-a-day")
#
#     if not valid_amount(amount):
#         return render_template("index.html", OPTIONS=OPTIONS, error="That's a whole lot of words my guy, we can't do anymore than 50 a day.")
#
#     if "amount" in request.cookies:
#         amount = int(amount) + int(request.cookies.get("amount"))
#     # data = jpd.select_partial(amount, content)
#
#     data = None
#
#     response = make_response(render_template("index.html", data=data, amount=amount, options=OPTIONS, sound_source=SOUNDS))
#     response.set_cookie('amount', str(amount))
#     return response
