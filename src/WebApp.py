from flask import Flask, render_template, url_for, request, redirect, make_response
from os.path import exists
from datetime import datetime
import os
import JapaneseDB as jpd
import re
import json

app = Flask(__name__)

SOUNDS = os.path.join('static', 'sounds')


# Allows for the sound files to be uploaded
app.config['UPLOAD_FOLDER'] = SOUNDS


if not exists("src/Japanese.db"):
    jpd.create_db()
    jpd.populate_db()


@app.route("/", methods=["POST", "GET"])
def index():
    if "settings" in request.cookies:
        return words()

    # if request.method == "POST":
    #     words_a_day = request.form.get("words-a-day")
    #     date_to_finish = request.form.get("date-to-finish")
    #     goal_type = request.form.get("goal-type")
    #     word_goal = request.form.get("word-goal")
    #     return set_cookie_data(word_goal, goal_type, date_to_finish, words_a_day)
    
    return render_template("index.html")


@app.route("/words", methods=["POST", "GET"])
def words():
    # TODO This needs to be redone because we can handle this is JavaScript
    # current_words, date, words_per_day = request.cookies.get("data")[1:-1].replace(" ", "").replace("\"", "").split(",")

    # if (int(current_words) - int(words_per_day) / 6000) > 1:
    #     # We will need to figure out the difference left over to make sure we get the last words
    #     return render_template("completed.html")

    # words_data = jpd.select_all(current_words, words_per_day)
    words_page = make_response(render_template('words.html')) #, words_data=words_data))
    # date_last_used = datetime.strptime(date, '%Y-%m-%d').date()

    # if date_last_used == datetime.utcnow().date():
    #     return words_page

    # current_words = str(int(current_words) + int(words_per_day))
    # data = [current_words, date, words_per_day]
    # words_page.set_cookie("data", json.dumps(data))

    return words_page


# Returns data from the database to the javasScript file.
@app.route("/words-data", methods=["POST", "GET"])
def words_data():
    # TODO Get the cookie data here and pass it into this method.

    settings = json.loads(request.cookies.get("settings"))#[1:-1].replace(" ", "").replace("\"", "")
    word_goal = settings["WordGoal"]
    goal_type = settings["GoalType"]
    date_to_finish = settings["DateToFinish"]
    words_a_day= settings["WordsADay"]
    current_word_index = settings["CurrentWordIndex"]
    date_last_used = datetime.strptime(settings["DateLastUsed"], '%Y-%m-%d')
    streak = settings["Streak"]
    
    if date_last_used.strftime('%Y-%m-%d') != datetime.utcnow().date():
        current_word_index += int(words_a_day)
        # print(date_last_used.strftime('%Y-%m-%d'))
        # print(datetime.utcnow().date().strftime('%Y-%m-%d'))
        
    # webpage = make_response(render_template("index.html"))
    # webpage.set_cookie("settings", json.dumps(settings, default=str))

    words_data = jpd.select_all(current_word_index, words_a_day)
    
    return json.dumps({'status':'OK', 'settings': settings, "data": words_data})
    
    
# The daily word limit for the user
def valid_amount(amount):
    if amount is None:
        return False
    return 51 > int(amount) > 0


# ! Not being used right now
def valid_data(content, amount):
    if not content:
        return False
    if re.match(r'^([\s\d]+)$', amount) is None:
        return False
    return True


# Sets the data to a cookie received from index
def set_cookie_data(word_goal, goal_type, date_to_finish, words_a_day):
    # TODO This needs to set the cookie data 
    """
        MATH
        Figure out how many days are from goal
        Figure out the months
        Figure out how many weeks - subtract 2 for each weekend of total days
        Divide days by amount of words
    """
    # Trying to get the difference in days
    # future_date = datetime.strptime("2022-03-22", '%Y-%m-%d').date()
    # total_days = datetime.utcnow().date()
    # days_remaining = (future_date - total_days).days
    # weeks = int(days_remaining / 7)
    # total_months = future_date.month

    webpage = make_response(render_template("index.html"))
    
    settings = {
        "WordGoal" : int(word_goal),
        "GoalType": goal_type,
        "DateToFinish" : date_to_finish,
        "WordsADay" : int(words_a_day),
        "CurrentWordIndex": 0,
        "DateLastUsed" : datetime.utcnow().date(), 
        "Streak" : 0
    }
    
    webpage.set_cookie("settings", json.dumps(settings, default=str))

    return webpage


@app.route("/cookie-data", methods=["GET, POST"])
def set_posted_cookie_data():
        if request.method == "POST":
            words_a_day = request.form.get("words-a-day")
            date_to_finish = request.form.get("date-to-finish")
            goal_type = request.form.get("goal-type")
            word_goal = request.form.get("word-goal")
        return set_cookie_data(word_goal, goal_type, date_to_finish, words_a_day)








# ? May reuse this 
# OPTIONS = {
#     "jlpt_rating": "JLPT",
#     "kanji": "Kanji",
#     "kana": "Kana",
#     "meaning": "Meaning",
#     "sound_file": "Sound",
#     "vocab_type": "Word Type",
#     "expression_kanji": "Expression Kanji",
#     "expression_kana": "Expression Kana",
#     "expression_meaning": "Expression Meaning",
#     "expression_sound_file": "Expression Sound",
#     "furigana": "Furigana",
#     "expression_furigana": "Expression Furigana"
# }

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
