from flask import Flask, flash, redirect, render_template, request, url_for
from app import app
import sys
sys.path.append('models')
from question import Question, NewQuestionForm, AnswerForm


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/randomQuestion')
def randomQuestion():
    return redirect(url_for('question', id=Question.randomID()))


@app.route('/question/<id>', methods=['GET', 'POST'])
def question(id):
    form = AnswerForm(request.form)
    question = Question.find(id)
    if request.method == 'GET' or (request.method == 'POST' and not form.validate()):
        return render_template('question.html', question=question, form=form, amount=Question.size())
    elif request.method == 'POST' and form.validate():
        if request.form['answer'] == question.answer:
            flash('Correct!', 'positive')
            return randomQuestion()
        else:
            flash('Wrong Answer!', 'negative')
            return randomQuestion()
    else:
        return render_template('invalid_request.html')


@app.route('/questions/new', methods=['GET'])
def newQuestion():
    form = NewQuestionForm(request.form)
    if request.method == 'GET':
        return render_template('question_new.html', form=form, amount=Question.size())
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
        question.save()
        flash('Question successfully created!', 'positive')
        return render_template('index.html')
    elif request.method == 'POST' and not form.validate():
        flash('Oops, your submitted question appears to be invalid.', 'negative')
        return render_template('question_new.html', form=form, amount=Question.size())
    else:
        return render_template('invalid_request.html')
