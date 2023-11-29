## Course

class Course:
    def __init__(self, course_code, course_name, course_lectures, course_labs):
        self.course_code = course_code
        self.course_name = course_name
        self.course_lectures = course_lectures
        self.course_labs = course_labs


course1 = Course(101, "Computer Networks", 3, 1)
course2 = Course(102, "Data Structures", 3, 1)
course3 = Course(103, "Discrete Mathematics", 2, 0)
course4 = Course(104, "Digital Electronics", 2, 1)

major1 = Course(201, "PFDS", 3, 2)
major2 = Course(202, "GDAC", 3, 2)
major3 = Course(203, "EWA", 3, 2)
major4 = Course(204, "CY", 3, 2)
recess = Course(000, "RECESS", 7, 0)

course_list = [course1, course2, course3, course4, major1, major2, major3, major4] ## wihtout recess

## Faculty

class Faculty:
    def __init__(self, faculty_id:int, faculty_name:str, courses_taught:list):
        self.faculty_id = faculty_id
        self.faculty_name = faculty_name
        self.courses_taught = courses_taught

        time_table = dict()
        mon_list = [0]*6
        tue_list = [0]*6
        wed_list = [0]*6
        thu_list = [0]*6
        fri_list = [0]*6
        time_table['Monday'] = mon_list
        time_table['Tuesday'] = tue_list
        time_table['Wednesday'] = wed_list
        time_table['Thursday'] = thu_list
        time_table['Friday'] = fri_list
        self.timetable = time_table



anuradha = Faculty(1, "Anuradha", [course2])
yogita = Faculty(2, "Yogita", [course1, course3])
pooja = Faculty(3, "Pooja", [course4])
neha = Faculty(4, "Neha", [course3])
akanksha = Faculty(5, "Akanksha", [major1])
nisha = Faculty(6, "Nisha", [major2])
shaveta = Faculty(7, "Shaveta", [course1, course2])
pankaj = Faculty(8, "Pankaj", [major3])
prerna = Faculty(9, "Prerna", [major1])
sharda = Faculty(10, "Sharda", [course4])
arjun = Faculty(11, "Arjun", [course4])
anjali = Faculty(12, "Anjali", [course4])
vandana = Faculty(13, "Vandana", [course4])
shilpa = Faculty(14, "Shilpa", [course2])
anshul = Faculty(15, "Anshul", [course2])
neetu = Faculty(16, "Neetu", [course2, course1])
rajni = Faculty(17, "Rajni", [course3])
neeti = Faculty(18, "Neeti", [course3])
mehak = Faculty(19, "Mehak", [course3])
empty = Faculty(20,'EMPTY',[recess])

faculty_list = [anuradha, yogita, pooja, neha, akanksha, nisha, shaveta, pankaj, prerna, sharda, arjun, anjali, vandana, shilpa, anshul, neetu, rajni, neeti, mehak ]

## SECTION

class Section:
    def __init__(self, section_name):
        self.section_name = section_name
        self.courses = {}

        time_table = dict()
        mon_list = [0]*6
        tue_list = [0]*6
        wed_list = [0]*6
        thu_list = [0]*6
        fri_list = [0]*6
        time_table['Monday'] = mon_list
        time_table['Tuesday'] = tue_list
        time_table['Wednesday'] = wed_list
        time_table['Thursday'] = thu_list
        time_table['Friday'] = fri_list
        self.timetable = time_table
        self.reference = [[0]*6]*5

    def add_course(self, course, faculty):
        # self.courses[course.course_code] = {"course_name": course.course_name, "faculty": faculty.faculty_name} #dict
        self.courses[course] = faculty
    
    def section_info(self):
        print("Section:", self.section_name)
        print("Courses:")
        for c, f in self.courses.items():
            print("Course Code:", c.course_code)
            print("Course Name:", c.course_name)
            # print("Faculty:", f.faculty_name)
            # print('FACULTY OBJECT',f)
            print()
    



section_A = Section("A")
section_A.add_course(course1, yogita)
section_A.add_course(course2, anuradha)
section_A.add_course(course3, neha)
section_A.add_course(course4, pooja)
section_A.add_course(major1, akanksha)
# section_A.add_course(recess,empty)

section_B = Section("B")

section_B.add_course(course1, neeti)
section_B.add_course(course2, shilpa)
section_B.add_course(course3, yogita)
section_B.add_course(course4, arjun)
section_B.add_course(major1, prerna)
# section_B.add_course(recess,empty)

section_C = Section("C")
section_C.add_course(course1, yogita)
section_C.add_course(course2, anshul)
section_C.add_course(course3, neha)
section_C.add_course(course4, sharda)
section_C.add_course(major2, nisha)
# section_C.add_course(recess,empty)

section_D = Section("D")
section_D.add_course(course1, neetu)
section_D.add_course(course2, shaveta)
section_D.add_course(course3, neha)
section_D.add_course(course4, anjali)
section_D.add_course(major3, pankaj)
# section_D.add_course(recess,empty)

section_E = Section("E")
section_E.add_course(course1, mehak)
section_E.add_course(course2, neetu)
section_E.add_course(course3, rajni)
section_E.add_course(course4, vandana)
section_E.add_course(major3, shaveta)
# section_E.add_course(recess,empty)

section_list = [section_A, section_B, section_C, section_D, section_E] # list of objects

# print(section_A.section_info())
