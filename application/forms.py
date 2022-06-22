from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired

class BasicForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    food = SelectField('Favourite Food', choices=[('okra soup', 'okra soup'), ('pap', 'pap'), ('jollof', 'jollof')])
    submit = SubmitField('Add Name')

class TodoForm(FlaskForm):
    ntask = StringField('Task', validators=[DataRequired()])
    status = BooleanField('Status')
    submitted = SubmitField('Add Task')

class EditForm(FlaskForm):
    otask = StringField('Old Task', validators=[DataRequired()])
    ntask = StringField('New Task', validators=[DataRequired()])
    submitted = SubmitField('Edit Task')


