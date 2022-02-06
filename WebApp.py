from flask import Flask, render_template, url_for, request, redirect
from os.path import exists
import JapaneseDB as jpd

app = Flask(__name__)

if not exists("Japanese.db"):
    jpd.create_db()
    jpd.populate_db()


# Sets the root of the website
@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        amount = 18
        content = request.form.getlist('options')
        data = jpd.select_partial(amount, content)

        return render_template("index.html", options=data, amount=amount)
    else:
        return render_template("index.html")
