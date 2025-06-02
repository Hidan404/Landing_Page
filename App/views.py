from flask import Flask, render_template, request, url_for, redirect
from App import app

tarefas = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/static/<path:path>")
def static_files(path):
    return app.send_static_file(path)

@app.route('/task')
def task():
    return render_template('task_app.html')

@app.route("/todo",methods=['GET', 'POST'])
def todo():
    if request.method == 'POST':
        nova_tarefa = request.form.get('tarefa')
        if nova_tarefa:
            tarefas.append(nova_tarefa)
        return redirect(url_for('todo'))    
    
    return render_template('todo_list.html', tarefas=tarefas)



@app.route("/delete", methods=['POST'])
def delete():
    tarefa_id = int(request.form.get('tarefa_id', -1))
    global tarefas
    if 0 <= tarefa_id < len(tarefas):
        tarefas.pop(tarefa_id)
    return redirect(url_for('todo'))

