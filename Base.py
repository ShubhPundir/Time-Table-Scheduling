# FACULTY

class Faculty:
    def __init__(self, faculty_id:int, faculty_name:str, courses_taught:list):
        self.faculty_id = faculty_id
        self.faculty_name = faculty_name
        self.courses_taught = courses_taught

anuradha = Faculty(1, "Anuradha", ["Data Structures"])
yogita = Faculty(2, "Yogita", ["Computer Networks", "Discrete Mathematics"])
pooja = Faculty(3, "Pooja", ["Digital Electronics"])
neha = Faculty(4, "Neha", ["Discrete Mathematics"])
akanksha = Faculty(5, "Akanksha", ["PFDS"])
nisha = Faculty(6, "Nisha", ["GDAC"])
shaveta = Faculty(7, "Shaveta", ["CY", "Data Structures"])
pankaj = Faculty(8, "Pankaj", ["EWA"])
prerna = Faculty(9, "Prerna", ["PFDS"])
sharda = Faculty(10, "Sharda", ["Digital Electronics"])
arjun = Faculty(11, "Arjun", ["Digital Electronics"])
anjali = Faculty(12, "Anjali", ["Digital Electronics"])
vandana = Faculty(13, "Vandana", ["Digital Electronics"])
shilpa = Faculty(14, "Shilpa", ["Data Structures"])
anshul = Faculty(15, "Anshul", ["Data Structures"])
neetu = Faculty(16, "Neetu", ["Data Structures", "Computer Networks"])
rajni = Faculty(17, "Rajni", ["Discrete Mathematics"])
neeti = Faculty(18, "Neeti", ["Computer Networks"])
mehak = Faculty(19, "Mehak", ["Computer Networks"])


## Course

class Course:
    def __init__(self, course_code, course_name, course_faculty, course_lectures, course_labs):
        self.course_code = course_code
        self.course_name = course_name
        self.course_faculty = course_faculty
        self.course_lectures = course_lectures
        self.course_labs = course_labs


course1 = Course(101, "Computer Networks", [yogita, neetu, neeti, mehak], 3, 1)
course2 = Course(102, "Data Structures", [anuradha, shilpa, anshul, neetu, shaveta], 3, 1)
course3 = Course(103, "Discrete Mathematics", [neha, yogita, rajni], 2 , 0)
course4 = Course(104, "Digital Electronics", [pooja, sharda, arjun, anjali, vandana], 2, 1)

major1 = Course(201, "PFDS", [akanksha, prerna], 3, 2)
major2 = Course(202, "GDAC", [nisha], 3, 2)
major3 = Course(203, "EWA", [pankaj], 3, 2)
major4 = Course(204, "CY", [shaveta], 3, 2)
recess = Course(000, "RECESS", [], 1, 0)

#SECTION

class Section:
    def __init__(self, section_name):
        self.section_name = section_name
        self.courses = {}

    def add_course(self, course , faculty):
        self.courses[course.course_code] = {"course_name": course.course_name, "faculty": faculty.faculty_name} #dict

    def section_info(self):
        print("Section:", self.section_name)
        print("Courses:")
        for course_code, info in self.courses.items():
            print("Course Code:", course_code)
            print("Course Name:", {info['course_name']})
            print("Faculty:", {info['faculty']})
            print()



section_A = Section("A")
section_A.add_course(course1, yogita)
section_A.add_course(course2, anuradha)
section_A.add_course(course3, neha)
section_A.add_course(course4, pooja)
section_A.add_course(major1, akanksha)


section_B = Section("B")

section_B.add_course(course1, neeti)
section_B.add_course(course2, shilpa)
section_B.add_course(course3, yogita)
section_B.add_course(course4, arjun)
section_B.add_course(major1, prerna)


section_C = Section("C")
section_C.add_course(course1, yogita)
section_C.add_course(course2, anshul)
section_C.add_course(course3, neha)
section_C.add_course(course4, sharda)
section_C.add_course(major2, nisha)


section_D = Section("D")
section_D.add_course(course1, neetu)
section_D.add_course(course2, shaveta)
section_D.add_course(course3, neha)
section_D.add_course(course4, anjali)
section_D.add_course(major3, pankaj)


section_E = Section("E")
section_E.add_course(course1, mehak)
section_E.add_course(course2, neetu)
section_E.add_course(course3, rajni)
section_E.add_course(course4, vandana)
section_E.add_course(major3, shaveta)

print(section_E.section_info())
