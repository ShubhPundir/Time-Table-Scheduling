import tkinter as tk
from tkinter import ttk
from NewBase1 import course_list, faculty_list, section_list
import random

class TimetableApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Timetable App")

        self.section_label = ttk.Label(self.master, text="Select Section:")
        self.section_label.grid(row=0, column=0, padx=10, pady=10)

        self.sections = [section.section_name for section in section_list]
        self.section_var = tk.StringVar()
        self.section_combobox = ttk.Combobox(self.master, textvariable=self.section_var, values=self.sections)
        self.section_combobox.grid(row=0, column=1, padx=10, pady=10)

        self.show_courses_button = ttk.Button(self.master, text="Show Courses", command=self.show_courses)
        self.show_courses_button.grid(row=1, column=0, columnspan=2, pady=10)

        self.timetable_text = tk.Text(self.master, height=10, width=50)
        self.timetable_text.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        self.display_timetable_button = ttk.Button(self.master, text="Display Timetable", command=self.display_timetable)
        self.display_timetable_button.grid(row=3, column=0, columnspan=2, pady=10)

    def show_courses(self):
        selected_section_name = self.section_var.get()
        selected_section = next(section for section in section_list if section.section_name == selected_section_name)
        courses = section_courses(selected_section)

        timetable_text_content = f"Courses for Section {selected_section_name}:\n"
        for course in courses:
            timetable_text_content += f"- {course}\n"

        self.timetable_text.delete(1.0, tk.END)
        self.timetable_text.insert(tk.END, timetable_text_content)

    def display_timetable(self):
        self.timetable_text.delete(1.0, tk.END)
        for sec in section_list:
            timetable_text_content = f'Section {sec.section_name} Timetable:\n'
            for row, cols in sec.timetable.items():
                timetable_text_content += f'{row}: {cols}\n'
            timetable_text_content += '----' * 20 + '\n\n'
            self.timetable_text.insert(tk.END, timetable_text_content)

    def update_text_widget(self, content):
        self.timetable_text.insert(tk.END, content + "\n")

def display_timetable(temp):
    for row, cols in temp.timetable.items():
        app.update_text_widget(f"{row}: {cols}")

def get_faculty(section, course):
    content = f'Section: {section.section_name}\nCourse: {course.course_name}\nFaculty name: {section.courses[course].faculty_name}'
    app.update_text_widget(content)
    return section.courses[course]  # faculty object

def faculty_insert(faculty, day, position, section):
    content = f"Section {section.section_name} successfully scheduled at Day {day} Position {position}."
    app.update_text_widget(content)

def section_insert(section, day, position, course):
    content = f"Class {course.course_name} successfully scheduled at Day {day} Position {position}."
    app.update_text_widget(content)

def check(section, day, position, course):
    position = position - 1
    faculty = section.courses[course]  # get faculty object
    app.update_text_widget(f'FACULTY: {faculty.faculty_name}')
    if course.course_code in section.timetable[day]:
        content = f"Class {course.course_name} is already scheduled on Day {day}. Finding a new day."
        app.update_text_widget(content)
        new_day = random.choice(list(section.timetable.keys()))
        content = f"Trying a new day: {new_day}"
        app.update_text_widget(content)
        check(section, new_day, position + 1, course)
        return
    if section.timetable[day][position] == 0 and faculty.timetable[day][position] == 0:
        # slot free for both faculty and section
        section_insert(section, day, position, course)
        faculty_insert(faculty, day, position, section)
        app.update_text_widget('----' * 50)
        return
    else:
        # case of clash
        content = f"Class slot at Day {day} Position {position} is occupied. Finding a new position."
        app.update_text_widget(content)
        new_position = random.randint(1, 6)
        content = f"Trying a new position: {new_position}"
        app.update_text_widget(content)
        check(section, day, new_position, course)

def section_courses(section):
    content = f'Section: {section.section_name}'
    app.update_text_widget(content)

    courses = []
    for c, f in section.courses.items():
        content = f'Course: {c.course_name}'
        app.update_text_widget(content)
        courses.append(c.course_name)
    return courses

if __name__ == "__main__":
    root = tk.Tk()
    app = TimetableApp(root)
    root.mainloop()

    # Default courses fill up
    default_courses = course_list[0:4]

    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

    for i in default_courses:
        for j in section_list:
            rand_day = random.sample(days, i.course_lectures)  # random day from Monday to Friday
            for d in rand_day:
                slot = random.randint(1, 6)  # random slot from 1 to 6
                check(section=j, day=d, position=slot, course=i)

    for sec in section_list:
        content = f'Section {sec.section_name}'
        app.update_text_widget(content)
        display_timetable(sec)
        app.update_text_widget('----' * 20)
