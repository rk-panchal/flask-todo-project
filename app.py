from flask import Flask
app = Flask(__name__)
@app.route('/api')
def view_data():
    data = {
        'name': 'Updated Flask API',
        'version': '2.0'
    }
    return data
if __name__ == '__main__':
    app.run(debug=True) 