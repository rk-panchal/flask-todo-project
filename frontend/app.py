from flask import Flask, render_template, request # we also import 'render_template' to render HTML templates

BACKEND_URL = 'http://localhost:1000' 
app = Flask(__name__)

@app.route('/todos')
def view_todos():
    return render_template('todo.html')

@app.route('/submit_todo_item', methods=['POST']) # we specify that this endpoint only accepts POST requests
def submit():
    form_data = dict(request.form) # we can get all form data as a dictionary using 'request.form.to_dict()''
    requests.post(f'{BACKEND_URL}/submittodoitem', data=form_data) # we send the form data to the backend API using 'requests.post()'
    return 'Form submitted successfully!' # we return a success message to the user after submitting the



if __name__ == '__main__':
    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=2000, debug=True) 