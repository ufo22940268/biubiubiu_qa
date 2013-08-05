from flask import Flask
from flask import render_template, url_for, request, flash
import sys
import question

app = Flask(__name__)
DATABASE = "content.db";

app.config.from_object(__name__);

@app.route("/")
def main():
    return render_template("main.html", questions = question.get_questions());

@app.route("/ask_question", methods=['GET', 'POST'])
def ask_question():
    if request.method == 'POST':
        print request.form
        question.add_question(request.form);
        return "";
    else:
        return render_template("ask_question.html");

if __name__ == "__main__":
    app.debug = True;
    app.run()
