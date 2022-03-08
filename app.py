responses = []

from flask import Flask, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey

app = Flask(__name__)
app.config['SECRET_KEY'] = 'helloworld'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False 

debug = DebugToolbarExtension(app)

questions = satisfaction_survey.questions

@app.route('/')
def homepage():
    return render_template('base.html')

@app.route('/questions/0')
def questions_page():
    return render_template('questions.html', questions=questions)


