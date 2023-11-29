from NewBase import course_list, faculty_list, section_list
import random
import sys
import pandas as pd
import os

## Time table operations
def display_timetable(temp):
    for row,cols in temp.timetable.items():
        print(row,':',cols)

def get_faculty(section,course):
    # print('Section:',section.section_name)
    # print('Course:',course.course_name)
    # print('Faculty name:',section.courses[course].faculty_name)
    return section.courses[course] ## faculty object
        

def faculty_insert(faculty,day,position,section):
    faculty.timetable[day][position] = section.section_name
    # print(f"Section {section.section_name} successfully scheduled at Day {day} Position {position}.")
    
def section_insert(section,day,position,course):
    section.timetable[day][position] = course.course_code    
    # print(f"Class {course.course_name} successfully scheduled at Day {day} Position {position}.")
    
def single_insert_check(section,day,position,course):
    position = position - 1
    faculty = section.courses[course] ## get faculty object
    # print('FACULTY:',faculty.faculty_name)
    if course.course_code in section.timetable[day]:
        # print(f"Class {course.course_name} is already scheduled on Day {day}. Finding a new day.")
        new_day = random.choice(list(section.timetable.keys()))
        # print(f"Trying a new day: {new_day}")
        single_insert_check(section, new_day, position + 1, course)
        return
    if section.timetable[day][position] == 0 and faculty.timetable[day][position] == 0:
        # slot free for both faculty and section
        section_insert(section, day, position, course)
        faculty_insert(faculty, day, position, section)
        # print('----'*50)
        return
    else:
        # case of clash
        # print(f"Class slot at Day {day} Position {position} is occupied. Finding a new position.")
        new_position = random.randint(1, 6)
        # print(f"Trying a new position: {new_position}")
        single_insert_check(section, day, new_position, course)
        
def double_insert_check(section,day,position,course):
    position = position - 1
    faculty = section.courses[course] ## get faculty object
    # print('FACULTY:',faculty.faculty_name)

    if section.timetable[day][position] == 0 and section.timetable[day][position+1] == 0 and faculty.timetable[day][position] == 0:
        # slot free for both faculty and section
        section_insert(section, day, position, course)
#         print('BAZZZZZINGA')
        section_insert(section, day, position+1, course)
        print()
        faculty_insert(faculty, day, position, section)
#         print('BAZZZZZINGA')
        faculty_insert(faculty, day, position+1, section)
        # print('----'*50)
        return
    else:
        # case of clash
        # print(f"Class slot at Day {day} Position {position} is occupied. Finding a new position.")
        new_position = random.randint(1, 5)
        # print(f"Trying a new position: {new_position}")
        double_insert_check(section, day, new_position, course)

    
def get_major(section):
    d = section.courses
    return list(d.keys())[-1] # returns an object

sys.setrecursionlimit(12000)

## Default courses lineup
default_courses = course_list[0:4]

## Default labs fill up
days = ['Monday','Tuesday','Wednesday','Thursday','Friday']
for i in default_courses:
    for j in section_list:
        rand_day = random.sample(days, i.course_labs) # random day from Monday to Friday
        for d in rand_day:
            slot = random.randint(1, 5) #  random slot from 1 to 5 --> as it's a 2 hour continuous class
            double_insert_check(section=j, day=d, position=slot, course=i)



## Major labs fill up
for sec in section_list:
    major = get_major(sec)
    rand_day = random.sample(days, major.course_labs) # random day from Monday to Friday
    for d in rand_day:
        slot = random.randint(1, 5) #  random slot from 1 to 6
        double_insert_check(section=sec, day=d, position=slot, course=major)


## Default lectures fill up
for i in default_courses:
    for j in section_list:
        rand_day = random.sample(days, i.course_lectures) # random day from Monday to Friday
        for d in rand_day:
            slot = random.randint(1, 6) #  random slot from 1 to 6
            single_insert_check(section=j, day=d, position=slot, course=i)
        

## Major courses fill up
for sec in section_list:
    major = get_major(sec)
    rand_day = random.sample(days, major.course_lectures) # random day from Monday to Friday
    for d in rand_day:
        slot = random.randint(1, 6) #  random slot from 1 to 6
        single_insert_check(section=sec, day=d, position=slot, course=major)

## Displaying sections
for sec in section_list:
    print('Section',sec.section_name)
    display_timetable(sec)
    print('----'*20)


## Saving files
section_timetable = os.path.join('timetables', 'sections')
faculty_timetable = os.path.join('timetables', 'faculty')

try:
    os.makedirs(section_timetable)
    os.makedirs(faculty_timetable)
    print(f"Directory '{section_timetable}' created successfully.")
    print(f"Directory '{faculty_timetable}' created successfully.")
except FileExistsError:
    print(f"Directory '{section_timetable}' already exists.")
    print(f"Directory '{faculty_timetable}' already exists.")

## Section dataset
for sec in section_list:
    df = pd.DataFrame(sec.timetable).T
    name = sec.section_name + '.csv'
    path = os.path.join(section_timetable,name)
    df.to_csv(path,index=True)

## Faculty dataset
for faculty in faculty_list:
    df = pd.DataFrame(faculty.timetable).T
    name = faculty.faculty_name + '.csv'
    path = os.path.join(faculty_timetable,name)
    df.to_csv(path,index=True)

