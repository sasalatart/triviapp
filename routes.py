from flask import Flask, request, render_template, url_for
from app import app
import sys
sys.path.append( 'models' )
from question import Question, NewQuestionForm


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/questions/new', methods=['GET'])
def newQuestion():
    form = NewQuestionForm(request.form)
    if request.method == 'GET':
        return render_template('question_new.html', form=form)
    else:
        return render_template('invalid_request.html')


@app.route('/questions', methods=['POST'])
def questions():
    form = NewQuestionForm(request.form)
    if request.method == 'POST' and form.validate():
        question = Question(form.category.data, form.question.data,
                            form.option_a.data, form.option_b.data,
                            form.option_c.data, form.option_d.data,
                            form.answer.data)
        return render_template('question_created.html', question=question)
    elif request.method == 'POST' and not form.validate():
        return render_template('question_new.html', form=form)
    else:
        return render_template('invalid_request.html')
