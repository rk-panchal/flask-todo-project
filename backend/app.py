from flask import Flask, request

app = Flask(__name__)
@app.route('/submittodoitem', methods=["POST"])
def submittodoitem():
    form_data = dict(request.form)
    
    result = collection.insert_one(form_data)
    form_data["_id"] = str(result.inserted_id)
    return form_data

if __name__ == '__main__':
    app.run(debug=True) 