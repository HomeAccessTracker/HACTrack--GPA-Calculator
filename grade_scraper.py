import bs4 as bs
import urllib

#import the connection class which takes care of the post request
from connection import connect

user_name = input('Enter your username: ')
pass_word = input('Enter your password: ')
page = connect(user_name, pass_word) #connection class returns the HTML for the grades page
grades = bs.BeautifulSoup(page.content, 'html5lib') #creating a new beautiful soup object which we can scrape for data

weighted_classes = ['Digital Forensics', 'Computer Science III']
nonGPA_classes = ['PSAT Team']
all_courses = []
all_grades = []
courses = {}

def get_minus(max_grade, grade):
    #scraping all the course names within the HTML of the grades page
    for course in grades.find_all(attrs={'id': 'courseName'}):
        #check to not include repeat classes
        # if course.text not in all_courses:
        all_courses.append(course.text)

#creating a dictionary to match the course names to their respective grades for ease in calculations
for course in range(len(all_courses)):
    courses[all_courses[course]] = all_grades[course]
    # to not have repeating classes
        if all_courses.count(all_courses[course]) > 1 and all_grades[course] == 0:
            continue
        courses[all_courses[course]] = all_grades[course]

    weighted_total = 0
    total_minus = 0
    numClasses = len(courses)

    #manipulates grade values in order to calculate the GPA
    for course in courses:

#GPA is calculated depending on the types of classes you take then subtracted by the total minus
#the total raw "GPA" is then divided by the number of classes you take to finally get a weighted GPA.
GPA = ((5*(len(courses)-weighted_total) + 6*weighted_total)-total_minus)/len(courses)
GPA = round((((5*(numClasses-weighted_total) + 6*weighted_total)-total_minus)/numClasses), 3)

for course in courses:
    print(course + ':   ', courses[course])
