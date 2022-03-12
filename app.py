from flask import Flask,request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

RESPONSES_KEY = "responses"

app = Flask(__name__)
app.config['SECRET_KEY'] = 'helloworld'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False 

debug = DebugToolbarExtension(app)

@app.route('/')
def homepage():
    return render_template('base.html', survey=survey)


@app.route('/start')
def start_survey():
    session[RESPONSES_KEY] = []
    return redirect('/questions/0')


@app.route("/answer", methods=["POST"])
def handle_question():

    choice = request.form['answer']

    responses = session[RESPONSES_KEY]
    responses.append(choice)
    session[RESPONSES_KEY] = responses

    if (len(responses) == len(survey.questions)):
        return redirect("/finished")

    else:
        return redirect(f"/questions/{len(responses)}")


@app.route('/questions/<int:qid>')
def questions(qid):
    responses = session.get(RESPONSES_KEY)
    if(responses is None):
        return redirect('/')
    if(len(responses) == len(survey.questions)):
        return redirect('/finished')
    if(len(responses) != qid):
        flash(f"Invalid question id: {qid}.")
    question = survey.questions[qid]
    return render_template('question.html', question_num=qid, question=question)


@app.route("/finished")
def complete():
    return render_template("finished.html")










# @app.route('/questions/0')
# def questions_page_1():
#     return render_template('question_1.html', questions=questions)

# @app.route('/questions/1')
# def questions_page_2():
#     return render_template('question_2.html', questions=questions)

# @app.route('/questions/2')
# def questions_page_3():
#     return render_template('question_3.html', questions=questions)

# @app.route('/questions/3')
# def questions_page_4():
#     return render_template('question_4.html', questions=questions)

# @app.route('/answers')
# def answers():
#     return render_template('answers.html', questions=questions)

# @app.route('/answers/new', methods=['POST'])
# def add_answers():
#     answer = request.form['answer']
#     responses.append(answer)
#     return redirect('/questions/1')