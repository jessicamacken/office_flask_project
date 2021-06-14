# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from datetime import datetime
from model import outcome
import model


# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', time=datetime.now())

@app.route('/results', methods=['GET','POST'])
def results():
    if request.method == 'POST':
        print(request.form)
        user_animal = request.form["animal"]
        user_vacation = request.form["vacation"]
        user_food = request.form["food"]
        outcome_info = outcome(user_animal,user_vacation,user_food)
        return render_template('results.html', user_animal=user_animal, user_vacation=user_vacation, user_food=user_food, outcome_info=outcome_info)
    else:
        return "error"