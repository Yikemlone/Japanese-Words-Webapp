from flask import Flask, render_template, url_for, request, redirect, make_response
from os.path import exists
from datetime import datetime
from datetime import timedelta
import os
import JapaneseDB as jpd
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

    return render_template("index.html")


@app.route("/words", methods=["POST", "GET"])
def words():
    # TODO This needs to be redone because we can handle this is JavaScript
    # ? Could still use this
    # if (int(current_words) - int(words_per_day) / 6000) > 1:
    #     # We will need to figure out the difference left over to make sure we get the last words
    #     return render_template("completed.html")

    words_page = make_response(render_template('words.html')) 
    
    return words_page


# Returns data from the database to the javasScript file.
@app.route("/words-data", methods=["POST", "GET"])
def words_data():
    settings = json.loads(request.cookies.get("settings"))
    print(settings)
    word_goal = settings["WordGoal"]
    goal_type = settings["GoalType"]
    date_to_finish = settings["DateToFinish"]
    words_a_day= settings["WordsADay"]
    current_word_index = settings["CurrentWordIndex"]
    date_last_used = datetime.strptime(settings["DateLastUsed"], '%Y-%m-%d').date()
    streak = int(settings["Streak"])

    print(current_word_index)

    if date_last_used == datetime.utcnow().date():
        current_word_index += int(words_a_day)
        
        if datetime.utcnow().date() != date_last_used + timedelta(days=1):
            streak = 0
        streak += 1
    
    print(current_word_index)
    
    updated_settings = {
        "WordGoal" : int(word_goal),
        "GoalType": goal_type,
        "DateToFinish" : date_to_finish,
        "WordsADay" : int(words_a_day),
        "CurrentWordIndex": current_word_index,
        "DateLastUsed" : datetime.utcnow().date(), 
        "Streak" : streak
    }
    
    words_data = jpd.select_all(current_word_index, words_a_day)
    
    return json.dumps({'status':'OK', 'settings': json.dumps(updated_settings, default=str), "data": words_data})


# Sets the data to a cookie received from index
@app.route("/cookie-data", methods=["POST", "GET"])
def set_cookie_data():
    # TODO This needs to set the cookie data 
    if request.method != "POST":
        return
    
    words_a_day = request.form.get("words-a-day")
    date_to_finish = request.form.get("date-to-finish")
    goal_type = request.form.get("goal-type")
    word_goal = request.form.get("word-goal")

    # ? Trying to get the difference in days
    # future_date = datetime.strptime("2022-03-22", '%Y-%m-%d').date()
    # total_days = datetime.utcnow().date()
    # ? May reuse this 
    # days_remaining = (future_date - total_days).days
    # weeks = int(days_remaining / 7)
    # total_months = future_date.month
    
    settings = {
        "WordGoal" : int(word_goal),
        "GoalType": goal_type,
        "DateToFinish" : date_to_finish,
        "WordsADay" : int(words_a_day),
        "CurrentWordIndex": 0,
        "DateLastUsed" : datetime.utcnow().date(), 
        "Streak" : 0
    }
    
    webpage = make_response(render_template("index.html"))
    webpage.set_cookie("settings", json.dumps(settings, default=str))

    # !!! Bug - Need to fix
    # This will cause it so the user must leave the webpage and come back
    # before the cookie will properly update.
    return webpage


# # ! May change this to the other method
# def set_posted_cookie_data():
#         if request.method == "POST":
#             words_a_day = request.form.get("words-a-day")
#             date_to_finish = request.form.get("date-to-finish")
#             goal_type = request.form.get("goal-type")
#             word_goal = request.form.get("word-goal")
#         return set_cookie_data(word_goal, goal_type, date_to_finish, words_a_day)