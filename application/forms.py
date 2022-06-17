from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, SelectField

class BasicForm(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    food = SelectField('Favourite Food', choices=[('okra soup', 'okra soup'), ('pap', 'pap'), ('jollof', 'jollof')])
    submit = SubmitField('Add Name')

class TodoForm(FlaskForm):
    ntask = StringField('Task')
    status = BooleanField('Status')
    submitted = SubmitField('Add Task')

class EditForm(FlaskForm):
    ntask = StringField('New Task')
    submitted = SubmitField('Edit Task')
