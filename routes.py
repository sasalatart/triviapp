from flask import Flask, flash, redirect, render_template, request, url_for
from app import app
from question import Question, NewQuestionForm, AnswerForm


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/randomQuestion')
def random_question():
    if Question.random_id():
        return redirect(url_for('question', id=Question.random_id()))
    else:
        flash('No questions found! Please create a new one.', 'negative')
        return new_question()


@app.route('/question/<id>', methods=['GET', 'POST'])
def question(id):
    form = AnswerForm(request.form)
    question = Question.find(id)

    if not question:
        return random_question()

    if request.method == 'GET' or (request.method == 'POST' and not form.validate()):
        return render_template('question.html', question=question, form=form, amount=Question.size())
    elif request.method == 'POST' and form.validate():
        if request.form['answer'] == question.answer:
            flash('Correct!', 'positive')
            return random_question()
        else:
            flash('Wrong Answer!', 'negative')
            return render_template('question.html', question=question, form=form, amount=Question.size())
    else:
        return render_template('invalid_request.html')


@app.route('/questions/new', methods=['GET'])
def new_question():
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
        return render_template('question_created.html', question=question, amount=Question.size())
    elif request.method == 'POST' and not form.validate():
        flash('Oops, your submitted question appears to be invalid.', 'negative')
        return render_template('question_new.html', form=form, amount=Question.size())
    else:
        return render_template('invalid_request.html')
