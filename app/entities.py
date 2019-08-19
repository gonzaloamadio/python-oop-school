"""
Define entities or members.
A Student has a name, last name, id, classes he attend, quizzes he takes.
A Teacher has a name, last name, id, classes he teaches, quizzes he makes.

ASSUMPTIONS:
    Both teacher and students has two names. Could be more complet / better.
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
