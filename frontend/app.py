from flask import Flask, render_template
app = Flask(__name__)

@app.route('/todos')
def view_todos():
    return render_template('todo.html')

if __name__ == '__main__':
    app.run(debug=True) 