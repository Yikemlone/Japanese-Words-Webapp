from tkinter.messagebox import NO
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


@app.route("/", methods=["GET"])
def index():
    if "settings" in request.cookies:
        return render_template('words.html')

    return render_template("index.html")


# Returns data from the database to the javasScript file.
@app.route("/words-data", methods=["POST", "GET"])
def words_data():
    settings = json.loads(request.cookies.get("settings"))
    
    word_goal = int(settings["WordGoal"])
    goal_type = settings["GoalType"]
    date_to_finish = settings["DateToFinish"]
    words_a_day= int(settings["WordsADay"])
    current_word_index = int(settings["CurrentWordIndex"])
    date_last_used = datetime.strptime(settings["DateLastUsed"], '%Y-%m-%d').date()
    streak = int(settings["Streak"])

    words_data = jpd.select_all(current_word_index, words_a_day)
    
    # !!! Make sure to fix the logic for these ifs. This was used for testing.
    if date_last_used == datetime.utcnow().date():
        current_word_index += int(words_a_day)
        
        if datetime.utcnow().date() != date_last_used + timedelta(days=1):
            streak = 0
        streak += 1
    
    updated_settings = {
        "WordGoal" : word_goal,
        "GoalType": goal_type,
        "DateToFinish" : date_to_finish,
        "WordsADay" : words_a_day,
        "CurrentWordIndex" : current_word_index,
        "DateLastUsed" : datetime.utcnow().date(), 
        "Streak" : streak
    }
    
    return json.dumps({'status':'OK', 'settings': json.dumps(updated_settings, default=str), "data": words_data})


@app.route("/completed", methods=["POST", "GET"])
def completed():
    return render_template('completed.html')
