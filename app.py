import flask from Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"

db = SQLAlchemy(app)

class ToDo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(30))
    completed = db.Column(db.Boolean, default=False)

db.create_all()

sample_todo = Todo(task = "Sample todo", completed = False)

db.session.add(sample_todo)
db.session.commit()

@app.route('/read')
def read():
    all_tasks = ToDo.query.all()
    tasks_string = ""
    for task in all_tasks:
        tasks_string += "<br>"+ task.task + " " + task.completed
    return tasks_string

@app.route('/add/<task>')
def add(task):
    new_task = ToDo(name=task)
    db.session.add(new_task)
    db.session.commit()
    return task + " " + "Added to database"