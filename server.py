from flask import Flask
from flask import render_template, url_for
import sys
app = Flask(__name__)

@app.route("/")
def main():
    return render_template("main.html");

@app.route("/ask_question")
def ask_question():
    return render_template("ask_question.html");

if __name__ == "__main__":
    app.debug = True;
    app.run()
