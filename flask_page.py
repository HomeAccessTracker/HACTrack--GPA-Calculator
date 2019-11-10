from flask import Flask, redirect, url_for, render_template

#import the grade_scraper method which takes care of getting the grades
from grade_scraper import get_grades

app = Flask(__name__)

@app.route("/")
def home():
    courses, gpa = get_grades(user_name,pass_word)
    return render_template("gpa.html", courses=courses, GPA=gpa)

if __name__ == "__main__":
    app.run(debug=True)
