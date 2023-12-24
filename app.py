from flask import Flask, request, render_template, url_for, redirect
from flask_cors import CORS
import wordparser

app = Flask(__name__)
CORS(app)
wcValues = []
n = 0

@app.route("/")
def helloworld():
    return "Hello World!"

#Members API Route
@app.route("/members")
def members():
    return {"members": ["Member1", "Member2", "Member3"]}

@app.route("/files", methods = ['POST'])
def files():
    dbFiles = request.json.get('input') 
    val = wordparser.getWordValues(dbFiles)
    wcValues.clear()
    wcValues.append(val)
    return {"wordCount": val}


if __name__ == "__main__":
    app.run()