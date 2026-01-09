from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "I am alive"

notes = [
        {
            "title": "My first note",
            "body": "This is the body"
        },
        {
            "title": "My second note",
            "body": "This is the second body"
        },
    ]

@app.route("/get-notes")
def get_notes():
    return notes

@app.route("/add-note", methods=["POST"])
def add_note():
    data = request.json

    if ("title" not in data):
        return jsonify(
            {
                "message": "You have no title"
            }
        ), 400

    notes.append({
        "title": data["title"],
        "body": data["body"]
    })
 
    return [
        {
            "title": "My first note",
            "body": "This is the body"
        },
        {
            "title": "My second note",
            "body": "This is the second body"
        },
    ]


if __name__ == "__main__":
    app.run(debug=True)

### Pythonanywhere, heroku, aws beanstalk