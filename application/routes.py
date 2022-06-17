from application import app
from application import db
from application.models import ToDo
from flask import redirect, url_for, render_template, request
from application.forms import BasicForm, TodoForm, EditForm

@app.route('/')
def index():
    todo = ToDo.query.all()
    return render_template('task.html', todolist=todo)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/task')
def task():
    return render_template('task.html')

@app.route('/adding', methods=['GET', 'POST'])
def adding():
    message = ""
    form = TodoForm()

    if request.method == 'POST':
        ntask = form.ntask.data
        status = form.status.data
        message = ntask + ' has been added'

        if ntask:
            new_task = ToDo(task=ntask)
            db.session.add(new_task)
            db.session.commit()  

    return render_template('adding.html', form=form, message=message)

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def register():
    message = ""
    form = BasicForm()

    if request.method == 'POST':
        first_name = form.first_name.data
        last_name = form.last_name.data
        food = form.food.data

        if len(first_name) == 0 or len(last_name) == 0:
            message = "Please supply both first and last name"
        else:
            message = f'Thank you, {first_name} {last_name} {food}'

    return render_template('home.html', form=form, message=message)

@app.route('/name')
def name():
    return render_template('name.html')

@app.route('/ben')
def ben():
    return render_template('ben.html')

@app.route('/harry')
def harry():
    return render_template('harry.html')

'''@app.route('/')
def index():
    todo = ToDo.query.first()
    return todo.task'''

'''@app.route('/')
def index():
    todo = ToDo.query.all()
    empstr = ""
    for t in todo:
        empstr += f'{t.id} {t.task} {t.completed} <br>'

    return empstr'''

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

    if todo.completed == False:
        todo.completed = True
    elif todo.completed == True:
        todo.completed = False
    
    db.session.commit()
    
    return redirect(url_for('index'))

@app.route('/updatename/<oldname>/<newname>')
def updatename(oldname, newname):
    select_task = ToDo.query.filter_by(task=oldname).first()
    select_task.task = newname
    db.session.commit()
    return f"{oldname} has been updated to {select_task.task}"

@app.route('/edit', methods=['GET', 'POST', 'PUT'])
def edit():
    message = ""
    form = EditForm()

    if request.method == 'PUT':
        ntask = form.ntask.data
        message = ntask + ' has been updated'

        if ntask:
            select_task = ToDo.query.filter_by(id=1).first()
            select_task.task = ntask
            db.session.commit()  

    return render_template('edit.html', form=form, message=message)

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

@app.route('/deleting/<int:id>')
def deleting(id):
    to_be_del = ToDo.query.get(id)
    db.session.delete(to_be_del)
    db.session.commit()
    return redirect(url_for('index'))