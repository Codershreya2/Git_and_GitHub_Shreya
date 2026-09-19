from flask import Flask, jsonify, render_template, request
import json
import os
from pymongo import MongoClient
from dotenv import load_dotenv
app = Flask(__name__)
load_dotenv()

mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri)

db = client["git_github_db"]
collection = db["todos"]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api")
def api():
    with open("data.json", "r") as file:
        data = json.load(file)

    return jsonify(data)
@app.route('/submittodoitem', methods=['POST'])
def submit_todo_item():
    item_name = request.form.get('itemName', '').strip()
    item_description = request.form.get('itemDescription', '').strip()

    collection.insert_one({
        'itemName': item_name,
        'itemDescription': item_description
    })

    return "To-Do item submitted successfully"


if __name__ == "__main__":
    app.run(debug=True)