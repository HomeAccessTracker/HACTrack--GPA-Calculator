from connection import connect #connection class returns the HTML for the grades page

import bs4 as bs
import urllib


user_name = ''
pass_word = ''
page = connect(user_name, pass_word) 
soup = bs.BeautifulSoup(page.content, 'html5lib') #creating a new beautiful soup object which we can scrape for data

#extra weighted classes that do not have keyword 'AP' in it
weighted_classes = ['Digital Forensics', 'Computer Science III']
all_courses = []
all_grades = []
courses = {}

#scrapes all the coursenames from the HAC HTML from the site
for course in soup.find_all(attrs={'id': 'courseName'}):
    if course.text not in all_courses:
        all_courses.append(course.text)

#scrapes all the grades from the HAC HTML from the site
for grade in soup.find_all(attrs={'id': 'average'}):
    #it is originally string so it must be converted to a float
    try:
        all_grades.append(round(float(grade.text)))
    except:
        all_grades.append(0)

for course in range(len(all_courses)):
    courses[all_courses[course]] = all_grades[course]
    
weighted_total = 0
total_minus = 0
print(courses)
for course in courses:

    if course in weighted_classes or 'AP' in course:
        weighted_total += 1
    else:
        courses[course] -= 10

    total_minus += (100-courses[course])*.1
    print(total_minus)
    
print(all_courses)
print(all_grades)

GPA = ((5*(len(courses)-weighted_total) + 6*weighted_total)-total_minus)/len(courses)
print(round(GPA, 3)) 
