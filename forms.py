#forms.py
from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField

class AddForm(FlaskForm):
    title = StringField('Title of Anecdote')
    submit = SubmitField('Add Anecdote')

class DelForm(FlaskForm):
    id = IntegerField('ID Number of Anecdote Title to Remove:')
    submit = SubmitField('Remove Anecdote')
