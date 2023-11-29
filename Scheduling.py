from NewBase import course_list, faculty_list, section_list

## Time table operations


def display_timetable(temp):
    for row,cols in temp.items():
        print(row,':',cols)

display_timetable(section_list[0].timetable)



def check(self, day, course, position):
    if self.timetable[day][position] == 0:
        
        self.insert(day, course, position)
    else:
        print(f"Class slot at Day {day} Position {position} is occupied.")

def info(section,course):

    print('Section:',section.section_name)
    print('Course:',course.course_name)
    print('Faculty:',section.courses[course].faculty_name)

    # section.timetable[day][position] = course
    # print(f"Class {course} successfully scheduled at Day {day} Position {position}.")


def insert(section,day,position,course):
    section.timetable[day][position] = course.course_code
    print(f"Class {course.course_name} successfully scheduled at Day {day} Position {position}.")



info(section_list[0],course_list[0])
insert(section_list[0],'Monday',2,course_list[0])

display_timetable(section_list[0].timetable)
