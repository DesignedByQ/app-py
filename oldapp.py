'''from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import redirect, url_for

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"

db = SQLAlchemy(app)

class ToDo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(30))
    completed = db.Column(db.Boolean, default=False)

db.drop_all()
db.create_all()

sample_todo = ToDo(task = "Sample todo", completed = False)

db.session.add(sample_todo)
db.session.commit()

@app.route('/')
def index():
    todo = ToDo.query.first()
    return todo.task

@app.route('/')
def index():
    todo = ToDo.query.all()
    empstr = ""
    for t in todo:
        empstr += f'{t.id} {t.task} {t.completed} <br>'

    return empstr

@app.route('/add')
def add():
    return 'Added a new todo'

@app.route('/read')
def read():
    all_tasks = ToDo.query.all()
    tasks_string = ""
    for task in all_tasks:
        tasks_string += "<br>"+ task.task + " " + str(task.completed)
    return tasks_string

@app.route('/update/<extask>/<status>')
def update(extask, status):
    select_task = ToDo.query.filter_by(task=extask).first()
    if status == "True":
        select_task.completed = True
        db.session.commit()
    elif status == "False":
        select_task.completed = False
        db.session.commit()
    return f"{select_task.task} {select_task.completed}"

@app.route('/complete/<int:id>')
def complete(id):
    todo = ToDo.query.get(id)
    todo.completed = True
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/updatename/<oldname>/<newname>')
def updatename(oldname, newname):
    select_task = ToDo.query.filter_by(task=oldname).first()
    select_task.task = newname
    db.session.commit()
    return f"{oldname} has been updated to {select_task.task}"

@app.route('/add/<ntask>')
def add(ntask):
    new_task = ToDo(task=ntask)
    db.session.add(new_task)
    db.session.commit()
    return ntask + " " + "Added to database"

@app.route('/delete/<extask>')
def delete(extask):
    to_be_del = ToDo.query.filter_by(task=extask).first()
    db.session.delete(to_be_del)
    db.session.commit()
    return extask + " " + 'deleted'
    
if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)'''