from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista zadań przechowywana w pamięci
todo_list = []

@app.route('/')
def index():
    # Wyświetlamy listę zadań na stronie głównej
    return render_template('index.html', todo_list = todo_list, enumerate = enumerate)

@app.route('/add', methods=['POST'])
def add_task():
    # Dodajemy nowe zadanie do listy
    task = request.form.get('task')
    if task:
        todo_list.append({'task': task, 'done': False})
    return redirect(url_for('index'))

@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    # Oznaczamy zadanie jako ukończone
    if 0 <= task_id < len(todo_list):
        todo_list[task_id]['done'] = True
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    if 0 <= task_id < len(todo_list):  # Sprawdzamy czy zadanie istnieje
        del todo_list[task_id]  # Usuwamy zadanie z listy
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
