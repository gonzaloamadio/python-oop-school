"""
Define entities or members.
A Student has a name, last name, id, classes he attend, quizzes he takes.
A Teacher has a name, last name, id, classes he teaches, quizzes he makes.

ASSUMPTIONS:
    Both teacher and students has two names. Could be more complet / better.

    By design, students can enroll to "running courses", and only running
    courses are courses given by teachers.
    There is no restriction in which course can a student enroll.
    Could be improved by having a hierarchy of courses, or another
    implementation of which courses can students enroll, but I think is out of
    scope of this exercise.
"""
class Person(object):
    """
    Returns a ```Person``` object with given name.

    """
    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name

    def get_names(self):
        "Returns a string containing hole name of the person"
        return "{} {}".format(self.first_name, self.last_name)


class Student(Person):
    """
    Returns a ```Student``` object.

    Atribute
    --------
    first_name : str
        first name of the student
    last_name : str
        last name or surname of the student
    student_id : str
        unique identifier of a student
    classes : list[str]
        list of running courses codes that a student is enroled in.

    """
    def __init__(self, first_name: str, last_name: str, student_id: str) -> None:
        """
        Parameters
        ----------
        first_name : str
            first name of the student
        last_name : str
            last name or surname of the student
        student_id : str
            unique identifier of a student
        """
        Person.__init__(self, first_name, last_name)
        self.student_id = student_id
        self.classes = []

    def get_enroled_courses(self):
        return self.classes

    def enrol(self, course_running):
        """Add course to courses that the student is enroled in."""
        self.classes.append(course_running.running_course_code)
        course_running.add_student(self)



class Teacher(Person):
    """
    Returns a ```Teacher``` object.

    Atribute
    --------
    first_name : str
        first name of the teacher
    last_name : str
        last name or surname of the teacher
    teacher_id : str
        unique identifier of a teacher
    classes : list[str]
        list of running courses codes that the teacher is teaching in.
    """
    def __init__(self, first_name: str, last_name: str, teacher_id: str) -> None:
        """
        Parameters
        ----------
        first_name : str
            first name of the teacher
        last_name : str
            last name or surname of the teacher
        teacher_id : str
            unique identifier of a teacher
        """
        Person.__init__(self, first_name, last_name)
        self.teacher_id = teacher_id
        self.classes = []

    def add_course_to_teach(self, course_code):
        """Add running course to courses that the teacher is teaching in."""
        self.classes.append(course_code)

    def get_teaching_courses(self):
        """Return a list of running courses the teacher is teaching in."""
        return self.classes
