#!/usr/bin/env python
# coding: utf-8

# In[1]:





# In[2]:


from NewBase import course_list, faculty_list, section_list
import random


# In[ ]:





# In[3]:


## Time table operations
def display_timetable(temp):
    for row,cols in temp.timetable.items():
        print(row,':',cols)

def get_faculty(section,course):
    print('Section:',section.section_name)
    print('Course:',course.course_name)
    print('Faculty name:',section.courses[course].faculty_name)
    return section.courses[course] ## faculty object
        

def faculty_insert(faculty,day,position,section):
    faculty.timetable[day][position] = section.section_name
    print(f"Section {section.section_name} successfully scheduled at Day {day} Position {position}.")
    
def section_insert(section,day,position,course):
    section.timetable[day][position] = course.course_code    
    print(f"Class {course.course_name} successfully scheduled at Day {day} Position {position}.")
    
def check(section,day,position,course):
    position = position - 1
    faculty = section.courses[course] ## get faculty object
    print('FACULTY:',faculty.faculty_name)
    if course.course_code in section.timetable[day]:
        print(f"Class {course.course_name} is already scheduled on Day {day}. Finding a new day.")
        new_day = random.choice(list(section.timetable.keys()))
        print(f"Trying a new day: {new_day}")
        check(section, new_day, position + 1, course)
        return
    if section.timetable[day][position] == 0 and faculty.timetable[day][position] == 0:
        # slot free for both faculty and section
        section_insert(section, day, position, course)
        faculty_insert(faculty, day, position, section)
        print('----'*50)
        return
    else:
        # case of clash
        print(f"Class slot at Day {day} Position {position} is occupied. Finding a new position.")
        new_position = random.randint(1, 6)
        print(f"Trying a new position: {new_position}")
        check(section, day, new_position, course)

    
def section_courses(section):
    courses = []
    print('Section:',section.section_name)
    for c,f in section.courses.items():
#         section.section_info()
        print('Course:',c.course_name)
        courses.append(c.course_name)
#         print('Faculty',get_faculty(section,c))
    return courses


# In[4]:


section_courses(section_list[0])


# In[5]:


## Default courses fill up

default_courses = course_list[0:4]
default_courses


# ## Default courses fill up

# In[6]:


days = ['Monday','Tuesday','Wednesday','Thursday','Friday']

for i in default_courses:
    for j in section_list:
        rand_day = random.sample(days, i.course_lectures) # random day from Monday to Friday
        for d in rand_day:
            slot = random.randint(1, 6) #  random slot from 1 to 6
            check(section=j, day=d, position=slot, course=i)
        
        


# In[ ]:





# In[7]:


for sec in section_list:
    print('Section',sec.section_name)
    display_timetable(sec)
    print('----'*20)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




