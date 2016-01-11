from wtforms import Form, TextField, SelectField, HiddenField, validators


class Question:
    questions_id = 0

    def __init__(self, category, question, option_a, option_b, option_c, option_d, answer):
        Question.questions_id += 1

        self.id = Question.questions_id
        self.category = category
        self.question = question
        self.option_a = option_a
        self.option_b = option_b
        self.option_c = option_c
        self.option_d = option_d
        self.answer = answer


class NewQuestionForm(Form):
    category = SelectField('Category',
                           choices=[('animals', 'Animals'),
                                    ('arts', 'Arts'),
                                    ('computing', 'Computing'),
                                    ('entertainment', 'Entertainment'),
                                    ('geography', 'Geography'),
                                    ('government', 'Government'),
                                    ('history', 'History'),
                                    ('mathematics', 'Mathematics'),
                                    ('other', 'Other'),
                                    ('people', 'People'),
                                    ('phrases', 'Phrases'),
                                    ('politics', 'Politics'),
                                    ('science', 'Science'),
                                    ('words', 'Words')],
                           validators=[validators.Required()])

    question = TextField('Question',
                         validators=[validators.Required(),
                                     validators.Length(min=3, max=200)])
    option_a = TextField('Option A',
                         validators=[validators.Required(),
                                     validators.Length(min=1, max=200)])
    option_b = TextField('Option B',
                         validators=[validators.Required(),
                                     validators.Length(min=1, max=200)])
    option_c = TextField('Option C',
                         validators=[validators.Required(),
                                     validators.Length(min=1, max=200)])
    option_d = TextField('Option D',
                         validators=[validators.Required(),
                                     validators.Length(min=1, max=200)])
    answer = SelectField('Answer',
                         choices=[('a', 'A'),
                                  ('b', 'B'),
                                  ('c', 'C'),
                                  ('d', 'D')],
                         validators=[validators.Required()])


class AnswerForm(Form):
    answer = HiddenField('Answer',
                         validators=[validators.Required(),
                                     validators.AnyOf(['a', 'b', 'c', 'd'],
                                                      message=u'Invalid value, must be one of: %(values)s',
                                                      values_formatter=None)])
