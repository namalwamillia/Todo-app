from flask import Flask,render_template,request,redirect,url_for

#app instance from  Flask app.

app =   Flask(__name__,template_folder='templates')

tasks = []

@app.route('/')
def home():
    return render_template('index.html',tasks=tasks)

@app.route('/add',methods=['POST','GET'])
def create_new_task():
    task = request.form.get('task')
    tasks.append(task)
    return redirect(url_for('home'))


@app.route('/delete_task/<int:task_id>',methods=['POST'])
def delete_task(task_id):
    del tasks[task_id]
    return redirect (url_for('home'))
  
@app.route('/update_task/<int:task_id>', methods=['POST'])
def update_task(task_id):
    if request.method == 'POST':
        updated_task = request.form.get('updated_task')
        if 0 <= task_id< len(tasks):
            tasks[task_id] = updated_task
        return redirect(url_for('home'))  


if __name__ == '__main__':
    app.run(debug=True)