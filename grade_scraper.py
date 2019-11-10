from flask import Flask, redirect, url_for, render_template
import bs4 as bs
import urllib

#import the connection class which takes care of the post request
from connection import connect

user_name = '' #enter username
pass_word = '' #enter password

page = connect(user_name, pass_word) #connection class returns the HTML for the grades page
grades = bs.BeautifulSoup(page.content, 'lxml') #creating a new beautiful soup object which we can scrape for data

weighted_classes = ['Digital Forensics', 'Computer Science III']
nonGPA_classes = ['PSAT Team']
all_courses = []
all_grades = []
courses = {}


#finds the total loss of points for the class
def get_minus(max_grade, grade):
    lost_points = (100-grade)*.1
    if max_grade-lost_points < 0:
        return max_grade
    else:
        return lost_points

#scraping all the course names within the HTML of the grades page
for course in grades.find_all(attrs={'id': 'courseName'}):
    all_courses.append(course.text)

#scraping all the grades for the respective classes
for grade in grades.find_all(attrs={'id': 'average'}):
    #the grades are originally strings so we must convert them to floats (then round them for GPA calculation polcy)
    #if the string is empty the grade is defaulted to 0
    try:
        all_grades.append(round(float(grade.text)))
    except:
        all_grades.append(0)

#creating a dictionary to match the course names to their respective grades for ease in calculations
for course in range(len(all_courses)):
        # to not have repeating classes
        if all_courses.count(all_courses[course]) > 1 and all_grades[course] == 0:
            continue
        courses[all_courses[course]] = all_grades[course]

weighted_total = 0
total_minus = 0
numClasses = len(courses)

#manipulates grade values in order to calculate the GPA
for course in courses:
    #if a course is not factored in GPA, we skip it in calculations
    if course in nonGPA_classes:
        numClasses -= 1
        continue
    elif course in weighted_classes or 'AP' in course:
        weighted_total += 1
        total_minus += get_minus(6, courses[course])
    else:
        total_minus += get_minus(5, courses[course])

#GPA is calculated depending on the types of classes you take then subtracted by the total minus
#the total raw "GPA" is then divided by the number of classes you take to finally get a weighted GPA.
GPA = round((((5*(numClasses-weighted_total) + 6*weighted_total)-total_minus)/numClasses), 3)

app = Flask(__name__)
print(GPA)
@app.route("/")
def home():
    return render_template("gpa.html", courses=courses, GPA=GPA)

if __name__ == "__main__":
    app.run()
