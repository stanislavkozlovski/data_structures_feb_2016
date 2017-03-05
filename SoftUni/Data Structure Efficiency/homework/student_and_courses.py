"""
A text file students.txt holds information about students and
    their courses in format {first-name | last-name | course-name} like in the example below.

Write a program to find and print the courses in alphabetical order
    and for each course print its students ordered by last name and then by first name.
"""
import re
from sortedcontainers import SortedSet, SortedDict
FILE_PATH = "students.txt"


class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return '{first_name} {last_name}'.format(first_name=self.first_name, last_name=self.last_name)

    def __gt__(self, other):
        return (self.last_name + self.first_name) > (other.last_name + other.first_name)

    def __lt__(self, other):
        return (self.last_name + self.first_name) < (other.last_name + other.first_name)

    def __eq__(self, other):
        return (self.last_name + self.first_name) == (other.last_name + other.first_name)

    def __hash__(self):
        return hash(self.last_name + self.first_name)


def read_file(file_path):
    """
    Read each student line and returns a list with a list of each student inside of it,
    holding values for the student's first name, last name and course
    """
    with open(file_path, 'r') as students:
        return [list(filter(None, re.split(r'[ |,]', student.rstrip('\n')))) for student in students]


def order_students(students: list):
    """
    :param students: list of students, where each student is represented by a list holding three values
        ['first name', 'last name', 'course']
    :return: A SortedDictionary {key: student's course, value: SortedSet{Person}}
    """
    ordered_students = SortedDict()
    for first_name, last_name, course in students:
        if course not in ordered_students:
            ordered_students[course] = SortedSet()

        ordered_students[course].add(Person(first_name, last_name))

    return ordered_students


def print_output(ordered_students: SortedDict):
    for course, students in ordered_students.items():
        print("{course}: {students}".format(course=course,
                                            students=', '.join(str(student) for student in students)))


def main():
    students = read_file(FILE_PATH)
    ordered_students = order_students(students)
    print_output(ordered_students)



if __name__ == '__main__':
    main()