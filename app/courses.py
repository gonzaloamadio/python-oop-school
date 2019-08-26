"""Define classes related with courses.

A Department has courses, can create them, can set them as running for actual
year. They are the responsable for the business logic of courses.

A Course is offered by one Department (every year), always same name and code.

A RunningCourse, is a course that is actually given a particular year.
Each time they have a list of enrolled students

ASSUMPTIONS:
    A course can be created through a department.
    A course can be running only once a year.

    There are no functions to mark course as finished, and more functionalities
    Checks, and how information is related are not comprehensive comparing with
    reality, and much more things can be done.
    I consider them out of scope of the exercise.
"""
from classroom.app.entities import Student, Teacher
from typings import Dict, List
CoursesInfo = Dict[str, Course]

class Department:
    def __init__(self, name: str, department_code: str) -> None:
        self.name = name
        self.department_code = department_code
        self.courses: CoursesInfo = {} # type: ignore

    def add_course(self, description: str, course_code: str) -> Course:
        """Add course to this department.

        A course is strongly coupled to a department. And a department is in
        charge of managing the course.
        """
        self.courses[course_code] = Course(description, course_code, self) # type: ignore
        return self.courses[course_code] # type: ignore

    def get_courses(self) -> Dict[str, Course]:
        """Return courses belonging to this department."""
        return self.courses

    @staticmethod
    def add_student_to_course(student: Student, running_course) -> None:
        """ ."""
        running_course.add_student(student)

    @staticmethod
    def assign_teacher_to_course(teacher: Teacher, running_course: CourseRunning) -> None:
        running_course.assign_teacher(teacher)
        teacher.add_course_to_teach(running_course.running_course_code)

    @staticmethod
    def mark_course_as_running(course: Course, year: str) -> CourseRunning:
        # add_running returns a CourseRunning
        return course.add_running(year)


class Course:
    def __init__(self, description: str, course_code: str, department: Department) -> None:
        self.description = description
        self.course_code = course_code
        self.department = department
        # self.department.add_course(self)
        self.runnings: List[CourseRunning] = []

    def add_running(self, year: str) -> CourseRunning:
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

    def get_runnings(self) -> List[CourseRunning]:
        """Return the list of classes that are or were teached."""
        return self.runnings


class CourseRunning:
    def __init__(self, course: Course, year: str, teacher: Teacher=None) -> None:
        self.course = course
        self.year = year
        self.teacher = teacher
        rcc = "{}_{}".format(course.course_code, year)
        self.running_course_code = rcc
        self.students: List[Student] = []

    def add_student(self, student: Student) -> None:
        """Add a student to the students that assist to this specific course"""
        self.students.append(student)

    def assign_teacher(self, teacher: Teacher) -> None:
        """Assign a teacher to this specific course."""
        self.teacher = teacher

    def get_students(self) -> List[Student]:
        """Return students assisting to this specific course."""
        return self.students

    def get_code(self) -> str:
        """Get code of this specific course."""
        return self.running_course_code
