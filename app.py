from flask import Flask, render_template, request, redirect, flash, session

import surveys as s

app = Flask(__name__)

app.config['SECRET_KEY'] = "xBapAYVvZtgRETKAvYhjHiAmZtox8950"


# survey = s.satisfaction_survey  #default
survey = [s.satisfaction_survey]
q_num = [0, 0]

@app.route('/')
def select_survey():
    """Provide list of available surveys to home page template"""
    surveys = s.surveys
    return render_template('home.html', surveys=surveys)

@app.route('/survey')
def begin_survey():
    """Provide selected survey title and instructions to survey template"""
    survey_selection = (request.args['survey'])
    survey[0] = s.surveys[survey_selection]
    q_num[0] = 1
    q_num[1] = len(survey[0].questions)
    title = survey[0].title
    instructions = survey[0].instructions
    return render_template('survey.html', title=title, instructions=instructions)

@app.route('/begin', methods=["POST"])
def record_response():
    session['responses'] = []
    return redirect(('/questions/1'))

@app.route('/questions/<int:num>')
def display_question(num):
    """Provide question/choices based on number"""
    if num != q_num[0]:
        flash('Error: Invalid Request')
        return redirect(f'/questions/{q_num[0]}')
    if q_num[0] > q_num[1]:
        return redirect('/thanks')

    idx = num - 1
    title = survey[0].title
    question = survey[0].questions[idx].question
    choices = survey[0].questions[idx].choices
    return render_template('questions.html', title=title, question=question, \
        choices=choices, num=num)

@app.route('/answer', methods=["POST"])
def record_answer():
    """Append user's posted answer to list of responses and figure out next page"""
    answer = request.form['question']
    responses = session['responses']
    responses.append(answer)
    session['responses'] = responses

    q_num[0] += 1
    url = f'/questions/{q_num[0]}'

    if q_num[0] <= q_num[1]:
        return redirect(url)
    else:
        return redirect('/thanks')

@app.route('/thanks')
def say_thanks():
    return render_template('thanks.html')
    



