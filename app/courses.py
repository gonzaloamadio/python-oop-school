"""Define classes related with courses.

A Department has courses, can create them, can set them as running for actual year.
They are the responsable for the business logic of courses.

A Course is offered by one Department (every year), has always same name and code.

A RunningCourse, is a course that is actually given a particular year. Each time
they have a list of enrolled students

ASSUMPTIONS:
    A course can be created through a department.
    A course can be running only once a year.

    There are no functions to mark course as finished, and more functionalities.
    Checks, and how information is related are not comprehensive comparing with
    reality, and much more things can be done.
    I consider them out of scope of the exercise.
"""

class Department:
    def __init__(self, name, department_code):
        self.name = name
        self.department_code = department_code
        self.courses = {}

    def add_course(self, description, course_code):
        self.courses[course_code] = Course(description, course_code, self)
        return self.courses[course_code]

    def get_courses(self):
        return self.courses

    @staticmethod
    def add_student_to_course(student, running_course):
        running_course.add_student(student)

    @staticmethod
    def assign_teacher_to_course(teacher, running_course):
        running_course.add_teacher(teacher)
        teacher.add_course_to_teach(running_course.running_course_code)

    @staticmethod
    def mark_course_as_running(course, year):
        # add_running returns a Courserunning
        return course.add_running(year)

class Course:
    def __init__(self, description, course_code, department):
        self.description = description
        self.course_code = course_code
        self.department = department
        #self.department.add_course(self)
        self.runnings = []

    def add_running(self, year):
        """Add this course to the list of running courses, i.e. this course
        running a specific year.

        Parameters
        ----------
        year: str
            year that this course is teached. Mark as running.

        Return
        ------
        c: CourseRunning
            The CourseRunning created that represents this course as running.
        """
        self.runnings.append(CourseRunning(self, year))
        return self.runnings[-1]

    def get_runnings(self):
        return self.runnings


class CourseRunning:
    def __init__(self, course, year, teacher=None):
        self.course = course
        self.year = year
        self.teacher = teacher
        rcc = "{}_{}".format(course.course_code, year)
        self.running_course_code = rcc
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def add_teacher(self, teacher):
        self.teacher = teacher

    def get_students(self):
        return self.students

    def get_code(self):
        return self.running_course_code
