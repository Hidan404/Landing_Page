from flask import Blueprint, render_template, request, url_for, redirect
from .models import Tarefa
from . import db

views = Blueprint('views', __name__)

@views.route('/')
def index():
    return render_template('index.html')

@views.route("/static/<path:path>")
def static_files(path):
    return views.send_static_file(path)

@views.route('/task')
def task():
    return render_template('task_app.html')

@views.route("todo",methods=['GET', 'POST'])
def todo():
    if request.method == 'POST':
        nova_tarefa = request.form.get('tarefa')
        if nova_tarefa:
            print(f"Nova tarefa digitada: {nova_tarefa}")
            trefa = Tarefa(titulo=nova_tarefa)
            db.session.add(trefa)
            db.session.commit()
        return redirect(url_for('views.todo'))    
    tarefas = Tarefa.query.all()
    return render_template('todo_list.html', tarefas=tarefas)



@views.route("/delete", methods=['POST'])
def delete():
    tarefa_id = int(request.form.get('tarefa_id', -1))
    tarefa = Tarefa.query.get(tarefa_id)
    if tarefa:
        db.session.delete(tarefa)
        db.session.commit()
    return redirect(url_for('views.todo'))

