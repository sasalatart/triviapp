from flask import Flask, flash, redirect, render_template, request, url_for
from app import app
import os
import sys
import redis
import pickle
sys.path.append('models')
from question import Question, NewQuestionForm, AnswerForm

r = redis.StrictRedis(host=os.environ.get('DB_HOST', 'localhost'),
                      port=int(os.environ.get('DB_PORT', 6379)),
                      db=0)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/randomQuestion')
def randomQuestion():
    id = r.srandmember('question:ids')
    return redirect(url_for('question', id=id))


@app.route('/question/<id>', methods=['GET', 'POST'])
def question(id):
    form = AnswerForm(request.form)
    question = pickle.loads(r.get('question:' + id))
    if request.method == 'GET' or (request.method == 'POST' and not form.validate()):
        return render_template('question.html', question=question, form=form)
    elif request.method == 'POST' and form.validate():
        if request.form['answer'] == question.answer:
            flash('Correct!', 'success')
            return randomQuestion()
        else:
            flash('Wrong!', 'error')
            return randomQuestion()
    else:
        return render_template('invalid_request.html')


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
        r.sadd('question:ids', question.id)
        r.set('question:' + str(question.id), pickle.dumps(question))
        return render_template('question_created.html', question=question)
    elif request.method == 'POST' and not form.validate():
        return render_template('question_new.html', form=form)
    else:
        return render_template('invalid_request.html')
