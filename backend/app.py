from flask import Flask, request, jsonify # we also import 'render_template' to render HTML templates
from dotenv import load_dotenv # we import 'load_dotenv' to load environment variables from a .env file
from urllib.parse import quote_plus
import os # we import 'os' to access environment variables
# from pymongo import MongoClient # we import 'MongoClient' to connect to our MongoDB
import pymongo # we import 'pymongo' to connect to our MongoDB database and perform database operations
from pymongo import MongoClient
from bson import ObjectId

load_dotenv() # we call 'load_dotenv()' to load environment variables from the .env file

username = quote_plus(os.getenv("MONGO_USER"))
password = quote_plus(os.getenv("MONGO_PASS"))

MONGO_URI = f"mongodb+srv://{username}:{password}@rk.9hyvp36.mongodb.net/?appName=RK"

client = MongoClient(MONGO_URI)

db = client["flask-todo-project"]   # database
collection = db["flask-todo-project-collection"]  # collection

app = Flask(__name__)
@app.route('/submittodoitem', methods=["POST"])
def submittodoitem():
    form_data = dict(request.form)
    
    result = collection.insert_one(form_data)
    form_data["_id"] = str(result.inserted_id)
    return form_data

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000, debug=True) 