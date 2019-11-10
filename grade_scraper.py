import bs4 as bs
import urllib

file = open('googgrades.html') #input HAC static file right here
soup = bs.BeautifulSoup(file, 'lxml')
file.close()

weighted_classes = ['Digital Forensics', 'Computer Science III']
all_courses = []
all_grades = []
courses = {}

for course in soup.find_all(attrs={'id': 'courseName'}):
    if course.text not in all_courses:
        all_courses.append(course.text)

for grade in soup.find_all(attrs={'id': 'average'}):
    try:
        all_grades.append(round(float(grade.text)))
    except:
        all_grades.append(0)

for course in range(len(all_courses)):
    courses[all_courses[course]] = all_grades[course]

print(all_courses)
print(all_grades)
